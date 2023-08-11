from __future__ import annotations

from enum import Enum
from typing import Any, Dict, Protocol, TypeVar

RuleData = Dict[str, Any]


class FrameType(str, Enum):
    Cam = "cam"
    Lidar = "lidar"
    Det = "det"
    AI = "ai"
    Vis = "vis"


T = TypeVar("T")


class Mapper(Protocol):
    def load(self, data: Any, tp: type[T], /) -> T:
        ...

    def dump(self, data: T, tp: type[T], /) -> Any:
        ...
