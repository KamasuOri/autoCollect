import csv
import pandas as pd
import zipfile
import sys
import subprocess as sub
import time
import subprocess
from subprocess import call
from threading import Thread
import wmi

import os
import log
import GUI

def execCMD(command):
    p = sub.Popen(command,shell = True,stdout =sub.PIPE,stderr = sub.STDOUT)
    output,errors = p.communicate()  
    return output


def getDriveStoreable(checkRamOrDisk):
	enoughMem2SaveDisk=0
	c = wmi.WMI ()
	c.Win32_OperatingSystem()[0].Caption
	c.Win32_LogicalDisk()[0]
	ret = ['']

	ramSize =  long(c.Win32_ComputerSystem()[0].TotalPhysicalMemory)+10/(9.31*10**-10)
	cDriveSize = long(c.Win32_LogicalDisk()[0].Size) - long(c.Win32_LogicalDisk()[0].Freespace)+10/(9.31*10**-10)

	if "ram" in checkRamOrDisk:
		totalSizeRequest = ramSize
	else:
		totalSizeRequest=cDriveSize

	for a in c.Win32_LogicalDisk():
		if (long(a.size)-long(a.Freespace) ) > totalSizeRequest:
			ret.append(a.DeviceID)
	for a in ret:
		if len(a)==0:
			ret.remove(a)
	return ret

def getRamImage(osSize):
	listDriveStoreable = getDriveStoreable("ram")
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

	try:
		execCMD('mkdir '+currentPath+'\\REPORT\\ramDiskImage\\ramImage')
		path=''
		if osSize == 32:
			path = "Tool\\ramCapture\\x86\\RamCapture86.exe"
		else:
			path = "Tool\\ramCapture\\x64\\RamCapture64.exe"
		cmd = path+" "+currentPath+"\\REPORT\\ramDiskImage\\ramImage\\ramImage.mem"
		print cmd
		execCMD(cmd)
		log.log(1,"get ramImage")
	except:
		log.log(2,"get ramImage")

def getDiskImage():
	listDriveStoreable = getDriveStoreable("disk")
	inOrNot=0
	currentPath=os.getcwd()
	currentDrive = os.getcwd()[0:1]

	if len(listDriveStoreable) == 0:
		GUI.messageBox("Disk problem","11111")
		log.log(2,"get diskImage")
		return 0
		
	for a in listDriveStoreable:
		if currentDrive.lower() in a.lower():
			inOrNot=1

	if inOrNot == 0:
		GUI.messageBox("Disk problem","You will find REPORT in "+listDriveStoreable[0]+" drive cause current drive not enough to store !")
		currentPath = listDriveStoreable[0]
	try:
		execCMD('mkdir '+currentPath+'\\REPORT\\ramDiskImage\\diskImage')
		cmd = "Tool\\disk2vhd.exe c: "+currentPath+'\\REPORT\\ramDiskImage\\diskImage\\diskImage.vhd'
		execCMD(cmd)
		log.log(1,"get diskImage")
	except:
		log.log(2,"get diskImage")

