from zipfile import ZipFile
from rarfile import RarFile
import os
import shutil
# from glob import glob # For glob.extend
import glob             # for single glob
import re

# Run: pip install rarfile (https://rarfile.readthedocs.io/en/latest/api.html) also look at: https://stackoverflow.com/questions/43527641/extract-single-file-from-rar-archive-with-rarfile-in-python
#      Mac = brew install unrar / UBUNTU = sudo apt-get install -y rar unrar / 

class Extract_archive:
    
    def __init__(self):
        
        # Make sure the paths work with WINDOWS OS
        self.DESTINITION_PATH = 'dumps/'
        self.SOURCE_PATH = 'archives/'
        
        self.SOURCE = 'archives/1.rar' 
        
        self.FILE_BASE_NAME = os.path.basename(self.SOURCE)
        self.DESTINITION_DIRECTORY,  self.SOURCE_FILE_EXTENTION = os.path.splitext(self.FILE_BASE_NAME)
        self.DESTINITION = f'{self.DESTINITION_PATH}{self.DESTINITION_DIRECTORY}'

    def print_static_values(self):
        print(f'Source: {self.SOURCE}')
        print(f'File name: {self.FILE_BASE_NAME}')
        print(f'Extention: {self.SOURCE_FILE_EXTENTION}')
        print(f'Destinition: {self.DESTINITION}')
    
    def unzip(self):
        
        # NAVIGATING ONE DIRECTORY BACK AND THEN INSIDE THE 'archives' directory.
        # os.chdir()    Change directory
        # normpath()    Takes care of the Different OS path types
        # os.getcwd()   Get the current working directory
        # os.sep()      PATH SEPERATOR, \ for WINDOWS and / for LINUX / MAC
        os.chdir(os.path.normpath(os.getcwd() + os.sep + 'archives'))  
        
        # for file in os.scandir(self.SOURCE_PATH):
        for file in glob.glob(('*.zip')): # OR
            # destination_directory, source_file_extention = os.path.splitext(os.path.basename(file))
            destination_directory = os.path.splitext(file)[0] # OR
            # if source_file_extention == '.zip':
            with ZipFile(file, 'r') as zipObj: # OR ident
                # zipObj.extractall(f'{self.DESTINITION_PATH}{destination_directory}_ZIP') 
                zipObj.extractall(f'../{self.DESTINITION_PATH}{destination_directory}_ZIP') # OR
    
    def unrar(self):
        # os.chdir("/Users/hsingh/Documents/Python/compress_extract_tool/archives") 
        #! No need to run this because the current path has changed to /Users/hsingh/Documents/Python/compress_extract_tool/archives
        #! When we ran the os.chdir() in the previous step 
        # os.chdir(os.path.normpath(os.getcwd() + os.sep + 'archives'))
        
        #TODO find a way to use glob for multiple file extentions
        
        for file in glob.glob(('*.rar')):
            destination_directory = os.path.splitext(file)[0]
            with RarFile(file, 'r') as rarObj:
                rarObj.extractall(f'../{self.DESTINITION_PATH}{destination_directory}_RAR')
            
          
    def extract_archive(self):
        if self.SOURCE_FILE_EXTENTION == '.zip':
            with ZipFile(self.SOURCE, 'r') as zipObj:
                zipObj.extractall(f'{self.DESTINITION_PATH}{self.DESTINITION_DIRECTORY}') 
            print(f'UNZIP Complete. Please check {self.DESTINITION_PATH}')
        elif self.SOURCE_FILE_EXTENTION == '.rar':
            with RarFile(self.SOURCE, 'r') as rarObj:
                rarObj.extractall(f'{self.DESTINITION_PATH}{self.DESTINITION_DIRECTORY}')
            print(f'UNRAR Complete. Please check {self.DESTINITION_PATH}')
        else:
            print('Not supported')
            
    def boot(self):
        # self.print_static_values()
        self.unzip()
        self.unrar()
        # self.extract_archive()