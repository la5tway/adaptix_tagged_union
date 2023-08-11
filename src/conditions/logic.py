from __future__ import annotations

from dataclasses import dataclass

from src.tagged import TaggedUnion
from src.typings import RuleData

from .base import ValueInputCondition


@dataclass
class BooleanCondition(ValueInputCondition[bool]):
    def satisfied(self, data: RuleData) -> bool:
        return bool(data[self.key]) == self.value


@dataclass
class TrueCondition(BooleanCondition, TaggedUnion):
    value: bool = True


@dataclass
class FalseCondition(BooleanCondition, TaggedUnion):
    value: bool = False


@dataclass
class AnyCondition(TaggedUnion):
    def satisfied(self, data: RuleData) -> bool:
        return True


@dataclass
class NeitherCondition(TaggedUnion):
    def satisfied(self, data: RuleData) -> bool:
        return False
