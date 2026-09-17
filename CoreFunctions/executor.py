from CoreFunctions import registry
from CoreFunctions.db import log_action
from memory import memory

def execute_tool(name: str, **kwargs):
    t = registry.get(name)
    if t is None:
        return f"Unknown tool: {name}"

    if t.risk.value in ("modify", "destructive"):
        confirm = input(f"Run '{t.name}' with {kwargs}? (y/n): ")
        if confirm.strip().lower() != "y":
            log_action(t.name, kwargs, t.risk.value, "Cancelled by user")
            return "Cancelled."

    result = t.run(**kwargs)
    log_action(t.name, kwargs, t.risk.value, result)
    return result