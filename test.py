from datetime import datetime

from monitor import cpu_usage, ram_usage, disk_usage, check, get_warning
from logger import save_log

# Collect metrics
cpu = cpu_usage()
ram = ram_usage()
disk = disk_usage()

# Analyse metrics
status = check(cpu, ram, disk)
warnings = get_warning(cpu, ram, disk)

# Display report
now = datetime.now()

print("CPU:", cpu)
print("RAM:", ram)
print("Disk:", disk)
print("Status:", status)
print("Warnings:", warnings)

# Save report
save_log(cpu, ram, disk, status, now)

print("Integration test completed")