from __future__ import annotations

from adaptix import Retort

from src.actions import ExecuteAction, LogAction
from src.conditions import AndCondition, GreaterCondition, OrCondition, TrueCondition
from src.expressions import Expession
from src.rule import Rule
from src.tagged import get_tagged_union_key

TAG = get_tagged_union_key()
retort = Retort()

data = {
    "expressions": [
        {
            "condition": {
                TAG: "AndCondition",
                "conditions": [
                    {TAG: "GreaterCondition", "key": "speed", "value": 0},
                    {
                        TAG: "OrCondition",
                        "conditions": [
                            {TAG: "TrueCondition", "key": "object"},
                            {TAG: "TrueCondition", "key": "barrier"},
                        ],
                    },
                ],
            },
            "action": {
                TAG: "LogAction",
                "text": "ALARM! obstacle detected at speed: {speed}",
            },
        },
        {
            "condition": {
                TAG: "OrCondition",
                "conditions": [
                    {TAG: "GreaterCondition", "key": "speed", "value": 100},
                    {TAG: "TrueCondition", "key": "object"},
                    {TAG: "TrueCondition", "key": "barrier"},
                ],
            },
            "action": {
                TAG: "ExecuteAction",
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
dumped = retort.dump(loaded)
print(dumped)
