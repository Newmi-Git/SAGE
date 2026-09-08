import psutil
#

def show_cpu_percentage():
    print(psutil.cpu_percent(interval=1))
    
def show_cpu_times_in_seconds_user():
    cpu_time = psutil.cpu_times
    return cpu_time().user


def show_cpu_times_in_minutes_user():
    cpu_time = psutil.cpu_times
    return cpu_time().user / 60


def show_cpu_times_in_hours_user():
    cpu_time = psutil.cpu_times
    return (cpu_time().idle / 60) / 60

print(show_cpu_times_in_hours_user())
