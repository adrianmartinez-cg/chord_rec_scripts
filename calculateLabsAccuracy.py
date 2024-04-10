import os
import re
import numpy as np
import matplotlib.pyplot as plt
## Chord Functions #####################################################

def getChordsDict():
    return {'11': {'type': 'maj', 'extensions': [5], 'bass': 0},
    '7': {'type': 'maj', 'extensions': [10], 'bass': 0},
    '7(4)': {'type': 'maj', 'extensions': [5, 10], 'bass': 0}, 
    '7/2': {'type': 'maj', 'extensions': [2, 10], 'bass': 2}, 
    '7/3': {'type': 'maj', 'extensions': [10], 'bass': 4}, 
    '7/4': {'type': 'maj', 'extensions': [5, 10], 'bass': 5}, 
    '7/5': {'type': 'maj', 'extensions': [10], 'bass': 7},
    '7/6': {'type': 'maj', 'extensions': [9, 10], 'bass': 9}, 
    '7/b2': {'type': 'maj', 'extensions': [1, 10], 'bass': 1}, 
    '7/b7': {'type': 'maj', 'extensions': [10], 'bass': 10}, 
    '9': {'type': 'maj', 'extensions': [2], 'bass': 0},
    '9(13)': {'type': 'maj', 'extensions': [2, 9], 'bass': 0}, 
    '9/3': {'type': 'maj', 'extensions': [2], 'bass': 4}, 
    '9/5': {'type': 'maj', 'extensions': [2], 'bass': 7}, 
    '9/b7': {'type': 'maj', 'extensions': [2, 10], 'bass': 10},
    'aug': {'type': 'aug', 'extensions': [], 'bass': 0}, 
    'aug(7)': {'type': 'aug', 'extensions': [11], 'bass': 0}, 
    'aug(b7)': {'type': 'aug', 'extensions': [10], 'bass': 0},
    'dim': {'type': 'dim', 'extensions': [], 'bass': 0},  
    'dim/7': {'type': 'dim', 'extensions': [11], 'bass': 11}, 
    'dim/b2': {'type': 'dim', 'extensions': [1], 'bass': 1}, 
    'dim/b3': {'type': 'dim', 'extensions': [], 'bass': 3}, 
    'dim/b5': {'type': 'dim', 'extensions': [], 'bass': 6}, 
    'dim/b7': {'type': 'dim', 'extensions': [10], 'bass': 10},
    'dim7': {'type': 'dim', 'extensions': [10], 'bass': 0},  
    'hdim7': {'type': 'dim', 'extensions': [10], 'bass': 0},
    'hdim7/4': {'type': 'dim', 'extensions': [5, 10], 'bass': 5},
    'hdim7/b3': {'type': 'dim', 'extensions': [10], 'bass': 3},
    'hdim7/b5': {'type': 'dim', 'extensions': [10], 'bass': 6},
    'maj': {'type': 'maj', 'extensions': [], 'bass': 0},
    'maj(11)': {'type': 'maj', 'extensions': [5], 'bass': 0},
    'maj(2)/2': {'type': 'maj', 'extensions': [2], 'bass': 2},
    'maj(4)/4': {'type': 'maj', 'extensions': [5], 'bass': 5},
    'maj(9)': {'type': 'maj', 'extensions': [2], 'bass': 0},
    'maj(9)/3': {'type': 'maj', 'extensions': [2], 'bass': 4},
    'maj(9)/5': {'type': 'maj', 'extensions': [2], 'bass': 7},
    'maj(9)/6': {'type': 'maj', 'extensions': [2, 9], 'bass': 9},
    'maj/#4': {'type': 'maj', 'extensions': [6], 'bass': 6},
    'maj/2': {'type': 'maj', 'extensions': [2], 'bass': 2},
    'maj/3': {'type': 'maj', 'extensions': [], 'bass': 4},
    'maj/4': {'type': 'maj', 'extensions': [5], 'bass': 5}, 
    'maj/5': {'type': 'maj', 'extensions': [], 'bass': 7},
    'maj/6': {'type': 'maj', 'extensions': [9], 'bass': 9},
    'maj/7': {'type': 'maj', 'extensions': [11], 'bass': 11},
    'maj/b2': {'type': 'min', 'extensions': [1], 'bass': 1},
    'maj/b3': {'type': 'maj', 'extensions': [3], 'bass': 3},
    'maj/b6': {'type': 'maj', 'extensions': [8], 'bass': 8},
    'maj/b7': {'type': 'maj', 'extensions': [10], 'bass': 10},
    'maj6': {'type': 'maj', 'extensions': [9], 'bass': 0},
    'maj6(2)/2': {'type': 'maj', 'extensions': [2, 9], 'bass': 2},
    'maj6(7)': {'type': 'maj', 'extensions': [9, 11], 'bass': 0},
    'maj6(9)': {'type': 'maj', 'extensions': [2, 9], 'bass': 0},
    'maj6(9)/3': {'type': 'maj', 'extensions': [2, 9], 'bass': 4},
    'maj6(9)/5': {'type': 'maj', 'extensions': [2, 9], 'bass': 7},
    'maj6(b7)': {'type': 'maj', 'extensions': [9, 10], 'bass': 0},
    'maj6/2': {'type': 'maj', 'extensions': [2, 9], 'bass': 2},
    'maj6/3': {'type': 'maj', 'extensions': [9], 'bass': 4},
    'maj6/4': {'type': 'maj', 'extensions': [5, 9], 'bass': 5}, 
    'maj6/5': {'type': 'maj', 'extensions': [9], 'bass': 0},
    'maj6/6': {'type': 'maj', 'extensions': [9], 'bass': 9},
    'maj7': {'type': 'maj', 'extensions': [11], 'bass': 0},
    'maj7(2)/2': {'type': 'maj', 'extensions': [2, 11], 'bass': 2},
    'maj7(9)/7': {'type': 'maj', 'extensions': [2, 11], 'bass': 11},
    'maj7/2': {'type': 'maj', 'extensions': [2, 11], 'bass': 2},
    'maj7/3': {'type': 'maj', 'extensions': [11], 'bass': 4},
    'maj7/5': {'type': 'maj', 'extensions': [11], 'bass': 7},
    'maj7/7': {'type': 'maj', 'extensions': [11], 'bass': 11},
    'maj9': {'type': 'maj', 'extensions': [2], 'bass': 0},
    'maj9(13)': {'type': 'maj', 'extensions': [2, 9], 'bass': 0},
    'maj9/3': {'type': 'maj', 'extensions': [2], 'bass': 4},
    'min': {'type': 'min', 'extensions': [], 'bass': 0},
    'min6': {'type': 'min', 'extensions': [8], 'bass': 0},
    'min7': {'type': 'min', 'extensions': [10], 'bass': 0},
    'min(11)': {'type': 'min', 'extensions': [5], 'bass': 0},
    'min(2)/2': {'type': 'min', 'extensions': [2], 'bass': 2},
    'min(6)/6': {'type': 'min', 'extensions': [8], 'bass': 8},
    'min(9)': {'type': 'min', 'extensions': [2], 'bass': 0}, 
    'min(9)/5': {'type': 'min', 'extensions': [2], 'bass': 7},
    'min(9)/b3': {'type': 'min', 'extensions': [2], 'bass': 3},
    'min/2': {'type': 'min', 'extensions': [2], 'bass': 2}, 
    'min/4': {'type': 'min', 'extensions': [5], 'bass': 5},
    'min/5': {'type': 'min', 'extensions': [], 'bass': 7},
    'min/6': {'type': 'min', 'extensions': [8], 'bass': 8},
    'min/7': {'type': 'min', 'extensions': [11], 'bass': 11},
    'min/b3': {'type': 'min', 'extensions': [], 'bass': 3},
    'min/b6': {'type': 'min', 'extensions': [8], 'bass': 8},
    'min/b7': {'type': 'min', 'extensions': [10], 'bass': 10},
    'min11': {'type': 'min', 'extensions': [5], 'bass': 0},
    'min11/5': {'type': 'min', 'extensions': [5], 'bass': 7},
    'min11/b3': {'type': 'min', 'extensions': [5], 'bass': 3},
    'min11/b7': {'type': 'min', 'extensions': [5], 'bass': 10},
    'min6(7)': {'type': 'min', 'extensions': [8, 11], 'bass': 0},
    'min6/2': {'type': 'min', 'extensions': [2, 8], 'bass': 2}, 
    'min6/5': {'type': 'min', 'extensions': [8], 'bass': 7},
    'min6/b3': {'type': 'min', 'extensions': [8], 'bass': 3},
    'min7(11)': {'type': 'min', 'extensions': [5, 10], 'bass': 0},
    'min7(13)': {'type': 'min', 'extensions': [9, 10], 'bass': 0},
    'min7(4)/4': {'type': 'min', 'extensions': [5, 10], 'bass': 5},
    'min7(4)/b7': {'type': 'min', 'extensions': [5, 10], 'bass': 10},
    'min7/2': {'type': 'min', 'extensions': [2, 10], 'bass': 2},
    'min7/4': {'type': 'min', 'extensions': [5, 10], 'bass': 5},
    'min7/5': {'type': 'min', 'extensions': [10], 'bass': 7},
    'min7/6': {'type': 'min', 'extensions': [8, 10], 'bass': 8},
    'min7/b2': {'type': 'min', 'extensions': [1, 10], 'bass': 1},
    'min7/b3': {'type': 'min', 'extensions': [10], 'bass': 3},
    'min7/b7': {'type': 'min', 'extensions': [10], 'bass': 10},
    'min9': {'type': 'min', 'extensions': [2], 'bass': 0},
    'min9/5': {'type': 'min', 'extensions': [2], 'bass': 7},
    'min9/b3': {'type': 'min', 'extensions': [2], 'bass': 3},
    'min9/b7': {'type': 'min', 'extensions': [2, 10], 'bass': 10},
    'minmaj7': {'type': 'min', 'extensions': [11], 'bass': 0},
    'minmaj7/7': {'type': 'min', 'extensions': [11], 'bass': 11},
    'sus2': {'type': 'sus', 'extensions': [2], 'bass': 0},
    'sus2(4)': {'type': 'sus', 'extensions': [2, 5], 'bass': 0},
    'sus2(6)': {'type': 'sus', 'extensions': [2, 9], 'bass': 0},
    'sus2/5': {'type': 'sus', 'extensions': [2], 'bass': 7},
    'sus4': {'type': 'sus', 'extensions': [5], 'bass': 0},
    'sus4(9)': {'type': 'sus', 'extensions': [2, 5], 'bass': 0},
    'sus4(b7)': {'type': 'sus', 'extensions': [5, 10], 'bass': 0},
    'sus4(b7)/4': {'type': 'sus', 'extensions': [5, 10], 'bass': 5},
    'sus4(b7)/b7': {'type': 'sus', 'extensions': [5, 10], 'bass': 10},
    'sus4(b7,9)': {'type': 'sus', 'extensions': [2, 5, 10], 'bass': 0},
    'sus4(b7,9,13)': {'type': 'sus', 'extensions': [2, 9, 10], 'bass': 0},
    'sus4/4': {'type': 'sus', 'extensions': [5], 'bass': 5}
    }

