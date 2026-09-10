from dataclasses import dataclass as dtc
from enum import Enum as en
from typing import Callable, Any

class RiskLevel(en):
    READ_ONLY = "read_only"
    MODIFY = "modify"
    DESTRUCTIVE = "destructive"

@dtc
class Tool:
    name: str
    description: str
    params: dict[str, str]
    risk: RiskLevel
    fn: Callable[..., Any]

    def run(self, **kwargs):
        return self.fn(**kwargs)