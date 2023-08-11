from __future__ import annotations

import os
from typing import Any, Literal


def get_tagged_union_key(env_key: str = "TAGGED_UNION_KEY"):
    return os.environ.get(env_key, "__")


class TaggedMeta(type):
    __tag = get_tagged_union_key()

    def __new__(
        cls,
        name: str,
        bases: tuple[type[Any], ...],
        cls_dict: dict[str, Any],
    ) -> type[Any]:
        if "__annotations__" not in cls_dict:
            cls_dict["__annotations__"] = {}
        cls_dict["__annotations__"][cls.__tag] = Literal[name]  # type: ignore
        target = super().__new__(cls, name, bases, cls_dict)
        setattr(target, cls.__tag, name)
        return target


class TaggedUnion(metaclass=TaggedMeta):
    ...
