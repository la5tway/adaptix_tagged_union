from __future__ import annotations

from dataclasses import dataclass, field
from typing import Literal

from src.typings import RuleData

from .base import ValueInputCondition


@dataclass
class BooleanCondition(ValueInputCondition[bool]):
    def satisfied(self, data: RuleData) -> bool:
        return bool(data[self.key]) == self.value


@dataclass
class TrueCondition(BooleanCondition):
    value: bool = True
    kind: Literal["TrueCondition"] = field(default="TrueCondition", init=False)


@dataclass
class FalseCondition(BooleanCondition):
    value: bool = False
    kind: Literal["FalseCondition"] = field(default="FalseCondition", init=False)


@dataclass
class AnyCondition:
    kind: Literal["AnyCondition"] = field(default="AnyCondition", init=False)

    def satisfied(self, data: RuleData) -> bool:
        return True


@dataclass
class NeitherCondition:
    kind: Literal["NeitherCondition"] = field(default="NeitherCondition", init=False)

    def satisfied(self, data: RuleData) -> bool:
        return False
