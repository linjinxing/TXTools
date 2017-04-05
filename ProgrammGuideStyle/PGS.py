#!/usr/bin/env python

import re
import os
import json
import codecs

def writeFile(path, text):
    """
        写文件回去
    """     
    file = open(path, 'w')
    try:
        file.write(text)
    except Exception, error:
    	print str(error)
        raise
    finally:
        print "关闭文件: ", path
        file.close()

def readFile(path):
    """
        获取文件的内容
    """
    file = open(path, 'r')  
    try:
        return file.read()
    except Exception, error:
    	print str(error)
    finally:
        print "关闭文件: ", path
        file.close()
    return ""

def addViewPragmaMark(text, pragmaMark):


def addControllerPragmaMark(text, pragmaMark):
	

def findSourceCodeTemplateFiles(path):
	returnFiles = []
	for rt, dirs, files in os.walk(path):
		for dir in dirs:
			print "dir:" , dir
			returnFiles += findSourceCodeTemplateFiles(dir)
		returnFiles += files
	return returnFiles





