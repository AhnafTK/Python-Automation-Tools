import os
#import re
# from watchdog.observers import Observer
# from watchdog.events import FileSystemEventHandler
# import time

watch_path = "C:\\Users\\ahnaf\\Downloads\\test2"
# where the unsorted files go (folders aren't sorted)
unsorted = watch_path+"\\Unsorted"
# dictionary containing the targetted formats and their dest
track_list = {
    ".jpg": watch_path+"\\Images",
    ".png": watch_path+"\\Images",
    ".webm": watch_path+"\\Webms",
    ".mp4": watch_path+"\\Vids",
    ".pdf": watch_path+"\\Pdfs",
    ".docx": watch_path+"\\Documents",
    ".zip": watch_path+"\\Zips",
    ".txt": watch_path+"\\Text Files",
    ".exe": watch_path+"\\Executables",
    ".wav": watch_path+"\\Wavs",
    ".mov": watch_path+"\\movs",
}

for file in os.listdir(watch_path): 
    # print(file)

    # get the extension of the file
    # returns tuple, index 1 contains extension
    file_extension = os.path.splitext(file)[1]

    if file_extension.lower() in track_list:
        # it exists
        dest_path = track_list[file_extension.lower()]
        # check if the folder where it's meant to go doesnt exists
        if not os.path.exists(dest_path):
            try:
                print("making dir " + dest_path)
                os.makedirs(dest_path)
            except OSError as error:
                print(error)

        try:
            os.replace(watch_path+"\\"+file, dest_path+"\\"+file)
        except OSError as error:
            print(error)

    else:
        # check if its a folder
        if os.path.isfile(watch_path+"\\"+file):
            print(watch_path+"\\"+file + " iS FILE")
            dest_path = unsorted
            try:
                os.replace(watch_path+"\\"+file, unsorted+"\\"+file)
            except OSError as error:
                print(error)
