import os 
import shutil
import re
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time

watchPath = "C:\\Users\\ahnaf\\Downloads"


trackList = {
        ".jpg$" : watchPath+"\\Images",
        ".png$" : watchPath+"\\Images",
        ".webm$": watchPath+"\\Webms",
        ".mp4$": watchPath+"\\Vids",
        ".pdf$": watchPath+"\\Pdfs",
        ".rbxl$": watchPath+"\\RobloxFiles",
        ".rbxm$": watchPath+"\\RobloxFiles\\Rbmxs",
        ".docx$": watchPath+"\\Documents",
        ".zip$" : watchPath+"\\Zips",
        ".txt$" : watchPath+"\\Text Files",
        ".exe$" : watchPath+"\\Executables",
        ".wav$" : watchPath+"\\Wavs",       
}

unsorted = watchPath+"\\Unsorted"

class SortFolder(FileSystemEventHandler):
    
    def on_modified(self, event):
        for file in os.listdir(watchPath): # for each of the items in the dirclass
            found = False
            print(file + " FOUND? " + str(found))

            for extension, location in trackList.items():   # compare the extension of the file against tracklist
                if found : break 
                print("trying" + str(extension))
                
                if re.search(extension, file):  # if there is a match
                    if not os.path.exists(location): # check if the folder where it's meant to go doesnt exists
                        try:
                            print("making dir " + location)
                            os.makedirs(location)
                        except OSError as error:
                            print(error)

                    print(watchPath+"\\"+file+" -> " + location + "\\" + file)
                    #os.rename(watchPath+"\\"+file,location+"\\"+file)
                    try:
                        os.replace(watchPath+"\\"+file,location+"\\"+file)
                        found = True
                    except OSError as error:
                        print(error)

            print("UNSORTED")
            if not os.path.exists(unsorted): # check if the folder where it's meant to go doesnt exists
                try:
                print("making dir " + unsorted)
                    os.makedirs(unsorted)
                    found = True
                except OSError as error:
                    print(error)


observer = Observer()
event_handler = SortFolder()
observer.schedule(event_handler, watchPath, recursive = False)
observer.start()

try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
observer.join()

