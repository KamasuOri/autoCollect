#!/usr/bin/python
# -*- coding: utf8 -*-
'''
a==1 	= success
a==2	= fail
'''
def log(a,msg):
	if a ==1:
		logMsg = "++ SUCCESS "+msg+"\n"
	else:
		logMsg = "-- FAIL "+msg+"\n"
	f = open("runLog.txt","a")
	f.write(logMsg)
	f.close()