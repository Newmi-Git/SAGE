from senses import voice as vc
from senses import translator as tl
from memory import memory as mm
import commands
from CoreFunctions import cpu_brain, system_monitor
from CoreFunctions.llm_router import select_tool
from CoreFunctions.db import log_llm_decision, init_db

def brain():
    init_db()
    while True:
        vc.recorder()
        command = tl.transcribe_turbo()
        mm.save_memory(command)
        print("You:" + command)

        decision = select_tool(command)
        log_llm_decision(command, decision)

        if decision["matched"]:
            print(f"SAGE would call: {decision['tool_name']}({decision['arguments']})")
        else:
            print(f"SAGE: no tool match. Model said: {decision['raw_response']}")

if __name__ == "__main__":
    brain()