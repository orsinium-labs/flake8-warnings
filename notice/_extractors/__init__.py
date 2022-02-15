from typing import Tuple, Type
from ._base import Extractor, WarningInfo
from ._warnings import WarningsExtractor


__all__ = ["EXTRACTORS", "Extractor", "WarningInfo"]
EXTRACTORS: Tuple[Type[Extractor], ...] = (
    WarningsExtractor,
)
