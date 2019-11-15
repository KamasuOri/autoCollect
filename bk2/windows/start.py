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
from tkinter import *
import struct
import socket


import getLogFile
import networkSetting
import GUI
import getUserFootPrint
import getRamDiskImage

osSize=32

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
	if struct.calcsize("P")*8==64:
		osSize=64
	print osSize
	currentPath = os.getcwd()
	print socket.gethostname()
	execCMD('mkdir REPORT')
	
	if getLoginHistoryCheck.get():
		try:
			print "-------Get Login History-------"
			logname = getLogFile.getLogFile("User Profile Service","1.csv",currentPath)
			getUserFootPrint.remakeCsvHistoryLogin(logname)
			os.remove(logname)
			print "+++++++ Done Get login history+++++++"
		except:
			print "***** Error while trying to get Login History *****"

	if getProcessTreeCheck.get():
		try:
			print "-------Get Process Tree-------"	
			cmd = 'powershell -command "powershell -ExecutionPolicy ByPass -File .\\Tool\\GetProcessTree.ps1"'
			execCMD(cmd)
			print "+++++++ Done Get Process Tree+++++++"
		except:
			print "***** Error while trying to get Process Tree *****"
	if getNetworkConfigCheck.get():
		try:
			print "-------Get Nerwork Config-------"	
			networkSetting.getNetworkConfig()
			print "+++++++ Done Get Nerwork Config+++++++"
		except:
			print "***** Error while trying to get Nerwork Config *****"
	if fmhn.get():
		try:
			print "-------Get File Molidate History-------"
			val = int(fmhn.get())
			getUserFootPrint.getFileMolidateHistory(val)
			print "+++++++ Done Get File Molidate History+++++++"
		except ValueError:
		   	print "***** Error while trying to get Nerwork Config Input Must Be A Number*****"
	if getBroswerCacheCheck.get():
		try:
			print "-------Get Broswer Cache-------"	
			getUserFootPrint.getCacheBroswer(currentPath)
			print "+++++++ Done Get Broswer Cache+++++++"
		except:
			print "***** Error while trying to get Broswer Cache *****"
	master.quit()

isAdmin()

master = Tk()
getLoginHistoryCheck = IntVar()
getProcessTreeCheck = IntVar()
getNetworkConfigCheck = IntVar()
getBroswerCacheCheck = IntVar()

Label(master, text="Choose option").grid(row=0, sticky=W)
Checkbutton(master, text="Login History", variable=getLoginHistoryCheck).grid(row=1, sticky=W)
Checkbutton(master, text="Process Tree", variable=getProcessTreeCheck).grid(row=2, sticky=W)
Checkbutton(master, text="Network Config", variable=getNetworkConfigCheck).grid(row=4, sticky=W)
fmhn = Entry(master)
fmhn.grid(row=5, column=1)
Label(master, text="File Molidate History (input day)").grid(row=5)
Checkbutton(master, text="Brower Cache", variable=getBroswerCacheCheck).grid(row=6, sticky=W)
Button(master, text='Run check', command=startCollect).grid(row=7, sticky=W, pady=10)
mainloop()




# startCollect()

