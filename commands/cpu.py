import psutil
from CoreFunctions.registry import tool
from CoreFunctions.tool import RiskLevel

@tool(
    name="get_processes",
    description="Lists running processes, sorted by CPU or memory usage",
    params={"sort_by": "string", "limit": "int", "name_filter": "string"},
    risk=RiskLevel.READ_ONLY
)

def get_processes(sort_by: str = "cpu", limit: int = 10, name_filter: str = None):
    """
    sort_by: 'cpu' or 'memory'
    limit: how many results to return
    name_filter: optional substring to filter process names by
    """
    processes = []

    for process in psutil.process_iter(['pid', 'name']):
        if process.pid == 0:
            continue
        try:
            cpu_usage = process.cpu_percent(interval=0.1)
            mem_usage = process.memory_percent()
            name = process.info['name']

            if name_filter and name_filter.lower() not in name.lower():
                continue

            processes.append({
                'pid': process.info['pid'],
                'name': name,
                'cpu': round(cpu_usage, 2),
                'memory': round(mem_usage, 2)
            })
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass

    key = 'cpu' if sort_by == 'cpu' else 'memory'
    processes.sort(key=lambda x: x[key], reverse=True)

    return processes[:limit]

if __name__ == "__main__":
    for p in get_processes():
        print(f"{p['name']} (PID: {p['pid']}) - CPU: {p['cpu']}% - RAM: {p['memory']}%")