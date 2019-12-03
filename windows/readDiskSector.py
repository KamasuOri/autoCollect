import os
import wmi
import numpy as np
import sys
import subprocess as sub
import subprocess
from subprocess import call
from threading import Thread

import log
import GUI

from struct import *

SECTOR_SIZE = 512
ENTRY_SIZE= 0x80

def execCMD(command):
    p = sub.Popen(command,shell = True,stdout =sub.PIPE,stderr = sub.STDOUT)
    output,errors = p.communicate()  
    return output

def getNumberOfPhysicalDrive():
	count =0
	c = wmi.WMI()
	while count >=0:
		try:
			[drive] = c.Win32_DiskDrive(Index=count)
			print str(count),": PhysicalDrive"+str(count)+" have %s GB" % int(int(drive.size) / 1024**3)				#start at 0
			count +=1
		except:
			break
	return count-1

def getDataOfEntry(physicalNum):
	global workDrive
	count=1
	try:	
		drive = open("\\\\.\\PhysicalDrive"+physicalNum,"rb")
		drive.seek(2*SECTOR_SIZE)
		retData = np.zeros((100,3))									#start at 1
		while drive.read(5) != "\x00\x00\x00\x00\x00":
			drive.read(0x20-5)
			firstLBA = drive.read(8)
			firstLBA = int(unpack("<q",firstLBA)[0])
			lastLBA = drive.read(8)
			lastLBA = int(unpack("<q",lastLBA)[0])

			retData[count][0]=firstLBA
			retData[count][1]=lastLBA
			retData[count][2]=((lastLBA-firstLBA)*512)*10**(-9)
			drive.read(ENTRY_SIZE-0x30)
			count +=1
		retData[0][0]=count-1		# count saver
		drive.close()
	except:
		print "Fail in getNumberOfEntry"
		exit()
	return retData

def getDriveStoreable(totalSizeRequest):
	enoughMem2SaveDisk=0
	c = wmi.WMI ()
	c.Win32_OperatingSystem()[0].Caption
	c.Win32_LogicalDisk()[0]
	ret = ['']
	for a in c.Win32_LogicalDisk():
		# if (long(a.size)-long(a.Freespace) ) > totalSizeRequest:
		if (long(a.Freespace) ) > totalSizeRequest:
			print a.Freespace,"     ",totalSizeRequest
			ret.append(a.DeviceID)
	for a in ret:
		if len(a)==0:
			ret.remove(a)
	return ret

def readSectors(physicalNum,entryData,start_sector,sectors_to_read):
	try:
		drive = open("\\\\.\\PhysicalDrive"+physicalNum,"rb")
		drive.seek(SECTOR_SIZE*(entryData[0]+start_sector))
		

		listDriveStoreable = getDriveStoreable(sectors_to_read*512)
		inOrNot=0
		currentPath=os.getcwd()
		currentDrive = os.getcwd()[0:1]
		if len(listDriveStoreable) == 0:
			GUI.messageBox("Disk problem","11111")
			log.log(2,"get ramImage")
			return 0
			
		for a in listDriveStoreable:
			if currentDrive.lower() in a.lower():
				inOrNot=1

		if inOrNot == 0:
			GUI.messageBox("Disk problem","You will find REPORT in "+listDriveStoreable[0]+" drive cause current drive not enough to store !")
			currentPath = listDriveStoreable[0]
		execCMD('mkdir '+currentPath+'\\REPORT\\splitDiskImake')
		ret = open(currentPath+'\\REPORT\\splitDiskImake\\'+"ret","ab")
		for i in range (sectors_to_read):
			ret.write(drive.read(SECTOR_SIZE))
		ret.close()
		drive.close()
	except:
		print "fail in readSectors !"

def start():
	count = getNumberOfPhysicalDrive()
	physicalNum = raw_input("Input the PhysicalDrive you want to read:")
	entryData = getDataOfEntry(physicalNum)
	print "PhysicalDrive",physicalNum," have ",int(entryData[0][0])," entry!"
	for i in range(1,int(entryData[0][0])+1):
		print i,": size = ",entryData[i][2]," GB, have ",int(entryData[i][1]-entryData[i][0])," sector."
	entryRead = int(raw_input("Input the Entry you want to read:"))
	start_sector = int(raw_input("Input the Sector you want to start:"))
	sectors_to_read = int(raw_input("Input the number of Sectors you want to read:"))
	readSectors(physicalNum,entryData[entryRead],start_sector,sectors_to_read)

start()
