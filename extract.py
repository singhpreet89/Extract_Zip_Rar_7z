from zipfile import ZipFile
from rarfile import RarFile # We need to download the official WinRAR folder from winrar website.
import os
import shutil

# Run: pip install rarfile (https://rarfile.readthedocs.io/en/latest/api.html) also look at: https://stackoverflow.com/questions/43527641/extract-single-file-from-rar-archive-with-rarfile-in-python
#      pip install patool (Support many formats: https://pypi.org/project/patool/ and DOCUMENTATION: http://wummel.github.io/patool/)
class Extract_archive:
    
    # This code will not handle the file names such as 'something.tar.gz'
    def __init__(self):
        
        # Make sure the paths work with WINDOWS OS
        self.DESTINITION_PATH = '/Users/hsingh/Documents/Python/compress_extract/Dumps'
        self.SOURCE = 'Archives/zip_2MB.zip' 
        self.FILE_BASE_NAME = os.path.basename(self.SOURCE)
        self.DESTINITION_DIRECTORY,  self.SOURCE_FILE_EXTENTION = os.path.splitext(self.FILE_BASE_NAME)
    
    def print_static_values(self):
        print(obj.SOURCE)
        print(obj.FILE_BASE_NAME)
        print(obj.DESTINITION_DIRECTORY)
        print(obj.SOURCE_FILE_EXTENTION)
     
    def read_archive(self):
        if self.SOURCE_FILE_EXTENTION == '.zip':
            with ZipFile(self.SOURCE, 'r') as zipObj:
                zipObj.extractall(f'{self.DESTINITION_PATH}/{self.DESTINITION_DIRECTORY}')
        elif self.SOURCE_FILE_EXTENTION == '.rar':
            print("Support for RAR file coming in future.")
        else:
            print('Not supported')
        
if __name__ == "__main__":
    obj = Extract_archive()
    obj.print_static_values()
    obj.read_archive()
   