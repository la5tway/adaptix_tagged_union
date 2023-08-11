from __future__ import annotations

from adaptix import Retort

from src.actions import ExecuteAction, LogAction
from src.conditions import AndCondition, GreaterCondition, OrCondition, TrueCondition
from src.expressions import Expession
from src.rule import Rule

retort = Retort()

data = {
    "expressions": [
        {
            "condition": {
                "kind": "AndCondition",
                "conditions": [
                    {"kind": "GreaterCondition", "key": "speed", "value": 0},
                    {
                        "kind": "OrCondition",
                        "conditions": [
                            {"kind": "TrueCondition", "key": "object"},
                            {"kind": "TrueCondition", "key": "barrier"},
                        ],
                    },
                ],
            },
            "action": {
                "kind": "LogAction",
                "text": "ALARM! obstacle detected at speed: {speed}",
            },
        },
        {
            "condition": {
                "kind": "OrCondition",
                "conditions": [
                    {"kind": "GreaterCondition", "key": "speed", "value": 100},
                    {"kind": "TrueCondition", "key": "object"},
                    {"kind": "TrueCondition", "key": "barrier"},
                ],
            },
            "action": {
                "kind": "ExecuteAction",
            },
        },
    ],
}
manual = Rule(
    expressions=[
        Expession(
            condition=AndCondition(
                conditions=[
                    GreaterCondition(key="speed", value=0),
                    OrCondition(
                        conditions=[
                            TrueCondition(key="object"),
                            TrueCondition(key="barrier"),
                        ]
                    ),
                ]
            ),
            action=LogAction(text="ALARM! obstacle detected at speed: {speed}"),
        ),
        Expession(
            condition=OrCondition(
                conditions=[
                    GreaterCondition(key="speed", value=100),
                    TrueCondition(key="barrier"),
                    TrueCondition(key="object"),
                ]
            ),
            action=ExecuteAction(),
        ),
    ]
)
loaded = retort.load(data, Rule)
payload = {"speed": 1, "object": False, "barrier": True}
print("\nbefore retort loaded instance execute")
loaded.execute(payload)
print("\nbefore manual loaded instance execute")
manual.execute(payload)
assert manual == loaded, "instances are not equal"
dumped = retort.dump(loaded)
assert dumped == data, "dumped data are not equal"