def getAllChordLabelsInFolder(labelsFolder):
    chords = {}
    for file in os.listdir(labelsFolder):
        if file.endswith('.lab'):
            with open(os.path.join(labelsFolder,file), "r") as labelFile:
                lines = labelFile.readlines()
            for line in lines:
                _,_,chord = line.split()
                comps = chord.split(":")
                if len(comps) > 1:
                    count = chords.setdefault(comps[1],0)
                    chords[comps[1]] = count + 1
                else:
                    if chord != 'N':
                        count = chords.setdefault('maj',0)
                        chords['maj'] = count + 1
    return chords

def getEnharmonicNotes():
    return {
    'B#': 'C',
    'C#': 'Db',
    'D#': 'Eb',
    'E#': 'F',
    'F#': 'Gb',
    'G#': 'Ab',
    'A#': 'Bb',
    'Cb': 'B',
    'Db': 'C#',
    'Eb': 'D#',
    'Fb': 'E',
    'Gb': 'F#',
    'Ab': 'G#',
    'Bb': 'A#',
    'C': 'C',
    'D': 'D',
    'E': 'E',
    'F': 'F',
    'G': 'G',
    'A': 'A',
    'B': 'B',
    'N': 'N',
    '': ''
    }

def extractChordComponents(chordLabel):
    enharmonicNotes = getEnharmonicNotes()
    # Definir a expressão regular
    pattern = r'([A-Ga-gN][#b]?)(?::(minmaj|min|aug|dim|sus|)(\d*)?)?(?:/\\w+)?'
    
    # Aplicar a expressão regular na string
    result = re.match(pattern, chordLabel)
    
    # Se houver um resultado
    if result:
        root= result.group(1)  
        type = result.group(2)  # Tipo de acorde (opcional)
        extension = result.group(3)  # Extensão do acorde (opcional)
         # Se não houver tipo de acorde, definir como "maj"
        if not type:
            type = "maj"
        
        # Se não houver extensão no acorde, definir como uma string vazia
        if not extension:
            extension = ""
        info = {}
        info['root'] = root
        info['type'] = type
        info['extension'] = extension
        info['alt_root'] = enharmonicNotes[root]
        return info
    else:
        return {'root': '', 'type': '', 'extension': '', 'alt_root': ''}

