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

def execCMD(command):
    p = sub.Popen(command,shell = True,stdout =sub.PIPE,stderr = sub.STDOUT)
    output,errors = p.communicate()  
    return output

def remakeCsvHistoryLogin(inputCsv,outputCsv='tmp.csv'):
	listPID = getUserNameAndPID()
	with open(inputCsv, 'rb') as inp, open(outputCsv, 'wb') as out:
		writer = csv.writer(out)
		for row in csv.reader(inp):
			try:
				if row[1] == '2':
					row[1]='Logon'
					for a in listPID:
						if row[15] in a:
							row[15]=a
					writer.writerow(row)
				elif row[1] == '4':
					for a in listPID:
						if row[15] in a:
							row[15]=a
					row[1]='Logoff'
					writer.writerow(row)
				elif row[0] == 'Message':
					row[1] = 'Action'
					row[15] = 'UserNameAndPID'
					writer.writerow(row)
			except:
				continue
	inp.close()
	out.close()
	deleteTrashColumn(outputCsv)
	os.remove(outputCsv)
	

def deleteTrashColumn(inputCsv):
	f=pd.read_csv(inputCsv)
	keep_col = [u'Action',u'MachineName',u'UserNameAndPID',u'TimeCreated']
	new_f = f[keep_col]
	new_f.to_csv("REPORT\\ReleaeHistoryLogin.csv", index=False)

def getUserNameAndPID():
	data = execCMD('wmic useraccount get name,sid')
	data=data.split('\n')[:-1]
	for a in data:
		if len(a) < 5 or 'SID' in a or a == '':
			data.remove(a)
	return data
