import subprocess
from dictionary.diction import OPEN

POWER_SAVING_GUID = "a1841308-3541-4fab-bc81-f71556f20b4a"
BALANCED_GUID = "381b4222-f694-41f0-9685-ff5bb260df2e"
HIGH_PERFORMANCE_GUID = "8c5e7fda-e8bf-4a96-9a85-a6e23a8c635c"


command = input("You: ").lower()

open_words = [word.lower() for word in OPEN]

if (
    ("power saving" in command or "power saver" in command)
    and "enable" in command
):
    subprocess.run([
        "powercfg",
        "/setactive",
        POWER_SAVING_GUID
    ])

    print("SAGE: Power saving mode enabled")

elif (
    "display" in command
    and any(word in command for word in open_words)
):
    subprocess.run([
        "powercfg",
        "/setactive",
        POWER_SAVING_GUID
    ])

    print("SAGE: Power saving mode enabled")

else:
    print("SAGE: Invalid command")
