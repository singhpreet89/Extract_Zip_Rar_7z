# UnZIP_UnRAR_application
This tool supports the Extraction of ZIP and RAR files Compressed without a Password and support for files compressed with Password along with ZIP and RAR Compression is coming in the future release.

## Installation
1. Install [Python 3](https://www.python.org/downloads/)
2. Use the package manager [pip](https://pip.pypa.io/en/stable/) to install [rarfile](https://rarfile.readthedocs.io/en/latest/api.html).

```bash
pip install rarfile
```
3. RAR file Compression and Decompression is not directly supported by the [rarfile](https://rarfile.readthedocs.io/en/latest/api.html) library and requires additional downloads depending on the Operating System.

- **For Windows:** Install [WinRAR](https://www.win-rar.com) (Either 32bit or 64bit). The PATH for WinRAR is already provided inside the constructor of ***"extract.py"*** which should suffice most of the Windows users.  Unless you have installed the 32-bit WinRAR on the 64-bit Windows Operating System.
In this case, change the value of UNRAR_PATH in ***"extract.py"*** as follows:

```python
self.UNRAR_PATH = 'C:\\Program Files (x86)\\WinRAR\\UnRAR.exe'
``` 
- **For Mac:**  Install [HomeBrew](https://brew.sh/) and then [unrar](https://www.win-rar.com) as follows:
```bash
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
brew install unrar
``` 
- **For Ubuntu:**  Install [unrar](https://www.win-rar.com) as follows:
```bash
sudo apt-get install -y rar unrar
``` 
## Usage
1. Close the Repository.
2. Install Python 3 and the required packages / libraries listed in the earlier section.
3. Delete the samples(Test files) provided with the repository under the *"archives"* directory and copy all the compressed ***".zip"*** and ***".rar"*** files instead.
    ###### NOTE: A few Samples of normal and corrupted ***".zip"*** and ***".rar"*** files are provided in the ***"archives"*** directory to test the tool for **Extraction** and **Exception handling**.
4. The Decompressed files will be generated under the ***"dumps"*** directory.

## Running the application
Navigate to the **UnZIP_UnRar_application** directory and run the following command:
```bash
python index.py
```
- ###### NOTE: The value for variable ***self.INITIAL_DIRECTORY_NAME*** is equal to ***1*** in the ***"extract.py"*** file which indicates that the first extracted archive will be stored in the directory ***"1"***. Similarly, if 10 archives are extracted 10 new sub-directories will be created under ***"dumps"*** directory with ***names: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10***.    
```python 
self.INITIAL_DIRECTORY_NAME = 1
```
## License
[MIT](https://choosealicense.com/licenses/mit/)
