import datetime as dt
import os
import json 
memory_file = os.path.join(
    os.path.dirname(__file__),
    "memory",
    "conversations.json"
)

def save_memory(text):
    os.makedirs(os.path.dirname(memory_file), exist_ok=True)
    
    if os.path.exists(memory_file):
        with open(memory_file, "r", encoding = "utf-8") as file:
            memories = json.load(file)
    else:
            memories = []
    
    memories.append({
        "timestamp": dt.datetime.now().isoformat(),
        "text": text
    })
    with open(memory_file, "w", encoding = "utf-8") as file:
        json.dump(memories, file, indent=4)
    
    