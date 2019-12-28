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
import hashlib 
from pathlib import Path

def execCMD(command):
    p = sub.Popen(command,shell = True,stdout =sub.PIPE,stderr = sub.STDOUT)
    output,errors = p.communicate()  
    return output

def zipDir(sample):
	print sample
	if os.path.exists(sample):
		src = os.path.realpath(sample)
	root_dir,tail = os.path.split(src)
	shutil.make_archive(sample,"zip",sample)

def startUpdate(dirPath,DBPath):
	listDir = os.listdir(dirPath)
	for a in listDir:
		if len(a)>30 and "report-"	in a:
			updateDataFormReportDir(dirPath+"\\"+a+"\\")
			tmp = dirPath+"\\"+a
			shutil.move(tmp.replace('\\','\\\\')+".zip",DBPath)
def updateDataFormReportDir(dirPath):
	tmpData =[]
	reportData = open(dirPath+"pcInfo.txt","r").read().split("+--------+")
	# print reportData
	for a in reportData:
		if (len(a)>2):
			tmpData.append(a.replace("\n","").replace("\r","").strip().replace("    ","||"))
	print tmpData    # data của log file. xử lý sau.=========================================================================================
	zipDir(dirPath[:-1].replace('\\','\\\\'))
	shutil.rmtree(dirPath[:-1].replace('\\','\\\\'))
def start():
	file = open("path.txt","r").read().split("\n")
	startUpdate(file[0].replace('\\','\\\\'),file[1].replace('\\','\\\\'))
start()