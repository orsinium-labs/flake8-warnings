import ast
import tokenize
from pathlib import Path
from typing import Iterator, Optional, Sequence
from ._finder import WarningFinder


class Checker:
    name = __package__
    version = '0.0.1'

    def __init__(
        self,
        tree: ast.AST,
        file_tokens: Sequence[tokenize.TokenInfo],
        filename: Optional[str] = None,
    ) -> None:
        self._tokens = file_tokens
        self._filename = filename

    @property
    def _finder(self) -> WarningFinder:
        if not self._filename or self._filename in ('stdout', '-'):
            text = tokenize.untokenize(self._tokens).encode()
            return WarningFinder.from_text(text)
        return WarningFinder.from_path(Path(self._filename))

    def run(self) -> Iterator[tuple]:
        for winfo in self._finder.find():
            yield (
                winfo.line, winfo.col, winfo.message, type(self),
            )
