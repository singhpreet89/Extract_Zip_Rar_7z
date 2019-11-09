import zipfile    
import rarfile              
import os
import glob
        
class Extract_archive:
    
    def __init__(self):
        self.SOURCE_DIRECTORY = 'archives'
        self.DESTINITION_DIRECTORY = 'dumps'
        self.UNRAR_PATH = 'C:\\Program Files\\WinRAR\\UnRAR.exe'    # Used when the script is running on Windows OS
    
    def unzip(self):
        os.chdir(os.path.normpath(os.getcwd() + os.sep + self.SOURCE_DIRECTORY))  
        
        for file in glob.glob(('*.zip')):
            archive_directory = os.path.splitext(file)[0]
            with zipfile.ZipFile(file, 'r') as zipObj:
                zipObj.extractall(os.path.normpath(os.getcwd() + os.sep + '..' + os.sep + self.DESTINITION_DIRECTORY + os.sep + archive_directory + '_ZIP'))
        
        print ('\nUnzip Complete.....')
        os.chdir(os.path.normpath(os.getcwd() + os.sep + '..'))
        
    def unrar(self): 
        os.chdir(os.path.normpath(os.getcwd() + os.sep + self.SOURCE_DIRECTORY)) 
        
        if os.name == 'nt':
            rarfile.UNRAR_TOOL = self.UNRAR_PATH
        
        for file in glob.glob(('*.rar')):
            archive_directory = os.path.splitext(file)[0]
            with rarfile.RarFile(file, 'r') as rarObj:
                rarObj.extractall(os.path.normpath(os.getcwd() + os.sep + '..' + os.sep + self.DESTINITION_DIRECTORY + os.sep + archive_directory + '_RAR'))
                
        print ('UnRAR Complete.....')
        os.chdir(os.path.normpath(os.getcwd() + os.sep + '..'))
        
    def boot(self):
        self.unzip()
        self.unrar()