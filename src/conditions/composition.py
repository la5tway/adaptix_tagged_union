from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, List, Literal, Union

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
class AndCondition(CompositionCondition):
    kind: Literal["AndCondition"] = field(default="AndCondition", init=False)

    def satisfied(self, data: RuleData) -> bool:
        answers = [x.satisfied(data) for x in self.conditions]
        return len(answers) > 0 and all(answers)


@dataclass
class OrCondition(CompositionCondition):
    kind: Literal["OrCondition"] = field(default="OrCondition", init=False)

    def satisfied(self, data: RuleData) -> bool:
        return any(condition.satisfied(data) for condition in self.conditions)


@dataclass
class NotCondition:
    condition: CONDITION

    kind: Literal["NotCondition"] = field(default="NotCondition", init=False)

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
