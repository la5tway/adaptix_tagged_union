from __future__ import annotations

from typing import Union

from .execute import ExecuteAction
from .log import LogAction

ACTION = Union[
    LogAction,
    ExecuteAction,
]
__all__ = [
    "LogAction",
    "ACTION",
    "ExecuteAction",
]
