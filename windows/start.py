# -*- Coding: utf8 -*-
import zipfile
import sys
import subprocess as sub
import time
import subprocess
from subprocess import call
from threading import Thread
import os
import ctypes
 
import userHistoryLogin
import getLogFile
import networkSetting
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

def startCollect():
	currentPath = os.getcwd()
	execCMD('mkdir REPORT')
	
	try:
		print "-------Get Login History-------"
		logname = getLogFile.getLogFile("User Profile Service","1.csv",currentPath)
		userHistoryLogin.remakeCsvHistoryLogin(logname)
		os.remove(logname)
		print "+++++++ Done Get login history+++++++"
	except:
		print "***** Error while trying to get Login History *****"
	
	try:
		print "-------Get Process Tree-------"	
		cmd = 'powershell -command "powershell -ExecutionPolicy ByPass -File .\\Tool\\GetProcessTree.ps1"'
		execCMD(cmd)
		print "+++++++ Done Get Process Tree+++++++"
	except:
		print "***** Error while trying to get Process Tree *****"

	
	try:
		print "-------Get Nerwork Config-------"	
		networkSetting.getNetworkConfig()
		print "+++++++ Done Get Process Tree+++++++"
	except:
		print "***** Error while trying to get Nerwork Config *****"

isAdmin()
startCollect()
# currentPath = os.getcwd()
# getLogFile.getLogFile("Windows-PowerShell","1.csv",currentPath)