from __future__ import annotations

from dataclasses import dataclass

from src.tagged import TaggedUnion
from src.typings import RuleData


@dataclass
class ExecuteAction(TaggedUnion):
    def execute(self, data: RuleData):
        print("ExecuteAction")
