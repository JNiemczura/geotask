""" Purpose of this script is to read .txt files containing numerical data, pull out required data
and save it in separate .txt files for better readability """

from pathlib import Path
import os

def inputFilePath():
    """ Asks user for input and validates it. Returns validated absolute path of .txt file """
    inputPath = input(r'Please paste absolute file path: (e.g. C:\Program Files\Stuff\File.txt)') # Ask user for complete file path.
    savedPath = Path(inputPath) # Save given path in variable using Path (for compatibilty).
    while True: # Loop validating given path, returning savedPath if valid.
        if os.path.isabs(inputPath) and savedPath.exists() and savedPath.is_file():
            return savedPath
        else:
            print('Given path was not an absolute path or non existent one.')
            break

def openFile(Path):
    """ Opens a .txt file and rearranges it into a list of strings (separated by new lines) """
    usedFile = open(Path)
    usedFileLists = usedFile.readlines()
    return usedFileLists



