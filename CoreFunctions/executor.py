from CoreFunctions import registry
from memory import memory

def execute_tool(name: str, **kwargs):
    t = registry.get(name)
    if t is None:
        return f"Unknown tool: {name}"

    if t.risk.value in ("modify", "destructive"):
        confirm = input(f"Run '{t.name}' with {kwargs}? (y/n): ")
        if confirm.strip().lower() != "y":
            return "Cancelled."

    result = t.run(**kwargs)
    return result