import ollama
from CoreFunctions import registry

def build_tool_schema():
    """Convert the registry into Ollama's tool-calling format."""
    schema = []
    for t in registry.all_tools():
        schema.append({
            "type": "function",
            "function": {
                "name": t.name,
                "description": t.description,
                "parameters": {
                    "type": "object",
                    "properties": {
                        k: {"type": "string", "description": f"{k} parameter"}
                        for k in t.params
                    },
                    "required": list(t.params.keys())
                }
            }
        })
    return schema


def select_tool(user_command: str, model: str = "qwen2.5:7b"):
    """
    Sends the command to the local LLM with the tool schema.
    Returns the tool call the model WOULD make, without executing it.
    """
    tools = build_tool_schema()

    response = ollama.chat(
        model=model,
        messages=[{"role": "user", "content": user_command}],
        tools=tools
    )

    message = response["message"]

    if "tool_calls" in message and message["tool_calls"]:
        call = message["tool_calls"][0]
        return {
            "matched": True,
            "tool_name": call["function"]["name"],
            "arguments": call["function"]["arguments"]
        }

    return {
        "matched": False,
        "raw_response": message.get("content", "")
    }