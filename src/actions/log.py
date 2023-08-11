from __future__ import annotations

from dataclasses import dataclass, field
from typing import Literal

from src.typings import RuleData


@dataclass
class LogAction:
    text: str

    kind: Literal["LogAction"] = field(default="LogAction", init=False)

    def execute(self, data: RuleData):
        print(self.text.format_map(data))
