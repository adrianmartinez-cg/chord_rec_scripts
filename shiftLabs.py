import os
## SHIFT .LAB FUNCTIONS ############################################

def shiftIntervals(inputFile, outputFile, shift):
    with open(inputFile, 'r') as f:
        lines = f.readlines()   
    with open(outputFile, 'w') as f:
        for line in lines:
            parts = line.strip().split()
            startTime = float(parts[0]) + shift
            endTime = float(parts[1]) + shift
            label = parts[2]
            newLine = f"{startTime:.3f} {endTime:.3f} {label}\n"  # Formatar a linha com 3 casas decimais para os tempos
            f.write(newLine)

def calculateShift(predictedFile, expectedFile):
    # Open and read the first line of the predictedFile
    with open(predictedFile, 'r') as pf:
        predictedFirstLine = pf.readline().strip().split()

    # Open and read the first line of the expectedFile
    with open(expectedFile, 'r') as ef:
        expectedFirstLine = ef.readline().strip().split()
    
    if predictedFirstLine[2] == expectedFirstLine[2]:
        # Extract end times from the lines
        predictedEndTime = float(predictedFirstLine[1])
        expectedEndTime = float(expectedFirstLine[1])
        # Calculate the shift
        shift = predictedEndTime - expectedEndTime
    elif predictedFirstLine[2] == 'N' and expectedFirstLine[2] != 'N':
        shift = float(predictedFirstLine[1])
    elif predictedFirstLine[2] != 'N' and expectedFirstLine[2] == 'N':
        shift = -float(expectedFirstLine[1])
    else:
        print('Debug - Shift 0')
        print(f'Predicted file: {predictedFile}')
        print(f'Predicted first line: {predictedFirstLine}')
        print(f'Expected first line: {expectedFirstLine}')
        shift = 0
    return shift

def shiftFiles(expectedFolder, resultFolder, outputFolder):
    # Create output folder if it doesn't exist
    if not os.path.exists(outputFolder):
        os.makedirs(outputFolder)

    # Iterate over files in the expected folder
    for expectedFile in os.listdir(expectedFolder):
        if os.path.splitext(expectedFile)[1] == ".lab":
            expectedFilePath = os.path.join(expectedFolder, expectedFile)
            resultFilePath = os.path.join(resultFolder, expectedFile)

            # Check if the corresponding file exists in the result folder
            if os.path.exists(resultFilePath):
                # Calculate the shift
                shift = calculateShift(resultFilePath, expectedFilePath)

                # Shift the expected file and save it to the output folder
                outputFilePath = os.path.join(outputFolder, expectedFile)
                shiftIntervals(expectedFilePath, outputFilePath, shift)

rootDir = os.getcwd()
resultsFolder = os.path.join(rootDir,'results','pop909')
expectedLabelsDir = os.path.join(resultsFolder,'expected')
predictedLabelsDir = os.path.join(resultsFolder,'chordino_corrected')
shiftedLabelsDir = os.path.join(resultsFolder,'chordino_shifted')
shiftFiles(predictedLabelsDir,expectedLabelsDir,shiftedLabelsDir)