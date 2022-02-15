from typing import Tuple, Type

from ._base import Extractor, WarningInfo
from ._decorators import DecoratorsExtractor
from ._warnings import WarningsExtractor


__all__ = ["EXTRACTORS", "Extractor", "WarningInfo"]
EXTRACTORS: Tuple[Type[Extractor], ...] = (
    DecoratorsExtractor,
    WarningsExtractor,
)
