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
def execCMD(command):
	try:
	    p = sub.Popen(command,shell = True,stdout =sub.PIPE,stderr = sub.STDOUT)
	    output,errors = p.communicate()  
	except:
		print "fail when execCMD :"+command
	return output

'''
laasy file .evtx taji thuw mujc cura windows event theo nameLog va convert sang .csv
'''
# get login log file
def getLogFile(nameLog,savename,workPath):
	try:
		listLog = execCMD("dir %SystemRoot%\\System32\\Winevt\\Logs").split('\n')
		logLogin=''
		for a in listLog:
			if nameLog in a:
				logLogin=a.split('Microso')
		logLoginName = 'Microso'+logLogin[len(logLogin)-1][:-1]
		cmd = 'cd %SystemRoot%\\System32\\Winevt\\Logs &' +'copy "'  +logLoginName + '" ' + workPath
		execCMD(cmd)
		os.rename(logLoginName, '123.evtx')
		cmd = 'powershell -command "Get-WinEvent -Path 123.evtx | Export-CSV ' + savename + '"'
		print execCMD(cmd)
		# os.remove('123.evtx')
	except:
		print "fail when getLogFile"
	return savename