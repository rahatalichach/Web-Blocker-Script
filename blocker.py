import datetime
import time

block_time = datetime.datetime(2024, 1, 3)
site_block = ["www.wscubetech.com", "www.booking.com"]
path = "C:/Windows/System32/drivers/etc/hosts"
redirect = "127.0.0.1"

while datetime.datetime.now() < block_time:
    print("Start blocking")
    with open(path, "r+") as host_file:
        content = host_file.read()
        for website in site_block:
            if website not in content:
                host_file.write(redirect + " " + website + "\n")

while True:
    with open(path, "r+") as host_file:
        lines = host_file.readlines()
        host_file.seek(0)
        for line in lines:
            if not any(website in line for website in site_block):
                host_file.write(line)
        host_file.truncate()

    time.sleep(5)