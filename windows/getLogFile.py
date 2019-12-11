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
import log
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
		execCMD('mkdir REPORT\\tmpFile')
		listLog = execCMD("c: & dir %SystemRoot%\\System32\\Winevt\\Logs").split('\n')
		logLogin=''
		for a in listLog:
			if nameLog in a:
				logLogin=a.split('Microso')
		logLoginName = 'Microso'+logLogin[len(logLogin)-1][:-1]
		cmd = 'c: & cd %SystemRoot%\\System32\\Winevt\\Logs &' +'copy "'  +logLoginName + '" ' + workPath
		execCMD(cmd)
		os.rename(logLoginName, 'loginLog.evtx')
		cmd = 'powershell -command "Get-WinEvent -Path loginLog.evtx | Export-CSV ' + savename + '"'
		print execCMD(cmd)
		execCMD('move loginLog.evtx REPORT\\tmpFile')
	except:
		log.log(2,"fail when getLogFile")
	return savename
