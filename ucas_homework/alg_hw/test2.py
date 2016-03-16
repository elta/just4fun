#! /usr/bin/python

import os;
import tarfile;

def list_path(path="/"):
    return os.listdir(path)

def untarFile(filepath=""):
    # print "untar file"
    saveDir = os.getcwd()
    # print filepath, os.path.split(filepath)[0]
    os.chdir(os.path.split(filepath)[0])
    tar = tarfile.open(filepath, "r")
    tar.extractall()
    tar.close()
    os.chdir(saveDir)

def numSum(filepath=""):
    oFile = open(filepath)
    strNum = oFile.read()
    intNum = int(strNum)
    oFile.close()
    # print "Add new value ", intNum

    return intNum

def isGz(cFile=""):
    return os.path.splitext(cFile)[1] == '.gz'

def isDir(cFile=""):
    return os.path.isdir(cFile)

def isText(cFile=""):
    return os.path.splitext(cFile)[1] == ''

def enterDir(path="/"):
    count = 0

    path = path + "/"

    # Step 1, untar file
    for cFile in list_path(path):
        if isGz(path + cFile):
            untarFile(path + cFile)

    # Step 2, count or enter sub dir
    for cFile in list_path(path):
        if isDir(path + cFile):
            count += enterDir(path + cFile)
        elif isText(path + cFile):
            count += numSum(path + cFile)

    return count


# start
os.chdir("test")

print enterDir(os.getcwd())
