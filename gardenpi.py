'''Concatenates mp4 files into one mp4 file 
 
 Usage:
    python gardenpi.py
'''


import datetime
import os
import shutil
import subprocess


def get_todays_date_as_str():
    '''Return todays date as a string in the format
       yyyymmdd
    '''
    today = datetime.datetime.now().strftime ("%Y%m%d")

    return today


def get_source_files_path():
    '''Returns the path of where the source files are
       located    
    '''
    src = r'C:\Users\Ian\Documents\GitHub\GardenPi\TestFilesSrc' # r'/home/pi/pi-timolo/media/motion'

    return src
    

def get_file_destination_path():
    '''Returns the path of where the destination file 
       will be saved
    '''    
    des = r'C:\Users\Ian\Documents\GitHub\GardenPi\TestFilesDes' #r'/home/pi/Documents/garden/' + today

    return des


def create_file_destination_directory(path):
    '''Creates the directory for the supplied path

       Args: 
           path: string containing the location of where
                 the directory should be created
    '''
    os.mkdir(path)


def create_filelist(srcfiles):
    '''Create a file containing the contents of the folder

       Args:
           srcfiles: list of source files
    '''
    with open('filelist.txt', 'w') as filelist:
        for f in srcfiles:
            filelist.write("file './" + f + "'\n")    
    

def create_mp4_file(filename):
    '''Create one mp4 from all the mp4s in the directory

       Args:
          filename: the filename of new mp4 file created by this 
                    process
    '''
    subprocess.run(['ffmpeg','-f', 'concat', '-safe', ' 0', '-i', 'filelist.txt', '-c', 'copy', filename])


def copy_mp4_file_to_destination(src, videofilename, des ):
    '''Copies the combined mp4 file to the destination directory

       Args:
           src: path of the source files
           videofilename: filename of the mp4 file
           des: path to where the filename should be copied to           
    '''        
    print("copying video file")
    shutil.copy(os.path.join(src,videofilename), des)

def delete_source_files(path):
    '''Remove all the files from the src directory

       Args: 
           path: location of the files to be deleted
    '''
    filestodelete = os.listdir(path)
    
    for f in filestodelete:
        os.remove(os.path.join(path,f))


def main():
    '''
    '''

    today = get_todays_date_as_str()

    # example filename 20200520.mp4
    video_file_name = today + '.mp4'

    src = get_source_files_path()
    
    des = get_file_destination_path()

    create_file_destination_directory(des)

    # cd to where the files are 
    os.chdir(src)

    # sort the directory contents by name
    srcfiles = sorted(os.listdir(src))

    create_filelist(srcfiles)

    create_mp4_file(video_file_name)
    
    copy_mp4_file_to_destination(src, video_file_name, des )

    delete_source_files(src)


if __name__ == '__main__':
    main() 

