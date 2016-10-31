# !/usr/bin/python

__version__ = '0.0.1'


from datetime import datetime
from datetime import timedelta

import time
import hashlib

import threading

from packages.fileHasher import fileHasher
from packages.logIt import logIt

import os 


"""
TODO:
    compare hashes
    passing arguments (multiple directories)
    recursive vs. non-recursive

"""
 
interval = 10


def poll(target, logger = None):
    if logger:
        logger.log('pollint' + target)
        startTotal = time.time()
    
    hasher = fileHasher(hashlib.md5, logger)
    for root, dirs, files in os.walk(target):
        for name in files:
            if logger:
                logger.log(name)
                start = time.time()    
            hasher.fileHash(os.path.join(root,name))          
            if logger:
                stop = time.time()
                logger.log('time: ' + '%s' % (stop-start))
                logger.log('-----')
    if logger:
        stop = time.time()
        logger.log('time: ' + '%s' % (stop-startTotal))
    return hasher.WholeHash()

if __name__ == "__main__":
    directoryHashes = list()
    
    #path = r'P:\PRO-378\TestPosit\nightlyBuilds'
    path = r'/home/norman/Downloads/'
    #path = r'C:\Users\nom\Downloads'
    if os.path.exists(path):    
        debug = True
        logger = logIt(os.getcwd(), 'logger'+datetime.utcnow().strftime("%Y-%m-%d-%H-%M-%S")+'.txt', debug)
        d = timedelta(seconds=interval)
        start = datetime.utcnow()
        directoryHashes.append((start.strftime("%Y-%m-%d %H:%M:%S"),poll(path, logger)))
        try:
            while True:
                stop = datetime.utcnow()
                if stop-start > d:
                    directoryHashes.append((stop.strftime("%Y-%m-%d %H:%M:%S"),poll(path, logger)))
                    start = datetime.utcnow() 
                    #print stop - start
                    #if logger: 
                    #    for tup in directoryHashes:                    
                    #        logger.log(' --> '.join(tup))
        except KeyboardInterrupt:
            print 'stopping the application'
    else:
        print 'path does not exist', path
