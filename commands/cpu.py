import subprocess
import psutil

def get_top_processes():
    processes = []
    
    for process in psutil.process_iter(['pid', 'name']):
        if process.pid == 0:
            continue
        try:
            cpu_usage = process.cpu_percent(interval=0.1)
            
            processes.append({
                'pid':process.info['pid'],
                'name':process.info['name'],
                'cpu': cpu_usage
            })
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass
        
    processes.sort(key= lambda x:x['cpu'], reverse=True)
    
    for process in processes[:10]:
        print(f"{process['name']} (PID: {process['pid']}) - {process['cpu']}%")
            
get_top_processes()
