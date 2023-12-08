import os 
import mimetypes
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
        ".exe$" : watchPath+"\\Executables"
}

class SortFolder(FileSystemEventHandler):

    def on_modified(self, event):
        for file in os.listdir(watchPath): # for each of the items in the dirclass
            for extension, location in trackList.items():   # compare the extensions against the name of the file
                if re.search(extension, file):  # if there is a match
                    if not os.path.exists(location): # check if the folder where it's meant to go doesnt exists
                        try:
                            print("making dir " + location)
                            os.makedirs(location)
                        except OSError as error:
                            print(error)

                    print(watchPath+"\\"+file+" -> " + location + "\\" + file)
                    os.rename(watchPath+"\\"+file,location+"\\"+file)
                    #break


observer = Observer()
event_handler = SortFolder()
observer.schedule(event_handler, watchPath, recursive = False)
observer.start()

try:
    while True:
        time.sleep(3)
except KeyboardInterrupt:
    observer.stop()
observer.join()

