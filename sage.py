from senses import voice as vc
from senses import translator as tl
from datetime import datetime as dt
import os
from memory import memory as mm
import commands
from CoreFunctions import executor
from CoreFunctions import router

def brain():
    while True:
        vc.recorder()
        command = tl.transcribe_turbo()
        mm.save_memory(command)
        print("You:" + command)

        t = router.find_tool_for_command(command)
        if t:
            result = executor.execute_tool(t.name, mode="balanced")  # placeholder kwargs
            print(result)
        else:
            print("SAGE: no matching tool found")

if __name__ == "__main__":
    brain()