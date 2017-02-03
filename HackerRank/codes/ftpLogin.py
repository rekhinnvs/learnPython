import os
import time
from ftplib import FTP
ftp = FTP('122.181.189.37')
ftp.login('visio-testing','visiotesting')
print("Loging in..")
ftp.cwd('/visio-testing/rekhin')
print(ftp.nlst())
