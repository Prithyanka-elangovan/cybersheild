import re
log_file="../logs/web_activity_data.log"
with open(log_file,"r") as file:
    lines=file.readlines()
print("Total Log lines:",len(lines))
unauthorized=[line for line in lines if "401" in line]
print("Unauthorized requests:",len(unauthorized))
print("First Unauthorized event:",unauthorized[0].strip())
print("\n401 Unauthorized requests by IP addressess:")
current_ip=None
unauthorized_by_ip={}
for line in lines:
    line=line.strip()
    ip_match =re.match(r"^(\d{1,3}(?:\.\d{1,3}){3}):$",line)
    if ip_match:
       current_ip=ip_match.group(1)
    elif "401" in line and current_ip:
       if current_ip not in unauthorized_by_ip:
          unauthorized_by_ip[current_ip]=0
       unauthorized_by_ip[current_ip]+=1
for ip,count in unauthorized_by_ip.items():
    print(ip,"->",count)       
