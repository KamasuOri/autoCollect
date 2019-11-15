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

def getRamImage(osSize):
	try:
		execCMD('mkdir REPORT\\ramDiskImage\\ramImage')
		path=''
		if osSize == 32:
			path = "Tool\\ramCapture\\x86\\RamCapture86.exe"
		else:
			path = "Tool\\ramCapture\\x64\\RamCapture64.exe"
		cmd = path+" REPORT\\ramDiskImage\\ramImage\\ramImage.mem"
		print cmd
		execCMD(cmd)
		log.log(1,"get ramDisk")
	except:
		log.log(2,"get ramDisk")