def compareChords(label1,label2, minRightExtensions = 0.3, relaxType = False):
    #label2 = correct
    chordsDict = getChordsDict()
    enharmonicNotes = getEnharmonicNotes()
    c1comps = label1.split(":")
    c2comps = label2.split(":")
    if len(c1comps) > 1:
        root1, annotation1 = c1comps
    else:
        root1 = c1comps[0]
        annotation1 = 'maj'
    altroot1 = enharmonicNotes[root1]
    if len(c2comps) > 1:
        root2, annotation2 = c2comps
    else:
        root2 = c2comps
        annotation2 = 'maj'
    chord1Components = chordsDict[annotation1]
    chord2Components = chordsDict[annotation2]
    equalTypes = chord1Components['type'] == chord2Components['type']
    equalRoots = root1 == root2 or altroot1 == root2
    chord1extensions = chord1Components['extensions']
    chord2extensions = chord1Components['extensions']
    rightExtensions = 0
    for extension in chord2extensions:
        if extension in chord1extensions:
            rightExtensions += 1
    if len(chord2extensions) > 0:
        rightExtensionsPerc = rightExtensions / len(chord2extensions)
    else:
        rightExtensionsPerc = 1
    equal = True
    if not equalRoots:
        equal = False
    if rightExtensionsPerc < minRightExtensions:
        equal = False
    if not relaxType and not equalTypes:
        equal = False
    return equal

