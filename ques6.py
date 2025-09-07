from ftplib import FTP
import os
import time
import csv
import logging
from datetime import datetime


log_local_path = "C:/Users/ashutrai/OneDrive - Cisco/Desktop/programs/Projects/logs/ques6/"
log_file = "ftp_upload.log"
logging.basicConfig(
    filename= log_local_path+log_file,
    filemode="w",
    level=logging.INFO,
    format="%(levelname)s: %(message)s"
)

summary_local_path = log_local_path
summary_file_name = "upload_summary.csv"
summary_file_path = summary_local_path+summary_file_name
with open(summary_file_path,"w",newline="") as sobj:
    writer=csv.writer(sobj)
    header = ["filename", "size_bytes", "status", "remote_path", "duration_s", "notes"]
    writer.writerow(header)


class FTPOperations:
    def __init__(self,host,user,password):
        self.host=host
        self.user=user
        self.password=password
        self.start = time.monotonic()
    def connect(self):
        try:
            self.ftp = FTP(self.host,timeout=30)
            self.ftp.login(self.user,self.password)
            logging.info(f"{datetime.now()} : Connection Attempt - Login Success")
        except Exception as exp:
            print("Exception Occured : ",exp)
            logging.info(f"{datetime.now()} : Connection Attempt - Login Failure")

    def putFiles(self):
            total = 0
            uploaded = 0
            skipped = 0
            errors = 0
            remote_directory = "/ashutosh/"
            try:
                self.ftp.cwd(remote_directory)
            except Exception:
                self.ftp.mkd(remote_directory)
                self.ftp.cwd(remote_directory)

            for files in os.listdir('.'):
                start = time.monotonic()
                total += 1
                if files.endswith('.txt'):
                    logging.info(f"{datetime.now()} : {files} Selected")
                    try:
                        with open(files, "rb") as file:
                            self.ftp.storbinary(f"STOR {files}", file)
                        uploaded += 1
                        uploaded_duration = time.monotonic ()- start
                        logging.info(f"{datetime.now()} : Uploaded {files}, Size - {os.path.getsize(files)}, Duration - {uploaded_duration}s")
                        with open(summary_file_path,"a",newline="") as sobj:
                            writer=csv.writer(sobj)
                            data=[files,os.path.getsize(files),"UPLOADED",self.host+remote_directory+files,uploaded_duration,"NA"]
                            writer.writerow(data)
                    except Exception as exp:
                        logging.info(f"{datetime.now()} : {files} Upload Failed Error : {exp}")
                        print("Exception Occured : ",exp)
                        errors += 1
                        error_duration = time.monotonic()-start
                        with open(summary_file_path,"a",newline="") as sobj:
                            writer=csv.writer(sobj)
                            data=[files,os.path.getsize(files),"ERROR","",error_duration,"NA"]
                            writer.writerow(data)
                        continue
                else:
                    skipped += 1
                    skipped_duration = time.monotonic()-start
                    logging.info(f"{datetime.now()} : {files} Skipped because not text file")
                    with open(summary_file_path,"a",newline="") as sobj:
                        writer=csv.writer(sobj)
                        data=[files,os.path.getsize(files),"SKIPPED","",skipped_duration,"NA"]
                        writer.writerow(data)
            self.duration = time.monotonic() - self.start
            logging.info(f"{datetime.now()} : Total files found - {total}, Uploaded - {uploaded}, Skipped - {skipped}, Errors - {errors}, Total time - {self.duration}")
            print(f"Total files found - {total}, Uploaded - {uploaded}, Skipped - {skipped}, Errors - {errors}, Total time - {self.duration}")



logging.info(f"{datetime.now()} : Program Started")
host = "ftp.dlptest.com"
user = "dlpuser"
password = "rNrKYTX9g7z3RgJRmxWuGHbeu"
ftp1 = FTPOperations(host,user,password)
ftp1.connect()
ftp1.putFiles()
logging.info(f"{datetime.now()} : Program Ended")