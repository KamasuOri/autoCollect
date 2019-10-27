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
    p = sub.Popen(command,shell = True,stdout =sub.PIPE,stderr = sub.STDOUT)
    output,errors = p.communicate()  
    return output

def getDriveList():
	cmd = "wmic logicaldisk get name"
	tmp=''
	arrayDrive=['']
	for word in execCMD(cmd):	
		if ":" in word:
			if tmp != "c" and tmp != "C":
				arrayDrive.append(tmp)
		tmp = word
	del arrayDrive[0]
	return arrayDrive
print getDriveList()