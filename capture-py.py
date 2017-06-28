#TODO Add whitelist

import sys, time, shutil, os, datetime
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

def copyFile(srcfile): #copies and renames files
    dstfile = os.path.abspath(logPath) + '\\' + datetime.datetime.now().isoformat().replace(':','-')  + '-' +  os.path.basename(srcfile)
    cwPath = os.path.dirname(os.path.abspath(__file__))
    if  cwPath.lower() not in srcfile.lower():
      
        try:
            shutil.copyfile(srcfile,dstfile)
            print(srcfile + ' --> ' + dstfile)
            with open('cap-py.txt', 'a') as f:     #log files captured to cap-py.txt
                f.write(datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S') + ',' + srcfile + ',' + dstfile + '\n')
        except (OSError, IOError):
            pass
   
class FileEventHandler(FileSystemEventHandler): #Fires on file event
    def on_modified(self, event): #runs on file modified
        srcfile = str(event).split("'")[1].replace('\\\\','\\') #extract file name and path
        copyFile(srcfile)
           
    def on_deleted(self, event): #runs of file deleted
        srcfile = str(event).split("'")[1].replace('\\\\','\\') #extract file name and path
        copyFile(srcfile)

if len(sys.argv) != 3: #check if all arguments are provded or exit
    print('cap-py.py <watch-path> <archive-path>')
    sys.exit()
    
watchPath = sys.argv[1] #files to watch
logPath = sys.argv[2] #where to log/archive files

if not os.path.exists(logPath): #if logPath doesn't exsist, create it.
    os.makedirs(logPath)

event_handler = FileEventHandler()
observer = Observer()
observer.schedule(event_handler, watchPath, recursive=True)
observer.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()
observer.join()
