        


import time
from datetime import datetime
from monitor import cpu_usage,ram_usage,disk_usage,check,get_warning
from logger import save_log






def main():
        
        while True:
                
                cpu=cpu_usage()
                ram=ram_usage()
                disk=disk_usage()
                status=check(cpu,ram,disk)
                now=datetime.now()
                print("\n_____ SERVER HEALTH REPORT _____")
                print("Time:", now.strftime("%Y-%m-%d %H:%M:%S"))
                print("CPU:", cpu, "%")
                print("RAM:", ram, "%")
                print("Disk:", disk, "%")
                print("Status:", status)
                print("Warnings:", get_warning(cpu, ram, disk))
                save_log(cpu,ram,disk,status,now)
               
               
               
                time.sleep(10)
if __name__=="__main__":
        main()