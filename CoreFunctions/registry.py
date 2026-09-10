from CoreFunctions.tool import Tool, RiskLevel

_REGISTRY: dict[str, Tool] = {}

def register(tool: Tool):
    if tool.name in _REGISTRY:
        raise ValueError(f"Tool '{tool.name}' already registered")
    _REGISTRY[tool.name] = tool

def tool(name: str, description: str, params: dict, risk: RiskLevel = RiskLevel.READ_ONLY):
    def decorator(fn):
        register(Tool(name=name, description=description, params=params, risk=risk, fn=fn))
        return fn
    return decorator

def get(name: str) -> Tool | None:
    return _REGISTRY.get(name)

def all_tools() -> list[Tool]:
    return list(_REGISTRY.values())