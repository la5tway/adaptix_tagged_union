from __future__ import annotations

from dataclasses import dataclass
from typing import Any, List, Union

from src.tagged import TaggedUnion
from src.typings import RuleData

from .logic import (
    AnyCondition,
    FalseCondition,
    NeitherCondition,
    TrueCondition,
)
from .operator import (
    EqCondition,
    GreaterCondition,
    GreaterOrEqualCondition,
    LessCondition,
    LessOrEqualCondition,
    NotEqCondition,
)


@dataclass
class CompositionCondition:
    conditions: List[CONDITION]


@dataclass
class AndCondition(CompositionCondition, TaggedUnion):
    def satisfied(self, data: RuleData) -> bool:
        answers = [x.satisfied(data) for x in self.conditions]
        return len(answers) > 0 and all(answers)


@dataclass
class OrCondition(CompositionCondition, TaggedUnion):
    def satisfied(self, data: RuleData) -> bool:
        return any(condition.satisfied(data) for condition in self.conditions)


@dataclass
class NotCondition(TaggedUnion):
    condition: CONDITION

    def satisfied(self, data: RuleData) -> bool:
        return not self.condition.satisfied(data)


CONDITION = Union[
    AndCondition,
    AnyCondition,
    EqCondition[Any],
    FalseCondition,
    GreaterCondition[Any],
    GreaterOrEqualCondition[Any],
    LessCondition[Any],
    LessOrEqualCondition[Any],
    NeitherCondition,
    NotCondition,
    NotEqCondition[Any],
    OrCondition,
    TrueCondition,
]
