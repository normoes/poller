# !/usr/bin/python
"""

hashlib.md5().update considers order of files in the following way:
    assume:
        /pictures
            /products
                1.png
                2.png
                company_logo.png
            logo.png
    --> produces HASH1
    assume the following change:
        /pictures
            /products
                1.png
                2.png
            company_logo.png
            logo.png
    --> produces HASH2
--> HASH1 <> HASH2    

"""

__version__ = '0.0.1'


from datetime import datetime
from datetime import timedelta

import time
import hashlib

import threading

from packages.hasher.fileHasher import fileHasher

import os 
 
interval = 10

from packages.logger.logIt import logIt

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
    path = r'/home/norman/Downloads/adsodbc-11.10.0.24/'
    #path = r'C:\Users\nom\Downloads'
    if os.path.exists(path):    
        debug = True
        logger = logIt(os.getcwd(), 'logger'+datetime.now().strftime("%Y-%m-%d-%H-%M-%S")+'.txt', debug)
        d = timedelta(seconds=interval)
        start = datetime.now()
        directoryHashes.append((start.strftime("%Y-%m-%d %H:%M:%S"),poll(path, logger)))
	
        while True:
            stop = datetime.now()
            if stop-start > d:
                directoryHashes.append((stop.strftime("%Y-%m-%d %H:%M:%S"),poll(path, logger)))
                start = datetime.now() 
                if logger: 
                    for tup in directoryHashes:                    
                        logger.log(' --> '.join(tup))
    else:
        print 'path does not exist', path