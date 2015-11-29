
if __package__ is None:
    import sys
    from os import path
    sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )    

from packages.files.fileChecker import fileChecker 
from packages.logger.logIt import logIt
import os

logger = logIt(os.getcwd(), 'test_log'+__name__+'.txt')
f = fileChecker(logger)

print f.process(r'P:\PRO-378\TestPosit\nightlyBuilds')
print f.exists(r'P:\PRO-378\TestPosit\nightlyBuilds')
print f.isEmpty(r'P:\PRO-378\TestPosit\nightlyBuilds')
