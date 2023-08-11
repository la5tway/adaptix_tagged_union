from __future__ import annotations

from dataclasses import dataclass, field
from typing import Literal

from src.typings import RuleData

from .base import T, ValueInputCondition


@dataclass
class EqCondition(ValueInputCondition[T]):
    kind: Literal["EqCondition"] = field(default="EqCondition", init=False)

    def satisfied(self, data: RuleData) -> bool:
        return self.value == data[self.key]


@dataclass
class NotEqCondition(ValueInputCondition[T]):
    kind: Literal["NotEqCondition"] = field(default="NotEqCondition", init=False)

    def satisfied(self, data: RuleData) -> bool:
        return self.value != data[self.key]


@dataclass
class GreaterCondition(ValueInputCondition[T]):
    kind: Literal["GreaterCondition"] = field(default="GreaterCondition", init=False)

    def satisfied(self, data: RuleData) -> bool:
        return data[self.key] > self.value


@dataclass
class LessCondition(ValueInputCondition[T]):
    kind: Literal["LessCondition"] = field(default="LessCondition", init=False)

    def satisfied(self, data: RuleData) -> bool:
        return data[self.key] < self.value


@dataclass
class GreaterOrEqualCondition(ValueInputCondition[T]):
    kind: Literal["GreaterOrEqualCondition"] = field(
        default="GreaterOrEqualCondition", init=False
    )

    def satisfied(self, data: RuleData) -> bool:
        return data[self.key] >= self.value


@dataclass
class LessOrEqualCondition(ValueInputCondition[T]):
    kind: Literal["LessOrEqualCondition"] = field(
        default="LessOrEqualCondition", init=False
    )

    def satisfied(self, data: RuleData) -> bool:
        return data[self.key] <= self.value
