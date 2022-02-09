from collections import deque
from typing import Iterator, Tuple, Type
from ._base import Extractor, WarningInfo
from ._warnings import WarningsExtractor
import astroid

EXTRACTORS: Tuple[Type[Extractor], ...] = (
    WarningsExtractor,
)


class WarningFinder:
    _module: astroid.Module
    _extractors: Tuple[Extractor, ...]

    def __init__(self, module: astroid.Module):
        self._module = module
        self._extractors = tuple(e() for e in EXTRACTORS)

    def find(self) -> Iterator[WarningInfo]:
        yield from self._check_imports()

    def _check_imports(self) -> Iterator[WarningInfo]:
        for module in self._get_imported_modules():
            for extractor in self._extractors:
                yield from extractor.extract(module)

    def _get_imported_modules(self) -> Iterator[astroid.Module]:
        for node in self._traverse(self._module):
            if isinstance(node, astroid.Import):
                for name, _alias in node.names:
                    yield self._module.import_module(name)
            if isinstance(node, astroid.ImportFrom):
                yield self._module.import_module(node.modname)

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
