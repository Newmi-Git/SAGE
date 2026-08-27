import os
import subprocess
from dictionary import diction

os.startfile(os.getenv("APPDATA"))

command = input("You: ")

if command.lower() == "open appdata":
    print("SAGE: Opening Appdata...")
    os.startfile(os.getenv("APPDATA"))
else:
    print("SAGE: Invalid Command")


POWER_SAVING_GUID = "a1841308-3541-4fab-bc81-f71556f20b4a"
BALANCED_GUID = "381b4222-f694-41f0-9685-ff5bb260df2e"
HIGH_PERFORMANCE_GUID = "8c5e7fda-e8bf-4a96-9a85-a6e23a8c635c"

if "power saving" in command.lower or "power saver" in command.lower and "Enable" in command:
    subprocess.run([
        "powercfg",
        "/setactive",
        POWER_SAVING_GUID
    ])
    print("SAGE: Power saving mode enabled")
else:
    print("SAGE: Invalid command")

if "Display" in command or "power saver" in command and any(word in command in diction.OPEN):
    subprocess.run([
        "powercfg",
        "/setactive",
        POWER_SAVING_GUID
    ])
    print("SAGE: Power saving mode enabled")
else:
    print("SAGE: Invalid command")


