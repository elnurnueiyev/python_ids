import re 
import json
import csv 
from collections import Counter
 
with open('C:/Users/elnur/Desktop/ders/pyhton/sers/server_logs.txt') as server_logs: 

    pattern=re.compile(r'(?P<ip>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - - \[(?P<date>.?)\] "(?P<method>GET|POST|PUT|DELETE|PATCH) (?P<url>.?) HTTP/1\.1" (?P<status>\d{3})')


    lines = pattern.finditer(str(server_logs))
    
    lst=[]

    for line in lines: 
        lst.append(line.groupdict())

    for exp in server_logs:
        print(exp)


    fl_ent = [exp['ip'] for exp in lst if exp['status'] == '401' ]

    fl_ent_count = Counter(fl_ent)

    fl_ent_logs = {ip: count for ip, count in fl_ent_count.items() if count > 5}

    with open ('fl_logs.json', 'w') as json_file:
        json.dump(fl_ent_logs, json_file, indent=4)

    print(fl_ent_logs)

    th_ip = {ip: count for ip, count in fl_ent_count.items() if count > 3}

    with open ('th_ip.json', 'w') as json_file:
        json.dump(th_ip, json_file, indent=4 )
    
    print(th_ip) 

    with open ('fl_logs.json', 'r') as file2:
        fl_ent_logs_data = json.load(file2)

    with open ('th_ip.json', 'r') as file2:
        th_ip_data = json.load(file2)

    