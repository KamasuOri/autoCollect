#!/usr/bin/python
# -*- coding: utf8 -*-
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

#////////////////////////// option 1 //////////////////////

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


def getDataOfEntryOfOldDiskType(physicalNum):
	global workDrive
	count=1
	try:	
		drive = open("\\\\.\\PhysicalDrive"+physicalNum,"rb")
		drive.seek(2*SECTOR_SIZE)
		retData = np.zeros((100,3))
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
		retData[0][0]=count-1
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

def readSectors(physicalNum,entryData,start_sector,sectors_to_read): #ByPhysicalDrive
	try:
		drive = open("\\\\.\\PhysicalDrive"+physicalNum,"rb")
		print "1"
		drive.seek(SECTOR_SIZE*(entryData[0]+start_sector))
		print "2"

		# listDriveStoreable = getDriveStoreable(sectors_to_read*512)
		# inOrNot=0
		currentPath=os.getcwd()
		# currentDrive = os.getcwd()[0:1]
		# if len(listDriveStoreable) == 0:
		# 	GUI.messageBox("Disk problem","11111")
		# 	log.log(2,"get ramImage")
		# 	return 0
			
		# for a in listDriveStoreable:
		# 	if currentDrive.lower() in a.lower():
		# 		inOrNot=1

		# if inOrNot == 0:
		# 	GUI.messageBox("Disk problem","You will find REPORT in "+listDriveStoreable[0]+" drive cause current drive not enough to store !")
		# 	currentPath = listDriveStoreable[0]
		execCMD('mkdir '+currentPath+'\\REPORT\\splitDiskImake')
		ret = open(currentPath+'\\REPORT\\splitDiskImake\\'+"ret","ab")
		for i in range (sectors_to_read):
			ret.write(drive.read(SECTOR_SIZE))
		ret.close()
		drive.close()
	except:
		print "fail in readSectors !"

def getDataOfEntryOfNewDiskType(physicalNum):

	count=1
		
	drive = open("\\\\.\\PhysicalDrive"+physicalNum,"rb")
	drive.read(0x1be)
	retData = np.zeros((100,3))	#start at 1
									
	for i in range (4):
		if drive.read(8) != "\x00\x00\x00\x00\x00\x00\x00\x00":

			firstSector = drive.read(4)
			firstSector = int(unpack("<I",firstSector)[0])
			totalSector = drive.read(4)
			totalSector = int(unpack("<I",totalSector)[0])
			retData[count][0]=firstSector
			retData[count][1]=totalSector
			retData[count][2]=((totalSector)*512)*10**(-9)
			count +=1
	retData[0][0]=count-1		# count saver
	drive.close()
	return retData
def startReadByPhysicalDrive():
	count = getNumberOfPhysicalDrive()
	physicalNum = raw_input("Input the PhysicalDrive you want to read:")
	entryData = getDataOfEntryOfNewDiskType(physicalNum)
	print "PhysicalDrive",physicalNum," have ",int(entryData[0][0])," entry!"
	for i in range(1,int(entryData[0][0])+1):
		print i,": size = ",entryData[i][2]," GB, have ",int(entryData[i][1])," sector."
	entryRead = int(raw_input("Input the Entry you want to read:"))
	start_sector = int(raw_input("Input the Sector you want to start:"))
	sectors_to_read = int(raw_input("Input the number of Sectors you want to read:"))
	readSectors(physicalNum,entryData[entryRead],start_sector,sectors_to_read)


#////////////////////////// option 2 //////////////////////

def getDeviceIDAndSector():
	c = wmi.WMI ()
	c.Win32_OperatingSystem()[0].Caption
	c.Win32_LogicalDisk()[0]
	ret = ['']
	count=0
	for a in c.Win32_LogicalDisk():
		ret.append(a.DeviceID)
		print a.DeviceID,"     ",str(int(a.Size)/512)
	return ret
def getSectorOfDeviceID(DeviceID):
	c = wmi.WMI ()
	c.Win32_OperatingSystem()[0].Caption
	c.Win32_LogicalDisk()[0]
	for a in c.Win32_LogicalDisk():
		if DeviceID.upper() in a.DeviceID:
			return int(a.Size)/512
	return 0
def readSectorsByDeviceID(physicalNum,start_sector,sectors_to_read):
	try:
		drive = open("\\\\.\\"+physicalNum,"rb")
		drive.seek(SECTOR_SIZE*(start_sector))
		currentPath=os.getcwd()
		execCMD('mkdir '+currentPath+'\\REPORT\\splitDiskImake')
		ret = open(currentPath+'\\REPORT\\splitDiskImake\\'+"ret","ab")
		for i in range (sectors_to_read):
			ret.write(drive.read(SECTOR_SIZE))
		ret.close()
		drive.close()
	except:
		print "fail in readSectors !"

def startReadByDeviceID():
	print "Device   Total Sector"
	device = getDeviceIDAndSector()
	deviceinput = raw_input("Input device tou want to read:").replace("\n","")
	checkin=0
	for a in device:
		if deviceinput.upper() in a:
			checkin =1
			break
	if checkin ==0:
		return 0
	totalSector = getSectorOfDeviceID(deviceinput)
	start_sector = int(raw_input("Input the Sector you want to start:"))
	sectors_to_read = int(raw_input("Input the number of Sectors you want to read:"))
	if int(totalSector) < int(start_sector) or int(totalSector) < int(sectors_to_read) or (int(sectors_to_read) + int(start_sector))>int(totalSector):
		print "fail"
		return 0
	readSectorsByDeviceID(deviceinput+":",start_sector,sectors_to_read)
def start(option="1"):		# option = 1 -> read by PhysicalDrive
						# option = 2 -> read by DeviceID
	print "1111111"
	if option == "1":
		startReadByPhysicalDrive()
	if option == "2":
		startReadByDeviceID()

