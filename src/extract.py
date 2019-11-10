import zipfile    
import rarfile              
import os
import glob
import sys

class Extract_archive:
    
    def __init__(self):
        self.SOURCE_DIRECTORY = 'archives'
        self.DESTINITION_DIRECTORY = 'dumps'
        self.INITIAL_DIRECTORY_NAME = 1
        self.UNRAR_PATH = 'C:\\Program Files\\WinRAR\\UnRAR.exe'    # Used when the script is running on Windows OS
        self.EXCEPTIONS = dict()                                    # To store all the exceptions
    
    def unzip(self):
        os.chdir(os.path.normpath(os.getcwd() + os.sep + self.SOURCE_DIRECTORY))  
        
        for file in glob.glob('*.zip'):
            try:
                with zipfile.ZipFile(file, 'r') as zipObj:
                    zipObj.extractall(os.path.normpath(os.getcwd() + os.sep + '..' + os.sep + self.DESTINITION_DIRECTORY + os.sep + str(self.INITIAL_DIRECTORY_NAME)))
                print(f'Extracted: {file} -----> {str(self.INITIAL_DIRECTORY_NAME)}')
                self.INITIAL_DIRECTORY_NAME += 1
            except:
                print(f'\n*****\nALERT for FILE: {file}\nException: {sys.exc_info()[1]}\nException type: {sys.exc_info()[0]}\n*****\n')
                self.EXCEPTIONS[f'File: {str(file)}'] = f'Exception type: {sys.exc_info()[0]}, {sys.exc_info()[1]}'

        os.chdir(os.path.normpath(os.getcwd() + os.sep + '..'))
        
    def unrar(self): 
        os.chdir(os.path.normpath(os.getcwd() + os.sep + self.SOURCE_DIRECTORY)) 
        
        if os.name == 'nt':
            rarfile.UNRAR_TOOL = self.UNRAR_PATH
        
        for file in glob.glob('*.rar'):
            try:
                with rarfile.RarFile(file, 'r') as rarObj:
                    rarObj.extractall(os.path.normpath(os.getcwd() + os.sep + '..' + os.sep + self.DESTINITION_DIRECTORY + os.sep + str(self.INITIAL_DIRECTORY_NAME)))
                print(f'Extracted: {file} -----> {str(self.INITIAL_DIRECTORY_NAME)}')
                self.INITIAL_DIRECTORY_NAME += 1
            except:
                print(f'\n*****\nALERT for FILE: {file}\nException: {sys.exc_info()[1]}\nException type: {sys.exc_info()[0]}\n*****\n')
                self.EXCEPTIONS[f'File: {str(file)}'] = f'Exception type: {sys.exc_info()[0]}, {sys.exc_info()[1]}'
                  
        os.chdir(os.path.normpath(os.getcwd() + os.sep + '..'))   
        
    def check_exceptions(self):   
        if self.EXCEPTIONS:
            print("\nExtraction complete with the following Exceptions:")
            for key, value in self.EXCEPTIONS.items():
                print(f'{key} -----> {value}')
        else:
            print("\nExtraction complete.....\n")
       
    def boot(self):
        self.unzip()
        self.unrar()
        self.check_exceptions()