import subprocess
from CoreFunctions.registry import tool
from CoreFunctions.tool import RiskLevel

@tool(
    name="change_power_mode",
    description="Changes the Windows power plan",
    params={"mode": "string"},   # e.g. "balanced", "power saver", "high performance"
    risk=RiskLevel.MODIFY
)




def change_power_mode(mode: str):
    
    POWER_SAVING_GUID = "a1841308-3541-4fab-bc81-f71556f20b4a"
    BALANCED_GUID = "381b4222-f694-41f0-9685-ff5bb260df2e"
    HIGH_PERFORMANCE_GUID = "8c5e7fda-e8bf-4a96-9a85-a6e23a8c635c"
    
    if mode in ("power saving", "power saver"):
        subprocess.run([
            "powercfg",
            "/setactive",
            POWER_SAVING_GUID
        ])
        print("SAGE: Power Saving mode enabled")

    elif mode in ("balanced", "balance"):
        subprocess.run([
            "powercfg",
            "/setactive",
            BALANCED_GUID
        ])

        print("SAGE: Balanced enabled")
    elif mode in ("high power", "high performance"):
        subprocess.run([
            "powercfg",
            "/setactive",
            HIGH_PERFORMANCE_GUID
        ])
        print("SAGE: High Performance enabled")
    else:
        print(f"SAGE: Unknown power mode '{mode}'")


@tool(
    name="show_active_power_mode",
    description="Shows the active power plan",
    params={"mode": "string"},   # e.g. "balanced", "power saver", "high performance"
    risk=RiskLevel.READ_ONLY
)

def show_active_power_mode(show):
    if show in ("show", "active", "power plan"):
        subprocess.run([
            "powercfg",
            "/getactivescheme"
        ])
