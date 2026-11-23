threshold=80
def monitor_servers(servers):
    warnings=[]
    report={}
    for server,details in servers.items():
        cpu=details["cpu"]
        ram=details["ram"]
        disk=details["disk"]

        if cpu>threshold:
            warnings.append(f"{server} for cpu {cpu}")
        if ram>threshold:
            warnings.append(f"{server} for ram {ram}")
        if disk>threshold:
            warnings.append(f"{server} for disk {disk}")

        if cpu>threshold or ram>threshold or disk>threshold:
            status="Warning"
        else:
            status="Healthy"
        report[server]={
            "cpu":cpu,
            "ram":ram,
            "disk":disk,
            "status":status
        }

       
    if len(warnings)==0:
        warnings.append("all normal")
    return report  


def display_report(report):
    for server,details in report.items():
        cpu=details["cpu"]
        ram=details["ram"]
        disk=details["disk"]
        status=details["status"]

        print( f"{server} cpu {cpu} ram {ram} disk {disk} stauts {status}\n")
a=monitor_servers({
    "Server-01": {"cpu": 45, "ram": 60, "disk": 70},
    "Server-02": {"cpu": 90, "ram": 85, "disk": 50},
    "Server-03": {"cpu": 30, "ram": 40, "disk": 55}
})

display_report(a)