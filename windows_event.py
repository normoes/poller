"""pathwatcher.py - Monitor a directory for file additions / deletions
Watch a named directory for any new or removed files. More sophisticated
 notifications could be added, for example looking for changes in file
 sizes etc. It doesn't seem possible to determine from the system call
 *which* files were added or removed, so the simple expedient is adopted
 of listing all files before waiting and then comparing with the
 equivalent list when notified.
"""

import os
import sys
import time

import win32file
import win32event
import win32con

#
# The path to be watched would normally be passed as the parameter
#  to the script. If it is not, or if the parameter is blank, the
#  current directory is assumed, whatever that means in the context
#  of the script's execution.
#
try: path_to_watch = sys.argv[1] or "."
except: path_to_watch = "."
path_to_watch = os.path.abspath (path_to_watch)

print "Watching %s at %s" % (path_to_watch, time.asctime ())

#
# FindFirstChangeNotification sets up a handle for watching
#  file changes. The first parameter is the path to be
#  watched; the second is a boolean indicating whether the
#  directories underneath the one specified are to be watched;
#  the third is a list of flags as to what kind of changes to
#  watch for. We're just looking at file additions / deletions.
#
change_handle = win32file.FindFirstChangeNotification (
  path_to_watch,
  0,
  win32con.FILE_NOTIFY_CHANGE_FILE_NAME | win32con.FILE_NOTIFY_CHANGE_SIZE
)

#
# Loop forever, listing any file changes. The WaitFor... will
#  time out every half a second allowing for keyboard interrupts
#  to terminate the loop.
#
suffixes = ['B', 'KB', 'MB', 'GB', 'TB', 'PB']
def humansize(nbytes):
    if nbytes == 0: return '0 B'
    i = 0
    while nbytes >= 1024 and i < len(suffixes)-1:
        nbytes /= 1024.
        i += 1
    f = ('%.2f' % nbytes).rstrip('0').rstrip('.')
    return '%s %s' % (f, suffixes[i])    
    
        

try:

  while 1:
    old_path_contents = os.listdir (path_to_watch)
    old_file_sizes = {f: os.stat(os.path.join(path_to_watch,f)).st_size for f in old_path_contents}
    result = win32event.WaitForSingleObject (change_handle, 500)

    #
    # If the WaitFor... returned because of a notification (as
    #  opposed to timing out or some error) then look for the
    #  changes in the directory contents.
    #
    if result == win32con.WAIT_OBJECT_0: 
      new_path_contents = os.listdir (path_to_watch)  
      new_file_sizes = {f: os.stat(os.path.join(path_to_watch,f)).st_size for f in new_path_contents}
      file_size_changed = {f: os.stat(os.path.join(path_to_watch,f)).st_size for f in new_file_sizes.keys() if f in old_file_sizes.keys() and old_file_sizes[f] != new_file_sizes[f]}

      files_added = [f for f in new_path_contents if not f in old_path_contents]
      files_deleted = [f for f in old_path_contents if not f in new_path_contents]

      if files_added or files_deleted:
        print
        print time.asctime ()
        print "Added:", files_added or "Nothing"
        print "Deleted:", files_deleted or "Nothing"
      if file_size_changed:
        print
        print time.asctime ()
        print "size changed:", file_size_changed or "Nothing"

      win32file.FindNextChangeNotification (change_handle)

finally:
  win32file.FindCloseChangeNotification (change_handle)