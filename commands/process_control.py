import psutil
import subprocess
from CoreFunctions.registry import tool
from CoreFunctions.tool import RiskLevel

@tool(
    name="kill_process",
    description="Kills a process by PID",
    params={"pid": "int"},
    risk=RiskLevel.DESTRUCTIVE
)
def kill_process(pid: int):
    try:
        proc = psutil.Process(pid)
        proc.terminate()
        proc.wait(timeout=3)
        return f"Process {pid} terminated"
    except psutil.NoSuchProcess:
        return f"No process with PID {pid}"
    except psutil.TimeoutExpired:
        proc.kill()
        return f"Process {pid} force-killed"
    except psutil.AccessDenied:
        return f"Access denied killing PID {pid}"


@tool(
    name="restart_process",
    description="Kills a process by PID and relaunches it from a given executable path",
    params={"pid": "int", "path": "string"},
    risk=RiskLevel.DESTRUCTIVE
)
def restart_process(pid: int, path: str):
    kill_result = kill_process(pid)
    try:
        subprocess.Popen(path)
        return f"{kill_result}. Relaunched from {path}"
    except FileNotFoundError:
        return f"{kill_result}. Could not relaunch: {path} not found"