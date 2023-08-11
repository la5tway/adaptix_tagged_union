from __future__ import annotations

import inspect
from dataclasses import field
from typing import Any


class KindMeta(type):
    """
    Metaclass which ensures all domain event classes are frozen dataclasses.
    """

    def __new__(
        cls,
        name: str,
        bases: tuple[type[Any], ...],
        cls_dict: dict[str, Any],
    ) -> type[Any]:
        ann_key = "__annotations__"
        if ann_key not in cls_dict:
            cls_dict[ann_key] = {}
        cls_dict["__annotations__"]["kind"] = f"Literal[{name}]"
        target = super().__new__(cls, name, bases, cls_dict)
        target.__signature__ = inspect.signature(target.__init__)
        target.kind = field(default=name, init=False)
        return target
