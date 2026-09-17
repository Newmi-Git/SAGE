from CoreFunctions import registry

def find_tool_for_command(command: str):
    """Very simple keyword match against registered tool names/descriptions.
    Replace with the LLM-based selector in Phase 4."""
    command_lower = command.lower()
    for t in registry.all_tools():
        keywords = t.name.replace("_", " ").split() + t.description.lower().split()
        if any(word in command_lower for word in keywords):
            return t
    return None