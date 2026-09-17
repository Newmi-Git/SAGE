from fastapi import FastAPI
from CoreFunctions.system_monitor import get_ram_usage, get_disk_usage, get_network_usage
from commands.cpu import get_processes
import psutil
from commands.cpu import get_processes
from commands.process_control import kill_process, restart_process
from commands.system_exec import run_command
from CoreFunctions import executor
from CoreFunctions import registry
from CoreFunctions.llm_router import select_tool
from CoreFunctions.db import log_llm_decision


app = FastAPI(title="SAGE")

@app.get("/")
def root():
    return {"status": "SAGE backend running"}

@app.get("/system/cpu")
def cpu():
    return {"percent": psutil.cpu_percent(interval=1)}

@app.get("/system/ram")
def ram():
    return get_ram_usage()

@app.get("/system/disk")
def disk():
    return get_disk_usage("C:\\")  # adjust path for your OS

@app.get("/system/network")
def network():
    return get_network_usage()

@app.get("/system/processes")
def processes(sort_by: str = "cpu", limit: int = 10, name_filter: str = None):
    return get_processes(sort_by=sort_by, limit=limit, name_filter=name_filter)

@app.post("/process/kill/{pid}")
def kill(pid: int, confirm: bool = False):
    if not confirm:
        return {"error": "Confirmation required", "hint": "resend with confirm=true"}
    return {"result": executor.execute_tool("kill_process", auto_confirm=True, pid=pid)}

@app.post("/process/restart/{pid}")
def restart(pid: int, path: str, confirm: bool = False):
    if not confirm:
        return {"error": "Confirmation required", "hint": "resend with confirm=true"}
    return {"result": executor.execute_tool("restart_process", auto_confirm=True, pid=pid, path=path)}

@app.post("/system/run")
def run(cmd: str, confirm: bool = False):
    if not confirm:
        return {"error": "Confirmation required", "hint": "resend with confirm=true"}
    return {"result": executor.execute_tool("run_command", auto_confirm=True, cmd=cmd)}

@app.get("/tools")
def list_tools():
    return [
        {"name": t.name, "description": t.description, "params": t.params, "risk": t.risk.value}
        for t in registry.all_tools()
    ]

@app.post("/llm/decide")
def llm_decide(command: str):
    decision = select_tool(command)
    log_llm_decision(command, decision)
    return decision

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)