def createChordChart(file_path):
    """
    Creates a chord chart from a generic .lab file.

    Args:
        file_path (str): Path to the .lab file.

    Returns:
        None (Displays the chart using matplotlib).
    """
    # Read data from the .lab file
    with open(file_path, "r") as lab_file:
        lines = lab_file.readlines()

    # Parse time and chord information
    times = []
    chords = []
    for line in lines:
        parts = line.strip().split()
        if len(parts) == 3:
            start_time, end_time, chord = float(parts[0]), float(parts[1]), parts[2]
            times.append(start_time)
            chords.append(chord)

    # Create a plot with colored rectangles and time markers
    fig, ax = plt.subplots(figsize=(10, 4))
    for i in range(len(times) - 1):
        start_time, end_time, chord = times[i], times[i + 1], chords[i]
        ax.add_patch(plt.Rectangle((start_time, 0), end_time - start_time, 1, color="lightblue"))
        ax.text((start_time + end_time) / 2, 0.5, chord, ha="center", va="center", fontsize=6)

        # Add a dashed line for time marker
        ax.plot([end_time, end_time], [0, 1], linestyle="--", color="gray")

    # Configure axes
    ax.set_xlim(0, max(times))
    ax.set_ylim(0, 1)
    ax.set_xlabel("Time")
    ax.set_yticks([])

    # Display the chart
    plt.show()

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

## CALCULATE PRECISION OF LAB FILES FUNCTIONS #########################

