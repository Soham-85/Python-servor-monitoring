import psutil
THRESHOLD=80

def cpu_usage():
        cpu=psutil.cpu_percent(interval=1)
        return cpu



def ram_usage():
            ram=psutil.virtual_memory()
            return ram.percent



def disk_usage():
            disk=psutil.disk_usage('C:\\')
            
            return disk.percent




def check(cpu,ram,disk):
            if cpu>THRESHOLD or ram>THRESHOLD or disk>THRESHOLD:
                return "warning"
            else:
                return "Healthy"

def get_warning(cpu,ram,disk):
        Warnings=[]
        if cpu>THRESHOLD:
                Warnings.append(f"High Cpu usage {cpu}")
        if ram>THRESHOLD:
                Warnings.append(f"High Ram usage {ram}")
        if disk>THRESHOLD:
                Warnings.append(f"High disk usage {disk}")
        if len(Warnings)==0:
                return ["All Metrics normal"]

        return Warnings