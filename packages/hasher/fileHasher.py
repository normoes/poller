import os

from packages.files.fileChecker import fileChecker 

BLOCKSIZE = 128


class fileHasher():
    def __init__(self, hashMethod, logger = None):
        self.hashMethod = hashMethod
        self.hasher_whole = None
        self.logger = logger
        self.fileChecker = fileChecker(logger)    

    def fileHash(self, name):
        if self.fileChecker.process(name):
            with open(name,'rb') as fh:
                hasher = self.hashMethod()
                if not self.hasher_whole:
                    self.hasher_whole = self.hashMethod() 
                for chunk in iter(lambda: fh.read(BLOCKSIZE), b''): 
                    hasher.update(chunk)            
                    self.hasher_whole.update(chunk)
            if self.logger:
                self.logger.log('Hash: ' + hasher.hexdigest())
            return hasher.hexdigest()           
        return ''

    def WholeHash(self):
        if self.hasher_whole:            
            return self.hasher_whole.hexdigest()        
        return ''    
