import csv
import pandas as pd
import zipfile
import sys
import subprocess as sub
import time
import subprocess
from subprocess import call
from threading import Thread
import os
import log

def execCMD(command):
    p = sub.Popen(command,shell = True,stdout =sub.PIPE,stderr = sub.STDOUT)
    output,errors = p.communicate()  
    return output

def getLogicalDisk():

	'''
	xample return ['D:\\', 'E:\\', 'F:\\']
	'''

	cmd = "wmic logicaldisk get name"
	ret = execCMD(cmd).split('\n')
	retLogicalDisk=[]
	for a in ret:
		if 'Name' not in a and 'C:' not in a:
			a=a.replace(' ','')
			a=a.replace('\r','')
			if len(a)>0:
				a=a+'\\'
				retLogicalDisk.append(a)
	return retLogicalDisk

def getFileMolidateHistory(day):
	try:
		hours = day *24
		execCMD('mkdir REPORT\\molidateFileHistory')
		execCMD('mkdir REPORT')
		listDisk = getLogicalDisk()
		for disk in listDisk:
			psCMD = "Get-ChildItem -Path " + disk +" -Recurse | Where-Object -FilterScript { $_.LastWriteTime -ge (Get-Date).AddHours(-" + str(hours) +") }"
			cmd = "powershell -command " + '"'+psCMD+'"' +"> REPORT\\molidateFileHistory\\"+disk[:-2]+".history.in"+str(day)+".day.txt"
			execCMD(cmd)
		disk = "%userprofile%"
		psCMD = "Get-ChildItem -Path " + disk +" -Recurse | Where-Object -FilterScript { $_.LastWriteTime -ge (Get-Date).AddHours(-" + str(hours) +") }"
		cmd = "powershell -command " + '"'+psCMD+'"' +"> REPORT\\molidateFileHistory\\USER.history.in"+str(day)+".day.txt"
		execCMD(cmd)
		log.log(1,"getFileHistory")
	except:
		log.log(2,"getFileHistory")

def getCacheBroswer():
	execCMD('mkdir REPORT\\CacheBroswer')
	execCMD('mkdir REPORT\\CacheBroswer\\Chrome')
	execCMD('mkdir REPORT\\CacheBroswer\\CocCoc')
	execCMD('mkdir REPORT\\CacheBroswer\\FireFox')
	execCMD('mkdir REPORT\\CacheBroswer\\IE')
	cmd = 'copy "%USERPROFILE%\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\Cache" REPORT\\CacheBroswer\\Chrome'
	execCMD(cmd)

	cmd = 'copy "%USERPROFILE%\\AppData\\Local\\CocCoc\\Browser\\User Data\\Default\\Cache" REPORT\\CacheBroswer\\CocCoc'
	execCMD(cmd)

	cmd = 'copy "%USERPROFILE%\\AppData\\Local\\Mozilla\\Firefox\\Profiles" REPORT\\CacheBroswer\\FireFox'
	execCMD(cmd)

	cmd = 'copy "%localappdata%\\Microsoft\\Windows\\INetCache\\IE" REPORT\\CacheBroswer\\IE'
	execCMD(cmd)