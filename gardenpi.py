import datetime
import os
import shutil
import subprocess

# get todays date in yyyymmdd
today = datetime.datetime.now().strftime ("%Y%m%d")

# source and destination locations
src = r'/home/pi/pi-timolo/media/motion'
des = r'/home/pi/Documents/garden/' + today


os.mkdir(des)

# move all the files from src to destination 
srcfiles = os.listdir(src)

# copy the files to the new destination...
for f in srcfiles:
    shutil.copy(os.path.join(src,f), des)

# then delete them...
for f in srcfiles:
    os.remove(os.path.join(src,f))

# cd to where the files have been moved to
os.chdir(des)

desfiles = sorted(os.listdir(des))

# create a file containing the contents of the folder
with open('mylist.txt', 'w') as mylist:
    for f in desfiles: # need to sort the files by name
        mylist.write("file './" + f + "'\n")    
    
# command to create one mp4 from all the mp4s in the directory
mergedfilename = today + '.mp4'

# subprocess.run(['ffmpeg','-f', 'concat', '-safe', ' 0', '-i', 'mylist.txt', '-c', 'copy', 'video.mp4'])
subprocess.run(['ffmpeg','-f', 'concat', '-safe', ' 0', '-i', 'mylist.txt', '-c', 'copy', mergedfilename])
