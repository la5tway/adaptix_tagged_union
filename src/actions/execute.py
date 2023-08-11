from __future__ import annotations

from dataclasses import dataclass, field
from typing import Literal

from src.typings import RuleData


@dataclass
class ExecuteAction:
    kind: Literal["ExecuteAction"] = field(default="ExecuteAction", init=False)

    def execute(self, data: RuleData):
        print("ExecuteAction")
