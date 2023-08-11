from __future__ import annotations

from dataclasses import dataclass

from src.tagged import TaggedUnion
from src.typings import RuleData

from .base import T, ValueInputCondition


@dataclass
class EqCondition(ValueInputCondition[T], TaggedUnion):
    def satisfied(self, data: RuleData) -> bool:
        return self.value == data[self.key]


@dataclass
class NotEqCondition(ValueInputCondition[T], TaggedUnion):
    def satisfied(self, data: RuleData) -> bool:
        return self.value != data[self.key]


@dataclass
class GreaterCondition(ValueInputCondition[T], TaggedUnion):
    def satisfied(self, data: RuleData) -> bool:
        return data[self.key] > self.value


@dataclass
class LessCondition(ValueInputCondition[T], TaggedUnion):
    def satisfied(self, data: RuleData) -> bool:
        return data[self.key] < self.value


@dataclass
class GreaterOrEqualCondition(ValueInputCondition[T], TaggedUnion):
    def satisfied(self, data: RuleData) -> bool:
        return data[self.key] >= self.value


@dataclass
class LessOrEqualCondition(ValueInputCondition[T], TaggedUnion):
    def satisfied(self, data: RuleData) -> bool:
        return data[self.key] <= self.value
