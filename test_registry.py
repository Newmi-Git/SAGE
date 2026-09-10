

import commands  # triggers battery.py's @tool registration
from CoreFunctions import executor, registry

print("Registered tools:", [t.name for t in registry.all_tools()])

result = executor.execute_tool("change_power_mode", mode="balanced")
print("Result:", result)

