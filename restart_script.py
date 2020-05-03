import subprocess

# read the `docker ps | grep "healthy)" > grep.txt` report
with open("grep.txt", "r") as file:
    raw = file.readlines()[0]

# if 'unhealthy' not in raw:
#     print("no unhealthy containers")
#     exit(0)

# this means unhealthy is in the file:
splits = raw.split()

print(splits[len(splits)-1] + " is an unhealthy container")
restart_string = "docker restart " + splits[len(splits)-1] + "\n"

with open("restart_container.sh", "w") as file:
    file.write("#!/bin/bash\n")
    file.write(restart_string)

cmd = "./restart_container.sh"
subprocess.call(cmd, shell=True)
