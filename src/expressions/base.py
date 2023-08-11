from __future__ import annotations

from dataclasses import dataclass

from src.typings import RuleData

from ..actions import ACTION
from ..conditions import CONDITION


@dataclass
class Expession:
    condition: CONDITION
    action: ACTION

    def satisfied(self, data: RuleData):
        return self.condition.satisfied(data)

    def execute(self, data: RuleData):
        return self.action.execute(data)
