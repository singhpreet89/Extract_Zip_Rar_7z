# UnZIP_UnRAR_application
This tool supports **.zip**, **.rar** and **.7z** extraction.

## New Features!
  - Support for **.7z** extraction added.
  
## Installation & Requirements
1. Install [Python 3](https://www.python.org/downloads/)
2. Use the package manager [pip](https://pip.pypa.io/en/stable/) to install [rarfile](https://rarfile.readthedocs.io/en/latest/api.html), [py7zr](https://pypi.org/project/py7zr/) and [python-dotenv](https://pypi.org/project/python-dotenv/)
```bash
pip install rarfile
pip install py7zr
pip install python-dotenv
```

 3. RAR file extraction use [rarfile](https://rarfile.readthedocs.io/en/latest/api.html) and requires additional dependencyies based on the Operating System.
- **For Windows:** Install [WinRAR](https://www.win-rar.com) (Either 32bit or 64bit). The PATH for WinRAR is already provided as an Environment variable: ***WINDOWS_OS_UNRAR_PATH = C:\\Program Files\\WinRAR\\UnRAR.exe*** in the ***".env"*** file which should work for most Windows OS users unless a 32-bit WinRAR version is installed on the 64-bit Windows Operating System, in this case, change the value of UNRAR_PATH in ***".env"*** as follows:
```bash
WINDOWS_OS_UNRAR_PATH = C:\\Program Files (x86)\\WinRAR\\UnRAR.exe
``` 
- **For Mac:**  Install [HomeBrew](https://brew.sh/) and then [unrar](https://www.win-rar.com) with the following commands:
```bash
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
brew install unrar
``` 
- **For Ubuntu:**  Install [unrar](https://www.win-rar.com) with the following command:
```bash
sudo apt-get install -y rar unrar
``` 
## Usage
1. Clone the Repository.
2. Install all the requirements listed in the earlier section.
3. Delete the samples provided and copy the compressed files into the ***"archives"*** directory.
    ###### NOTE: A few Samples of normal and corrupted **.zip**, **.rar** and **.7z** files are provided in the ***"archives"*** directory to test **Extraction** and **Exception handling**.
4. The ***"extracted"*** directory will contain all the extracted files under their respective sub directories.

## Running the application
Navigate to the **UnZIP_UnRar_application** directory and run the following command:
```bash
python index.py
```
- ###### NOTE: The value for Environment variable: ***INITIAL_DIRECTORY_NAME = 1*** in the ***".env"*** indicates the first extracted archive will be stored in the sub-directory ***"1"*** under ***"extracted"*** directory. Similarly, if 10 archives are extracted to new sub-directories will be created under ***"extracted"*** directory with ***names: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10***.
```bash
INITIAL_DIRECTORY_NAME = 1
```

## License
[MIT](https://choosealicense.com/licenses/mit/)
