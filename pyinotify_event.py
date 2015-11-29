import pyinotify

# The watch manager stores the watches and provides operations on watches
wm = pyinotify.WatchManager()

mask = pyinotify.IN_DELETE | pyinotify.IN_CREATE  # watched events
#mask = pyinotify.ALL_EVENTS

class EventHandler(pyinotify.ProcessEvent):
    def process_IN_CREATE(self, event):
        print event
        print "Creating:", event.pathname

    def process_IN_DELETE(self, event):
        print "Removing:", event.pathname
        
    def process_IN_MODIFY(self, event):                                             
        #if not suffix_filter(event.name):                                           
        print "Modifing:", event.pathname   
        
handler = EventHandler()
# Notifier(wm, handler, timeout=10)
notifier = pyinotify.Notifier(wm, handler)
# Internally, 'handler' is a callable object which on new events will be called like this: handler(new_event)

wdd = wm.add_watch('/tmp', mask, rec=True)
"""
#remove hooks again
wm.rm_watch(wdd['/tmp'], rec=True)
#Or even better like this
wm.rm_watch(wdd.values())
"""
notifier.loop()

#notifier.stop()


