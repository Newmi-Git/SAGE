from senses import voice as vc
from senses import translator as tl
from datetime import datetime as dt
import os
from memory import memory as mm
import commands
from CoreFunctions import executor
def brain():
    vc.recorder()
    command = tl.transcribe_turbo()
    mm.save_memory(command)
    print("You:" + command)
    if "power" in command or "battery" in command:
        result = executor.execute_tool("change_power_mode", mode="balanced")
        print(result)
    brain()

brain()

