import subprocess
from CoreFunctions.registry import tool
from CoreFunctions.tool import RiskLevel

@tool(
    name="run_command",
    description="Executes a raw shell command and returns its output",
    params={"cmd": "string"},
    risk=RiskLevel.DESTRUCTIVE
)
def run_command(cmd: str):
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=15)
        return {
            "stdout": result.stdout,
            "stderr": result.stderr,
            "returncode": result.returncode
        }
    except subprocess.TimeoutExpired:
        return {"error": "Command timed out"}