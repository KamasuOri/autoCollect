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
	# print sample
	if os.path.exists(sample):
		src = os.path.realpath(sample)
	root_dir,tail = os.path.split(src)
	shutil.make_archive(sample,"zip",sample)

def startUpdateReportFile(dirPath,DBPath):
	listDir = os.listdir(dirPath)
	for a in listDir:
		if len(a)>30 and "report-"	in a:
			print "Handle report hash: "+a
			updateDataFormReportDir(dirPath+"\\"+a+"\\")
			tmp = dirPath+"\\"+a
			try:
				shutil.move(tmp.replace('\\','\\\\'),DBPath)
			except:
				print "delete"
				shutil.rmtree(tmp.replace('\\','\\\\'))
def updateDataFormReportDir(dirPath):
	tmpData =''
	splitData = []
	reportData = open(dirPath+"pcInfo.txt","r").read().split("+--------+")
	# print reportData
	for a in reportData:
		if (len(a)>2):
			splitData.append(a.replace("\n","").replace("\r","").strip().replace("    ","||"))
			tmpData += a.replace("\n","").replace("\r","").strip().replace("    ","||") +'\n'
	# print tmpData    # data của log file. xử lý sau
	addDataToReportDataFile(tmpData)
	# zipDir(dirPath[:-1].replace('\\','\\\\'))
	# shutil.rmtree(dirPath[:-1].replace('\\','\\\\'))

def addDataToReportDataFile(a):
	f = open("reportData.txt","a")
	f.write(a)
	f.write("============================================================================================================\n")
	f.close()

########################################################################################################################################################################################

def remakeReportDataFile(DBPath):
	listDir = os.listdir(DBPath)
	f = open("reportData.txt","w")
	for a in listDir:
		if len(a)>30 and "report-"	in a:
			
			print "Handle report hash: "+a
			newPath = DBPath+"\\"+a+"\\"
			
			reportData = open(newPath+"pcInfo.txt","r").read().split("+--------+")

			tmpData=''
			for a2 in reportData:
				if (len(a2)>2):
					tmpData += a2.replace("\n","").replace("\r","").strip().replace("    ","||") +'\n'
			f.write(tmpData)
			f.write("============================================================================================================\n")
	f.close()
########################################################################################################################################################################################

def start():
	file = open("control.txt","r").read().split("\n")
	try:
		if "updateReportFile" in file[0]:
			startUpdateReportFile(file[1].replace('\\','\\\\'),file[2].replace('\\','\\\\'))
		if "remakeReportDataFile" in file[0]:
			remakeReportDataFile(file[2].replace('\\','\\\\'))
	except:
		return 1
start()