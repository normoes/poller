import os

class logIt():
    def __init__(self, path, filename, debug = False):
        self.filename = filename
        self.debug = debug
        self.path = path
        self.fh = None
    def log(self, toLog):
        if self.debug:
            ## terminal output
            print toLog
            ## log file output
            self.fh = open(os.path.join(self.path,self.filename), 'a')
            try:            
                self.fh.write(toLog+'\n')
            except IOERROR:
                print 'no access to log file:', self.filename
            finally:
                self.fh.close()
