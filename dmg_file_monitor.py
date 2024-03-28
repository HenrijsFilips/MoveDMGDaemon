import os #for path handling
import time #for sleep
import shutil #for file operations

#downloads path
downloads_dir = os.path.expanduser('~/Downloads')

#place to move the files
dmg_folder = "/Volumes/T7 Shield/DMG files"

def move_dmg_files():
    #iterate through each file in downloads folder
    for file in os.listdir(downloads_dir):
        if file.endswith(".dmg"):
            #add the file to the end of the path 
            source = os.path.join(downloads_dir, file)
            #add the file to the end of destination path
            destination = os.path.join(dmg_folder, file)
            
            shutil.move(source, destination)
            
#the part that monitors the downloads folder
def monitor_downlaods_folder():
    while True:
        move_dmg_files()
        #check every 10 seconds for new dmg files
        time.sleep(10)
        
if __name__ == "__main__":
    monitor_downlaods_folder()