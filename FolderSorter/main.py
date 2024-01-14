import os
#import re
# from watchdog.observers import Observer
# from watchdog.events import FileSystemEventHandler
# import time

watch_path = "C:\\Users\\ahnaf\\Downloads\\test2"   # The folder that is sorted
unsorted = watch_path+"\\Unsorted"                  # where the unsorted files go (folders aren't sorted)
dest_path = ""                                      # Destination path
debug_mode = False                                  # prints output when true

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

for file in os.listdir(watch_path):                 # iterate through each file in the watched folder
    if debug_mode : print(file)
    # if its a folder, then skip
    if not os.path.isfile(watch_path+"\\"+file):    # If it's not a file, then skip. Folders aren't sorted
        continue
    
    file_extension = os.path.splitext(file)[1]      # get the file extension from the returned tuple

    if file_extension.lower() in track_list:                 # if its in the track list
        dest_path = track_list[file_extension.lower()]
        if debug_mode : print("IN TRACKLIST: "+ dest_path)
    else: # if its not
        dest_path = unsorted
        if debug_mode : print("UNSORTED: "+ dest_path)

    # check if the destination exists
    if not os.path.exists(dest_path):                                   # if the dest folder doesnt exists
        if debug_mode : print("DEST DOESNT EXIST: " + dest_path)
        if debug_mode : print("MAKING: " + dest_path)
        try:
            os.makedirs(dest_path)                                      # make the dest folder
        except OSError as error:   
            print(error)

    try:
        os.replace(watch_path+"\\"+file, dest_path+"\\"+file)           # move the items
    except OSError as error:
        print(error)
    
    if debug_mode : print(" ")