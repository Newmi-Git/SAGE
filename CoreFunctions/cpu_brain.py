import psutil
from CoreFunctions.registry import tool
from CoreFunctions.tool import RiskLevel

@tool(
    name="get_cpu_percent",
    description="Returns current CPU usage percentage",
    params={},
    risk=RiskLevel.READ_ONLY
)
def show_cpu_percentage():
    return psutil.cpu_percent(interval=1)

@tool(
    name="get_cpu_time_hours",
    description="Returns CPU idle time in hours since boot",
    params={},
    risk=RiskLevel.READ_ONLY
)
def show_cpu_times_in_hours_user():
    cpu_time = psutil.cpu_times
    return (cpu_time().idle / 60) / 60