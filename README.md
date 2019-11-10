# compress_extract_tool
The user can Extract the ZIP and RAR files using this tool. At the moment this tool supports only the Extraction of ZIP and RAR files Compressed without a Password. Support for ZIP and RAR Compression, along with Password handling is coming in the future release.

## Installation
1. Install [Python](https://www.python.org/downloads/)
2. Use the package manager [pip](https://pip.pypa.io/en/stable/) to install [rarfile](https://rarfile.readthedocs.io/en/latest/api.html).

```bash
pip install rarfile
```
3. RAR file compression and uncompression is not directly possible with the [rarfile](https://rarfile.readthedocs.io/en/latest/api.html) library and requires additional downloads depending on the Operating System.

- **For Windows:** Install [WinRAR](https://www.win-rar.com) (Either 32bit or 64bit). he PATH for WinRAR is already provided inside the constructor of "extract.py" which should suffice most of the Windows users.  Unless you have installed the 32 bit WinRAR on the 64 bit Windows Operating System, in this case, change the value of UNRAR_PATH in "extract.py" as follows:

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
2. Install all the requirements listed in the earlier section.
3. All the Compressed".zip" and ".rar" files are to be pasted into the "archives" directory.
   NOTE: There are a few Samples of ".zip" and ".rar" files provided along with this tool.
4. The Uncompressed files will be generated under the "dumps" directory.

## Running the application
Navigate to the compress_extract_tool directory and run the following command:
```bash
python index.py
```

## License
[MIT](https://choosealicense.com/licenses/mit/)
