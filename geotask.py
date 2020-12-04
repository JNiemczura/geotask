""" Purpose of this script is to read .txt files containing numerical data, pull out required data
and save it in separate .txt files for better readability """

from pathlib import Path
import os
import re

def inputFilePath():
    """ Asks user for input and validates it. Returns validated absolute path of .txt file """
    inputPath = input(r'Please paste absolute file path: (e.g. C:\Program Files\Stuff\File.txt)') # Ask user for complete file path.
    savedPath = Path(inputPath) # Save given path in variable using Path (for compatibilty).
    while True: # Loop validating given path, returning savedPath if valid.
        if os.path.isabs(inputPath) and savedPath.exists() and savedPath.is_file():  # try/except better?
            return savedPath
        else:
            print('Given path was not an absolute path or non existent one.')
            break

def openFile(Path):
    """ Opens a .txt file and rearranges it into a list of strings (separated by new lines) """
    usedFile = open(Path)
    usedFileLists = usedFile.readlines()
    return usedFileLists

def createSimplifiedFiles(Path, listOfStrings):
    """ Reads through a .txt file looking for 'Input data format: Nr	X	Y	H'
    Create output .txt files based on input .txt data:
    1) Consisting of height measured (IS11.H.09 or similar format - ".H." matching pattern) in format:
    H 	X	Y	H

    2) Consisting of all points measured (both IS11.H.09 and IS11.O.17 - ".H." and ".O." matching pattern) in format:
    X	Y	H

    4) Consisting of names of points measured (both IS11.H.09 and IS11.O.17 - ".H." and ".O." matching pattern) in format:
    Nr	X	Y	H """

    """ Regex objects for searching through files (to be simplified) """
    # heightMeasuredRegex = re.compile(r'IS11\.H\.\d+ (\d+\.\d+) (\d+\.\d+) (\d+\.\d+)')
    allMeasuredRegex = re.compile(r'(.*\.H\.\d+|.*\.O\.\d+) (\d+\.\d+) (\d+\.\d+) (\d+\.\d+)')

    #TRY OPENING ALL 3 FILES FIRST, THEN WHEN LOOPING ADDING STUFF TO ALL 3 OF THEM :)
    heightMeasured = open('HeightMeasured.txt', 'w')
    allPointsMeasured = open('AllPointsMeasured.txt', 'w')
    namesPointsMeasured = open('NamesPointsMeasured.txt', 'w')
    for line in listOfStrings:
        matchingObjects = allMeasuredRegex.findall(line)
        if matchingObjects != []:
            number = matchingObjects[0][0]
            X = matchingObjects[0][1]
            Y = matchingObjects[0][2]
            H = matchingObjects[0][3]
            heightMeasured.write(H + '\t' + X + '\t' + Y + '\t' + H +'\n')
            allPointsMeasured.write(X + '\t' + Y + '\t' + H +'\n')
            namesPointsMeasured.write(number + '\t' + X + '\t' + Y + '\t' + H +'\n')
    heightMeasured.close()
    allPointsMeasured.close()
    namesPointsMeasured.close()

    return print('All files saved successfully.')


userPath = inputFilePath()
textList = openFile(userPath)
createSimplifiedFiles(userPath, textList)



