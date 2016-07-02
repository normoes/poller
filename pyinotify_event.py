import pyinotify

# The watch manager stores the watches and provides operations on watches
wm = pyinotify.WatchManager()

#mask = pyinotify.IN_DELETE | pyinotify.IN_CREATE | pyinotify.IN_CLOSE_WRITE  # watched events
mask = pyinotify.ALL_EVENTS

class EventHandler(pyinotify.ProcessEvent):
    def process_IN_CREATE(self, event):
        #print event
        print "Creating:", event.pathname, event.name
	print

    def process_IN_DELETE(self, event):
        print "Removing:", event.pathname, event.name
	print
        
    def process_IN_MODIFY(self, event):                                             
        #if not suffix_filter(event.name):                                           
        print "Modifying:", event.pathname, event.name   
	print
    def process_IN_CLOSE_WRITE(self,event):
        print "close write", event.pathname, event.name
	print
    def process_IN_MOVED_FROM(self,event):
        print "move from", event.pathname, event.name
	print
    def process_IN_MOVED_TO(self,event):
        print "moved to", event.pathname, event.name
	print
    def process_default(self,event):
        print "default", event.pathname
        print event
	print
handler   = EventHandler()

class CommitFunction(pyinotify.ProcessEvent):
    def process_default(self, event):
        print '{0}, {1}'.format(event.path, event.name)

# Notifier(wm, handler, timeout=10)
#notifier = pyinotify.Notifier(wm, handler)
notifier  = pyinotify.AsyncNotifier(wm, handler)
# Internally, 'handler' is a callable object which on new events will be called like this: handler(new_event)

wdd = wm.add_watch('/tmp/New Folder', mask, rec=True, auto_add=True) #, auto_add=True, proc_fun=CommitFunction())
"""
#remove hooks again
wm.rm_watch(wdd['/tmp'], rec=True)
#Or even better like this
wm.rm_watch(wdd.values())
"""
#notifier.loop(daemonize=False, callback=None)
import asyncore
asyncore.loop()

#notifier.stop()


