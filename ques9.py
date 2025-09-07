import requests
import os
import csv
import time
import sys
import logging
from datetime import datetime

log_local_path = "C:/Users/ashutrai/OneDrive - Cisco/Desktop/programs/Projects/logs/"
log_file = "download.log"
logging.basicConfig(
    filename= log_local_path+log_file,
    filemode="w",
    level=logging.INFO,
    format="%(levelname)s: %(message)s"
)
logging.info(f"{datetime.now()} : Program Started")

summary_local_path = "C:/Users/ashutrai/OneDrive - Cisco/Desktop/programs/Projects/"
summary_file_name = "summary.csv"
summary_file_path = summary_local_path+summary_file_name
with open(summary_file_path,"w",newline="") as sobj:
    writer=csv.writer(sobj)
    header = ["url", "status", "saved_as", "size_bytes", "duration_s", "error"]
    writer.writerow(header)

Total = 0
Downloaded = 0
Failed = 0

with open("urls9.txt","r") as url_obj:
    for line in url_obj:
        Total += 1
        stripped_line=line.strip()
        if stripped_line.startswith("#"):
            continue
        else:
            try:
                hostname=stripped_line
                logging.info(f"{datetime.now()} : URL - {hostname} Started")
                response=requests.get(hostname,timeout=30)
                start = time.monotonic()
                if response.status_code == 200:
                    file_name = hostname.split('/')[-1]
                    local_path = "C:/Users/ashutrai/OneDrive - Cisco/Desktop/programs/Projects/downloads/"
                    file_path = local_path+file_name
                    print(file_path) # for understanding which file is currently getting written
                    size=len(response.content)/512  # 64 bit * 8 bit
                    if os.path.exists(file_path):
                        with open(file_path,"ab") as fobj:
                            fobj.write(response.content)
                        duration = time.monotonic() - start
                    else:
                        with open(file_path,"wb") as fobj:
                              fobj.write(response.content)
                        duration = time.monotonic() - start

                    with open(summary_file_path,"a",newline="") as sobj:
                        writer=csv.writer(sobj)
                        data=[hostname,response.status_code,file_name,size,duration,"NA"]
                        writer.writerow(data)
                    Downloaded += 1
                    logging.info(f"{datetime.now()} : Status - {response.status_code}, {size} bytes, Duration - {duration}s")

                elif response.status_code != 200:
                    duration = time.monotonic() - start
                    with open(summary_file_path,"a",newline="") as sobj:
                        writer=csv.writer(sobj)
                        data=[hostname,response.status_code,"","",duration,"Failed"]
                        writer.writerow(data)
                    Failed += 1
                    logging.info(f"{datetime.now()} : Status - {response.status_code}, Duration - {duration}s, Failed")
                logging.info(f"{datetime.now()} : URL - {hostname} Finished")

            except Exception as err:
                print("Exception Occured : ",err)
                Failed += 1
                logging.info(f"{datetime.now()} : Exception Occured - {err}")
                

    print(f"Total: {Total} | Downloaded: {Downloaded} | Failed: {Failed} | Output: {local_path} | Summary: {summary_file_path} | Log: logs/download.log")


logging.info(f"{datetime.now()} : Program Ended")
sys.exit(0 if Failed == 0 else 1)