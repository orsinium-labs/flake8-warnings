from typing import Tuple, Type

from ._base import Extractor, WarningInfo, CODES
from ._decorators import DecoratorsExtractor
from ._docstrings import DocstringsExtractor
from ._warnings import WarningsExtractor
from ._stdlib import StdlibExtractor


__all__ = ["CODES", "EXTRACTORS", "Extractor", "WarningInfo"]
EXTRACTORS: Tuple[Type[Extractor], ...] = (
    DecoratorsExtractor,
    DocstringsExtractor,
    StdlibExtractor,
    WarningsExtractor,
)
