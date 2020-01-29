#!/usr/bin/python
# -*- coding: utf8 -*-
import zipfile
import sys
import subprocess as sub
import time
import subprocess
from subprocess import call
from threading import Thread
import os
import ctypes
import struct
import socket
import uuid 
import datetime
import shutil
import hashlib 

import getLogFile
import networkSetting
import GUI
import getUserFootPrint
import getRamDiskImage
import readDiskSector

now = datetime.datetime.now()
date = str(now.hour)+"-"+str(now.minute)+"-"+str(now.second)+"-"+str(now.day)+"-"+str(now.month)+"-"+str(now.year)
		
osSize=32

getLoginHistoryCheck = "0"
getProcessTreeCheck ="0"
getNetworkConfigCheck = "0"
getBroswerCacheCheck = "0"
getDiskImageCheck = "0"
getRamImageCheck = "0"
fmhn = "0"
toolReakDiskManualCheck="0"

jobsList=''
def execCMD(command):
    p = sub.Popen(command,shell = True,stdout =sub.PIPE,stderr = sub.STDOUT)
    output,errors = p.communicate()  
    return output

def isAdmin():
    try:
        is_admin = (os.getuid() == 0)
    except AttributeError:
        is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0

	if is_admin:
	    print("Okay let start it !")
	else:
	    print("You must run with admin privilege !!!")
	    raw_input()
	    exit(0)
def readControler():
	global getLoginHistoryCheck
	global getProcessTreeCheck
	global getNetworkConfigCheck
	global fmhn
	global getBroswerCacheCheck
	global getRamImageCheck
	global getDiskImageCheck
	global toolReakDiskManualCheck
	try:
		infile = open("control.txt","r").read().split("-")
		getLoginHistoryCheck = infile[0]
		getProcessTreeCheck = infile[1]
		getNetworkConfigCheck = infile[2]
		fmhn = infile[3]
		getBroswerCacheCheck = infile[4]
		getRamImageCheck = infile[5]
		getDiskImageCheck = infile[6]
		toolReakDiskManualCheck=infile[7]
	except:
		getLoginHistoryCheck = "0"
		getProcessTreeCheck ="0"
		getNetworkConfigCheck = "0"
		getBroswerCacheCheck = "0"
		getDiskImageCheck = "0"
		getRamImageCheck = "0"
		fmhn = "0"
		toolReakDiskManualCheck="0"
	



def startCollecter():
	global jobsList
	if struct.calcsize("P")*8==64:
		osSize=64	
	currentPath = os.getcwd()
	# print socket.gethostname()
	if os.path.exists("REPORT"):
		shutil.rmtree("REPORT")
	execCMD('mkdir REPORT')
	
	if "1" in getLoginHistoryCheck:
		try:
			print "-------Get Login History-------"
			jobsList += "Get Login History||"
			logname = getLogFile.getLogFile("User Profile Service","1.csv",currentPath)
			getUserFootPrint.remakeCsvHistoryLogin(logname)
			os.remove(logname)
			print "+++++++ Done Get login history+++++++"
		except:
			print "***** Error while trying to get Login History *****"

	if "1" in getProcessTreeCheck:
		try:
			print "-------Get Process Tree-------"
			jobsList += "Get Process Tree||"
			cmd = 'powershell -command "powershell -ExecutionPolicy ByPass -File .\\Tool\\GetProcessTree.ps1"'
			execCMD(cmd)
			print "+++++++ Done Get Process Tree+++++++"
		except:
			print "***** Error while trying to get Process Tree *****"
	if "1" in getNetworkConfigCheck:
		try:
			print "-------Get Nerwork Config-------"	
			jobsList += "Get Nerwork Config||"
			networkSetting.getNetworkConfig()
			print "+++++++ Done Get Nerwork Config+++++++"
		except:
			print "***** Error while trying to get Nerwork Config *****"
	if "0" not in fmhn:
		try:
			print "-------Get File Modified  History-------"
			jobsList += "Get File Modified  History||"
			val = int(fmhn)
			getUserFootPrint.getFileMolidateHistory(val)
			print "+++++++ Done Get File Modified  History+++++++"
		except ValueError:
		   	print "***** Error while trying to get Nerwork Config Input Must Be A Number*****"
	if "1" in getBroswerCacheCheck:
		try:
			print "-------Get Broswer Cache-------"	
			jobsList += "Get Broswer Cache||"
			getUserFootPrint.getCacheBroswer(currentPath)
			print "+++++++ Done Get Broswer Cache+++++++"
		except:
			print "***** Error while trying to get Broswer Cache *****"
	if "1" in getRamImageCheck:
		try:
			print "-------Get Ram Image-------"	
			jobsList += "Get Ram Image||"
			getRamDiskImage.getRamImage(osSize)
			print "+++++++ Done Get Ram Image+++++++"
		except:
			print "***** Error while trying to get Ram Image *****"
	if "1" in getDiskImageCheck:
		try:
			print "-------Get Disk Image-------"
			jobsList += "Get Disk Image||"	
			getRamDiskImage.getDiskImage()
			print "+++++++ Done Get Disk Image+++++++"
		except:
			print "***** Error while trying to get Disk Image *****"
	if "0" not in toolReakDiskManualCheck:
		try:
			print "-------toolReakDiskManualCheck-------"
			jobsList += "toolReakDiskManualCheck||"	
			readDiskSector.start(toolReakDiskManualCheck)
			print "+++++++ Done toolReakDiskManualCheck+++++++"
		except:
			print "***** Error while trying to toolReakDiskManualCheck *****"

def zipDir(sample):
	if os.path.exists(sample):
		src = os.path.realpath(sample)
	root_dir,tail = os.path.split(src)
	shutil.make_archive(sample,"zip",root_dir+"\\"+sample)

def md5File(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

def getPCInfoAndChangeFileName():
	PCreport = jobsList + "\n+--------+\n"
	PCInfo = PCreport
	PCInfo += date
	PCInfo += "\n+--------+\n"

	PCInfo += os.environ['COMPUTERNAME']
	PCInfo += "\n+--------+\n"

	cmd = "Tool\\dmidecode.exe -s system-uuid"
	PCInfo += execCMD(cmd).replace("\n","")
	PCInfo += "\n+--------+\n"

	cmd = "Tool\\dmidecode.exe -s Processor-Version System-UUID"
	PCInfo += execCMD(cmd).replace("\n","")
	PCInfo += "\n+--------+\n"

	macAddress=''
	ipconfig =  execCMD("ipconfig /all").split("\n")
	for a in ipconfig:
		if "Physical Address" in a:
			macAddress+=a.replace("Physical Address. . . . . . . . . :","")+"\n"
	PCInfo+=macAddress[:-1]
	PCInfo += "\n+--------+\n"

	
	result = hashlib.md5(PCInfo.encode())
	hashData = result.hexdigest()
	zipDir("REPORT")

	PCInfo+=md5File("REPORT.zip")
	PCInfo += "\n+--------+\n"

	f = open("pcInfo.txt","w")
	f.write(PCInfo)
	f.close()

	cmd = "mkdir report-"+hashData
	execCMD(cmd)
	shutil.move("REPORT.zip","report-"+hashData)
	shutil.move("pcInfo.txt","report-"+hashData)
	shutil.rmtree("REPORT")

# getPCInfoAndChangeFileName()

readControler()
startCollecter()
getPCInfoAndChangeFileName()
