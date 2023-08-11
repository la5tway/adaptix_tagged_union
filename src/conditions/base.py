from dataclasses import dataclass
from typing import Generic, TypeVar

T = TypeVar("T")


@dataclass
class ValueInputCondition(Generic[T]):
    key: str
    value: T
