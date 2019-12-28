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
 
def execCMD(command):
    p = sub.Popen(command,shell = True,stdout =sub.PIPE,stderr = sub.STDOUT)
    output,errors = p.communicate()  
    return output

def getNetworkConfig():
	f = open("REPORT\\networkConfig.txt","w")
	f.write("Ip and port \n")
	f.write(execCMD("ipconfig /all"))
	f.write("\n--------------------------------------\n")
	f.write("Route table \n")
	f.write(execCMD("route print"))
	f.write("\n--------------------------------------\n")
	f.close()