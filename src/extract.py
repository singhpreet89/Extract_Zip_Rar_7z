from zipfile import ZipFile    
import rarfile
from py7zr import SevenZipFile               
import os
from glob import glob
import sys
from dotenv import load_dotenv

class Extract_archive: 
    def __init__(self):
        load_dotenv()
        
        self.SOURCE_DIRECTORY = os.getenv("SOURCE_DIRECTORY")
        os.chdir(os.path.normpath(os.getcwd() + os.sep + self.SOURCE_DIRECTORY))

        self.DESTINITION_DIRECTORY = os.getenv("DESTINITION_DIRECTORY")
        self.INITIAL_DIRECTORY_NAME = int(os.getenv("INITIAL_DIRECTORY_NAME"))
        self.WINDOWS_OS_UNRAR_PATH = os.getenv("WINDOWS_OS_UNRAR_PATH")
        self.SUPPORTED_FORMATS = ['*.' + value for value in os.getenv("SUPPORTED_FORMATS").split(',')]

        self.EXCEPTIONS = dict()                                          

    def extract(self):
        if os.name == 'nt':
            rarfile.UNRAR_TOOL = self.WINDOWS_OS_UNRAR_PATH

        print("\n******************** EXTRACTED files ********************")
        count = 1
        for format in self.SUPPORTED_FORMATS:
            for file in glob(format):
                try:
                    if format == '*.zip':
                        with ZipFile(file, 'r') as zipObj:
                            zipObj.extractall(os.path.normpath(os.getcwd() + os.sep + '..' + os.sep + self.DESTINITION_DIRECTORY + os.sep + str(self.INITIAL_DIRECTORY_NAME)))
                    elif format == '*.rar':
                        with rarfile.RarFile(file, 'r') as rarObj:
                            rarObj.extractall(os.path.normpath(os.getcwd() + os.sep + '..' + os.sep + self.DESTINITION_DIRECTORY + os.sep + str(self.INITIAL_DIRECTORY_NAME)))
                    elif format == '*.7z':
                        with SevenZipFile(file, 'r') as sevenZObj:
                            sevenZObj.extractall(os.path.normpath(os.getcwd() + os.sep + '..' + os.sep + self.DESTINITION_DIRECTORY + os.sep + str(self.INITIAL_DIRECTORY_NAME)))
                    print(f'{count}. FILE: {file} =====> {str(self.INITIAL_DIRECTORY_NAME)}\n----------------------------------------------------------------------------------------')
                    self.INITIAL_DIRECTORY_NAME += 1
                    count += 1
                except:
                    self.EXCEPTIONS[f'File: {str(file)}'] = f'Exception type: {sys.exc_info()[0]}, {sys.exc_info()[1]}'

    def check_exceptions(self):   
        if self.EXCEPTIONS:
            print("\n******************** EXCEPTIONS ********************")
            for key, value in self.EXCEPTIONS.items():
                print(f'{key} =====> {value}')
            print("\nEXTRACTION finished with one or more exceptions.....")
        else:
            print('\nEXTRACTION finished.....')

    def boot(self):
        self.extract()
        self.check_exceptions()