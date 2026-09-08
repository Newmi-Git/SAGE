import subprocess

POWER_SAVING_GUID = "a1841308-3541-4fab-bc81-f71556f20b4a"
BALANCED_GUID = "381b4222-f694-41f0-9685-ff5bb260df2e"
HIGH_PERFORMANCE_GUID = "8c5e7fda-e8bf-4a96-9a85-a6e23a8c635c"


command = input("You: ").lower()

def change_power_mode():
    if (("power saving" in command or "power saver" in command) and "enable" in command):
        subprocess.run([
            "powercfg",
            "/setactive",
            POWER_SAVING_GUID
        ])

        print("SAGE: Balanced mode enabled")

    elif ("balanced" in command and "enable" in command):
        subprocess.run([
            "powercfg",
            "/setactive",
            BALANCED_GUID
        ])

        print("SAGE: High Performance mode enabled")
    elif ("high performance" in command and "enable" in command):
                subprocess.run([
            "powercfg",
            "/setactive",
            HIGH_PERFORMANCE_GUID
        ])
    else:
        print("SAGE: Invalid command")
        
change_power_mode()
