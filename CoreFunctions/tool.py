from dataclasses import dataclass
from enum import Enum
from typing import Callable, Any

class RiskLevel(Enum):
    READ_ONLY = "read_only"
    MODIFY = "modify"
    DESTRUCTIVE = "destructive"

@dataclass
class Tool:
    name: str
    description: str
    params: dict[str, str]
    risk: RiskLevel
    fn: Callable[..., Any]

    def run(self, **kwargs):
        return self.fn(**kwargs)