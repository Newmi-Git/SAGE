from fastapi import FastAPI
from CoreFunctions.system_monitor import get_ram_usage, get_disk_usage, get_network_usage
from commands.cpu import get_top_processes
import psutil
from commands.cpu import get_processes


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

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)