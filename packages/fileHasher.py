import os

from packages.fileChecker import fileChecker 

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
def test():
    import hashlib
    fileh = fileHasher(hashlib.md5)
    import os
    print fileh.fileHash(os.getcwd()+os.sep+'__init__.py')
    print fileh.fileHash(os.getcwd()+os.sep+'fileHasher.py')
    print fileh.fileHash(os.getcwd()+os.sep+'12.txt')
    print fileh.WholeHash()
    
    
if __name__ == '__main__':
    print __package__
    print __name__
    print __file__   
