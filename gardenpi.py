import datetime
import os
import shutil
import subprocess

# get todays date in yyyymmdd
today = datetime.datetime.now().strftime ("%Y%m%d")
#print(today)

# source and destination locations
src = r'/home/pi/pi-timolo/media/motion'
des = r'/home/pi/Documents/garden/' + today

os.mkdir(des)

# cd to where the files are 
os.chdir(src)

# sort the directory contents by name
srcfiles = sorted(os.listdir(src))
#print(desfiles)

# create a file containing the contents of the folder
with open('filelist.txt', 'w') as filelist:
    for f in srcfiles: 
        filelist.write("file './" + f + "'\n")    
    
# example filename 20200520.mp4
videofilename = today + '.mp4'

# create one mp4 from all the mp4s in the directory
subprocess.run(['ffmpeg','-f', 'concat', '-safe', ' 0', '-i', 'filelist.txt', '-c', 'copy', videofilename])

# copy the video to the destination directory
print("copying video file")
shutil.copy(os.path.join(src,videofilename), des)

# remove all the files from the src directory
filestodelete = os.listdir(src)
for f in filestodelete:
    os.remove(os.path.join(src,f))
    