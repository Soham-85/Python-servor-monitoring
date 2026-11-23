
from monitor import get_warning
def save_log(cpu,ram,disk,status,now):
        try:
                with open("server.log", "a") as file:
                        file.write("________Server Report__________\n")
                
                        file.write(f"Time:{now.strftime('%Y-%m-%d %H:%M:%S')}\n")
                
                        file.write(f"cpu usage{ cpu}\n")
                        file.write(f"ram usage {ram}\n")
                        file.write(f"disk usage {disk}\n")
                        file.write(f"status {status}\n")
                        warning=get_warning(cpu,ram,disk)
                        file.write(f"Warnings are {warning}\n")
        except OSError as e:
                print("Unable to save log",e)