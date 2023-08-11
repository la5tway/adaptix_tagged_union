from __future__ import annotations

from dataclasses import dataclass

from src.tagged import TaggedUnion
from src.typings import RuleData


@dataclass
class LogAction(TaggedUnion):
    text: str

    def execute(self, data: RuleData):
        print(self.text.format_map(data))
