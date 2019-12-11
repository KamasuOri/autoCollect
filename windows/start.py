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
from tkinter import *
import struct
import socket
import uuid 
import datetime
import shutil

import getLogFile
import networkSetting
import GUI
import getUserFootPrint
import getRamDiskImage


osSize=32

getLoginHistoryCheck = "0"
getProcessTreeCheck ="0"
getNetworkConfigCheck = "0"
getBroswerCacheCheck = "0"
getDiskImageCheck = "0"
getRamImageCheck = "0"
fmhn = "0"

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
	try:
		infile = open("control.txt","r").read().split("-")
		getLoginHistoryCheck = infile[0]
		getProcessTreeCheck = infile[1]
		getNetworkConfigCheck = infile[2]
		fmhn = infile[3]
		getBroswerCacheCheck = infile[4]
		getRamImageCheck = infile[5]
		getDiskImageCheck = infile[6]
	except:
		getLoginHistoryCheck = "0"
		getProcessTreeCheck ="0"
		getNetworkConfigCheck = "0"
		getBroswerCacheCheck = "0"
		getDiskImageCheck = "0"
		getRamImageCheck = "0"
		fmhn = "0"
	



def startCollecter():
	if struct.calcsize("P")*8==64:
		osSize=64	
	currentPath = os.getcwd()
	# print socket.gethostname()
	execCMD('mkdir REPORT')
	
	if "1" in getLoginHistoryCheck:
		try:
			print "-------Get Login History-------"
			logname = getLogFile.getLogFile("User Profile Service","1.csv",currentPath)
			getUserFootPrint.remakeCsvHistoryLogin(logname)
			os.remove(logname)
			print "+++++++ Done Get login history+++++++"
		except:
			print "***** Error while trying to get Login History *****"

	if "1" in getProcessTreeCheck:
		try:
			print "-------Get Process Tree-------"	
			cmd = 'powershell -command "powershell -ExecutionPolicy ByPass -File .\\Tool\\GetProcessTree.ps1"'
			execCMD(cmd)
			print "+++++++ Done Get Process Tree+++++++"
		except:
			print "***** Error while trying to get Process Tree *****"
	if "1" in getNetworkConfigCheck:
		try:
			print "-------Get Nerwork Config-------"	
			networkSetting.getNetworkConfig()
			print "+++++++ Done Get Nerwork Config+++++++"
		except:
			print "***** Error while trying to get Nerwork Config *****"
	if "0" not in fmhn:
		try:
			print "-------Get File Molidate History-------"
			val = int(fmhn)
			getUserFootPrint.getFileMolidateHistory(val)
			print "+++++++ Done Get File Molidate History+++++++"
		except ValueError:
		   	print "***** Error while trying to get Nerwork Config Input Must Be A Number*****"
	if "1" in getBroswerCacheCheck:
		try:
			print "-------Get Broswer Cache-------"	
			getUserFootPrint.getCacheBroswer(currentPath)
			print "+++++++ Done Get Broswer Cache+++++++"
		except:
			print "***** Error while trying to get Broswer Cache *****"
	if "1" in getRamImageCheck:
		try:
			print "-------Get Ram Image-------"	
			getRamDiskImage.getRamImage(osSize)
			print "+++++++ Done Get Ram Image+++++++"
		except:
			print "***** Error while trying to get Ram Image *****"
	if "1" in getDiskImageCheck:
		try:
			print "-------Get Disk Image-------"	
			getRamDiskImage.getDiskImage()
			print "+++++++ Done Get Disk Image+++++++"
		except:
			print "***** Error while trying to get Disk Image *****"

def changeNameReportDir():
	if os.path.exists('REPORT'):
		pcname = os.environ['COMPUTERNAME']
		macAddress =  hex(uuid.getnode())[2:-1]
		macAddress = macAddress[0:2]+"-"+macAddress[2:4]+"-"+macAddress[4:6]+"-"+macAddress[6:8]+"-"+macAddress[8:10]+"-"+macAddress[10:12]
		now = datetime.datetime.now()
		date = str(now.hour)+"-"+str(now.minute)+"-"+str(now.day)+"-"+str(now.month)+"-"+str(now.year)
		os.rename('REPORT', date)
		newDir = pcname+"\\"+macAddress
		cmd = "midir "+newDir
		execCMD(cmd)
		shutil.move(date, newDir+"\\"+date)

readControler()
startCollecter()
changeNameReportDir()

