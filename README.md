# Extract_Zip_Rar_7z
<p align="center">
	<a href="https://www.python.org/" alt="MADE WITH: PYTHON">
		<img src="https://forthebadge.com/images/badges/made-with-python.svg" />
	</a>
</p>
<p align="center">
  <a href="https://www.python.org/downloads/" alt="Powered by: Python 3.8.2">
    <img src="https://badgen.net/badge/Powered%20by/Python%20v3.8.2/3570A0" />
  </a>
  <a href="https://pypi.org/project/pipenv/" alt="Dependency: pipenv">
    <img src="https://badgen.net/badge/pipenv/v2020.5.28/148024" />
  </a>
  <a href="https://pypi.org/project/rarfile/" alt="Dependency: rarfile">
    <img src="https://badgen.net/badge/rarfile/v3.1/148024" />
  </a>
  <a href="https://pypi.org/project/py7zr/" alt="Dependency: py7zr">
    <img src="https://badgen.net/badge/py7zr/v0.6/148024" />
  </a>
  <a href="https://pypi.org/project/python-dotenv/" alt="Dependency: python-dotenv">
    <img src="https://badgen.net/badge/python-dotenv/v0.13.0/148024" />
  </a>
	<a href="https://opensource.org/licenses/MIT" alt="License: MIT">
		<img src="https://img.shields.io/badge/License-MIT-green.svg" />
	</a>
</p>
<p align="center">
  <strong>This tool supports .zip, .rar and .7z extraction.</strong>
</p>
  
## Installation & Requirements
1. Install [Python 3](https://www.python.org/downloads/)
2. Clone the repository.
3. Navigate to the root directory and use the package manager [pip](https://pypi.org/project/pip/) to install [pipenv](https://pypi.org/project/pipenv/)
```bash
pip install pipenv
```
4. Install the required packages defined inside the pipfile.lock file using  [pipenv](https://pypi.org/project/pipenv/):
```bash
pipenv install --ignore-pipfile
```
5. RAR extraction requires installation of an additional package / application:
  - **For Windows:** Install [WinRAR](https://www.win-rar.com) (Either 32-bit or 64-bit). The PATH for WinRAR is already provided in the **.env** file as  **WINDOWS_OS_UNRAR_PATH**, which works for most of the Windows users unless a 32-bit WinRAR version is installed on a 64-bit Windows. 
    * In that case, update the value of WINDOWS_OS_UNRAR_PATH in the **".env"** file as follows:
```bash
WINDOWS_OS_UNRAR_PATH = C:\\Program Files (x86)\\WinRAR\\UnRAR.exe
``` 
  - **For Mac:**  Install [HomeBrew](https://brew.sh/) and [unrar](https://www.win-rar.com) with the following commands:
```bash
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
brew install unrar
``` 
  - **For Ubuntu:**  Install [unrar](https://www.win-rar.com) with the following command:
```bash
sudo apt-get install -y rar unrar
``` 

## Running the application
1. Delete the samples provided in the **"archives"** directory and copy your own compressed files.
 - NOTE: A few Samples of **compressed** and **corrupted & compressed** **.zip**, **.rar** and **.7z** files are provided in the **"archives"** directory to testing. (i.e. **corrupted files** will generate exceptions).
2. Run the following command:
```bash
pipenv run python index.py
```
 - NOTE: The value for Environment variable: **INITIAL_DIRECTORY_NAME = 1** in the **".env"** indicates the first extracted archive will be stored in the sub-directory **"1"** under **"extracted"** directory. Similarly, 10 archives will be extracted into 10 sub-directories under the **"extracted"** directory with **names: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10**.
3. The **"extracted"** directory (created on the fly) will contain all the extracted files.

## License
[MIT](https://choosealicense.com/licenses/mit/)