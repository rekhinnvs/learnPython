import os
import time
from ftplib import FTP
dirPath = "/home/jyoti/Azmat/Bennu_Data_Stability/DATASTABILITY_Scripts/DATASTABILITY_Scripts/Downloaded"
ftp = FTP('125.63.77.147')
while True:
	fileList = os.listdir(dirPath)
	for fileName in fileList:
		os.remove(dirPath+"/"+fileName)
	print("You create I ll delete!")
	time.sleep(10800)
ftp.login('borqs1','S@(!M@BOr1')
ftp.cwd('/Vizio/Upload')

