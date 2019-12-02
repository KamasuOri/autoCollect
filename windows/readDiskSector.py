import os
import sys
import wmi
import numpy as np
from struct import *
workDrive=0
SECTOR_SIZE = 512
ENTRY_SIZE= 0x80

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

def getDataOfEntry():
	count=1
	try:
		drive1 = "\\\\.\\"+workDrive[:-1]
		print drive1
		drive = open(drive1,"rb")
		print "1"
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
			print retData[count][0],"  ",retData[count][1],"  ",retData[count][2]
			drive.read(ENTRY_SIZE-0x30)
			count +=1
		drive.close()
	except:
		print "Fail in getNumberOfEntry"
		exit()
	return retData
def readSectors(entryData,start_sector,sectors_to_read):
	drive = open("\\\\.\\PhysicalDrive1","rb")
	drive.seek(SECTOR_SIZE*(entryData[0]+start_sector))
	ret = open("ret","wb")
	ret.write(drive.read(sectors_to_read*SECTOR_SIZE))
	ret.close()
	drive.close()

# entryData = getDataOfEntry("PhysicalDrive1")
# readSectors(entryData[4],2,2)
def start():
	count = getNumberOfPhysicalDrive()
	workDrive = raw_input("Input your PhysicalDrive you want to read:")
	workDrive="PhysicalDrive"+workDrive
	print workDrive
	entryData = getDataOfEntry()
# getDataOfEntry()
start()