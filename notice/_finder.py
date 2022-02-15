from collections import deque
from contextlib import suppress
from pathlib import Path
from typing import Iterator, Tuple

import astroid

from ._extractors import EXTRACTORS, Extractor, WarningInfo


class WarningFinder:
    _module: astroid.Module
    _extractors: Tuple[Extractor, ...]

    def __init__(self, module: astroid.Module):
        self._module = module
        self._extractors = tuple(e() for e in EXTRACTORS)

    @classmethod
    def from_path(cls, path: Path) -> 'WarningFinder':
        text = path.read_text()
        module = astroid.parse(code=text, path=str(path))
        return cls(module)

    @classmethod
    def from_text(cls, text: str) -> 'WarningFinder':
        module = astroid.parse(code=text)
        return cls(module)

    def find(self) -> Iterator[WarningInfo]:
        yield from self._check_imports()

    def _check_imports(self) -> Iterator[WarningInfo]:
        for node in self._traverse(self._module):
            for target_node in self._get_imported_nodes(node):
                for extractor in self._extractors:
                    for warning in extractor.extract(target_node):
                        yield warning.evolve(line=node.lineno, col=node.col_offset)

    def _get_imported_nodes(self, node) -> Iterator[astroid.NodeNG]:
        if isinstance(node, astroid.Import):
            for name, _ in node.names:
                with suppress(astroid.AstroidImportError):
                    yield self._module.import_module(name)

        if not isinstance(node, astroid.ImportFrom):
            return
        try:
            module = self._module.import_module(node.modname)
        except astroid.AstroidImportError:
            return
        yield module
        for name, _ in node.names:
            _, resolved_nodes = module.lookup(name)
            for node in resolved_nodes:
                if isinstance(node, (astroid.ClassDef, astroid.FunctionDef)):
                    yield node

    @staticmethod
    def _traverse(node: astroid.NodeNG) -> Iterator[astroid.NodeNG]:
        todo = deque([node])
        while todo:
            node = todo.popleft()
            todo.extend(node.get_children())
            yield node

    # @staticmethod
    # def _infer(expr) -> Tuple[astroid.NodeNG, ...]:
    #     if not isinstance(expr, astroid.NodeNG):
    #         return tuple()
    #     with suppress(astroid.InferenceError, RecursionError):
    #         guesses = expr.infer()
    #         if guesses is astroid.Uninferable:  # pragma: no cover
    #             return tuple()
    #         return tuple(g for g in guesses if repr(g) != 'Uninferable')
    #     return tuple()
