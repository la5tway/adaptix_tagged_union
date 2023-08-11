from __future__ import annotations

from dataclasses import dataclass
from typing import Any, List

from src.typings import RuleData

from .expressions import Expession


@dataclass
class Rule:
    expressions: List[Expession]

    def execute(self, data: RuleData):
        res: dict[str, Any] = {}
        for expression in self.expressions:
            if expression.satisfied(data):
                res[expression.action.__class__.__name__] = expression.execute(data)
        return res