def getColoringAccuracy(expectedLabelsFile,predictedLabelsFile,minRightExtensions = 0.3, relaxType = False):
    def readLabelsFromFile(file,addPredictedLabel=False):
        firstTimeInstant = 0
        lastTimeInstant = 0
        with open(file, 'r') as f:
            lines = f.readlines()
            typeFile = 'e' if not addPredictedLabel else 'p'
            for i in range(len(lines)):
                parts = lines[i].strip().split()
                start = float(parts[0])
                end = float(parts[1])
                label = parts[2]
                timeLine.append((end, start, label, typeFile))
                if typeFile == 'e' and start > 0: #has been shifted
                    expectedTimeLine.append((start,0,'N'))
                if typeFile == 'e':
                    expectedTimeLine.append((end,start,label))
                if typeFile == 'p':
                    predictedTimeLine.append((end,start,label))
                if i == 0:
                    firstTimeInstant = start
                if i == len(lines) - 1:
                    lastTimeInstant = end
        return firstTimeInstant,lastTimeInstant
    
    def getCurrentChordInTimeline(time,fileTimeLine):
        chord = ''
        for event in fileTimeLine:
            end,start,label = event
            if time > start and time <= end:
                chord = label
                break
        return chord

    timeLine = []
    expectedTimeLine = []
    predictedTimeLine = []
    startTimeExpected, endTimeExpected = readLabelsFromFile(expectedLabelsFile)
    readLabelsFromFile(predictedLabelsFile,True)
    timeLine.sort()
    fullColoredLength = endTimeExpected - startTimeExpected
    coloredLength = 0
    for i in range(len(timeLine)):
        actualTime = timeLine[i][0]
        if i == 0:
            anteriorTime = timeLine[i][1]
        else:
            anteriorTime = timeLine[i-1][0] 
        if actualTime == 0 and anteriorTime == 0 : continue # nothing to compute
        expectedChordLabel = getCurrentChordInTimeline(actualTime,expectedTimeLine)
        predictedChordLabel = getCurrentChordInTimeline(actualTime,predictedTimeLine)
        if compareChords(predictedChordLabel,expectedChordLabel,minRightExtensions,relaxType):
            coloredLength += actualTime - anteriorTime
    return coloredLength / fullColoredLength


def getMeanColoringAccuracy(expectedFolder, predictedFolder,minRightExtensions=0.3, relaxType = False):
    files_ = []
    for dir, subDir, files in os.walk(expectedFolder):
        for file in files:
            if os.path.splitext(file)[1] == ".lab":
                if os.path.exists(os.path.join(predictedFolder,file)):
                    files_.append((getColoringAccuracy(os.path.join(expectedFolder,file),os.path.join(predictedFolder,file),minRightExtensions,relaxType),file))
    files_.sort(reverse=True)
    return files_,np.mean(np.array([x[0] for x in files_]))

## OTHER ##############################################################

def cleanNames(expectedFolder):
    for dir, subDir, files in os.walk(expectedFolder):
        for file in files:
            if os.path.splitext(file)[1] == ".lab":
                tokens = file.split("_")
                tokens = tokens[2:]
                newFileName = ' '.join(tokens)
                os.rename(os.path.join(expectedFolder,file),os.path.join(expectedFolder,newFileName))

dir = os.getcwd()
expectedLabelsDir = os.path.abspath(os.path.join(dir,'..','resultados','comp_transformer','pop909_expected'))
predictedLabelsDir = os.path.abspath(os.path.join(dir,'..','resultados','comp_transformer','pop909_predicted'))

#chords = ['A', 'A#:min', 'Db', 'Db:minmaj7','F#:aug7', 'F:7','G:dim6','B:min7/b7']
#for c in chords:
    #print(extractChordComponents(c))
#file = "001.lab"
#print(getColoringAccuracy(os.path.join(expectedLabelsDir,file),os.path.join(predictedLabelsDir,file)))

#createChordChart(os.path.join(predictedLabelsDir,file))
#createChordChart(os.path.join(expectedLabelsDir,file))

#'''
files, accuracy = getMeanColoringAccuracy(expectedLabelsDir,predictedLabelsDir)
print(f'####### {len(files)} Files #########')
map = {file[1]:file[0] for file in files if file[0] < 0.6}
print(map)
print('\n####### Accuracy (Expected) #########')
print(accuracy)
#'''

#chords = ['A#','B','B:7','B:min7','A#:minmaj7','C:aug']
#for c in chords:
    #print(extractChordComponents(c))
#shiftFiles(expectedLabelsDir,predictedLabelsDir,'queen_lab_expected_shifted')
#file = "Somebody To Love.lab"
#shiftIntervals(os.path.join(expectedLabelsDir,file),os.path.join(shiftedLabelsDir,file),shift=2.52)