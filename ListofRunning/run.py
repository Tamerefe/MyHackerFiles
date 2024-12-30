import psutil

print(f"{'PID':<10} {'Name':<40} {'Status':<10}")
print("="*60)

for proc in psutil.process_iter():
    try:
        pinfo = proc.as_dict(attrs=['pid', 'name', 'status'])
    except psutil.NoSuchProcess:
        pass
    else:
        print(f"{pinfo['pid']:<10} {pinfo['name']:<40} {pinfo['status']:<10}")

