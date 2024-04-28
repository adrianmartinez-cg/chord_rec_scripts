import os
import re
import numpy as np
import matplotlib.pyplot as plt
## Chord Functions #####################################################

def getChordsQualities():
  # Work in progress
  return {
      '11': '11',
      '7': '7',
      '7(4)' : '11',
      '7/2' : '9',
      '7/3' : '7',
      '7/4': '11',
      '7/5': '7',
      '7/6': '7(13)',
      '7/b2': '7',
      '7/b7': '7',
      '9' : '9',
      '9(13)' : '9(13)',
      '9/3' : '9',
      '9/5' : '9',
      '9/b7' : '9',
      'aug': 'aug',
      'aug(7)' : 'aug',
      'aug(b7)' : 'aug',
      'dim' : 'dim',
      'dim/7' : 'dim',
      'dim/b2' : 'dim',
      'dim/b3': 'dim',
      'dim/b5': 'dim',
      'dim/b7': 'dim',
      'dim7': 'dim7',
      'hdim7': 'hdim7',
      'hdim7/4': 'hdim7',
      'hdim7/b3': 'hdim7',
      'hdim7/b5': 'hdim7',
      'maj': 'maj',
      'maj(11)' : 'maj(11)',
      'maj(2)/2' : 'maj9',
      'maj(4)/4' : 'maj(11)',
      'maj(9)' : 'maj9',
      'maj(9)/3': 'maj9',
      'maj(9)/5': 'maj9',
      'maj(9)/6': 'maj9(13)',
      'maj/#4': 'maj(#11)',
      'maj/2': 'maj9',
      'maj/3': 'maj',
      'maj/4': 'maj(11)',
      'maj/5': 'maj',
      'maj/6': 'maj6',
      'maj/7': 'maj7',
      'maj/b2': 'maj(b2)',
      'maj/b3': 'maj(b3)',
      'maj/b6': 'maj(b13)',
      'maj/b7': 'maj(b7)',
      'maj6': 'maj6',
      'maj6(2)/2': 'maj9(13)',
      'maj6(7)': 'maj7(13)',
      'maj6(9)': 'maj9(13)',
      'maj6(9)/3': 'maj9(13)',
      'maj6(9)/5': 'maj9(13)',
      'maj6(b7)': '7(13)',
      'maj6/2': 'maj9(13)',
      'maj6/3': 'maj6',
      'maj6/4': 'maj(11)(13)',
      'maj6/5': 'maj6',
      'maj6/6': 'maj6',
      'maj7': 'maj7',
      'maj7(2)/2': 'maj7(9)',
      'maj7(9)/7': 'maj7(9)',
      'maj7/2': 'maj7(9)',
      'maj7/3': 'maj7',
      'maj7/4': 'maj7(11)',
      'maj7/5': 'maj7',
      'maj7/7': 'maj7',
      'maj9': 'maj9',
      'maj9(13)': 'maj9(13)',
      'maj9/3': 'maj9',
      'min': 'min',
      'min6': 'min6',
      'min7': 'min7',
      'min(11)': 'min(11)',
      'min(2)/2': 'min9',
      'min(6)/6': 'min6',
      'min(9)': 'min9',
      'min(9)/5': 'min9',
      'min(9)/b3': 'min9',
      'min/2': 'min9',
      'min/4': 'min(11)',
      'min/5': 'min',
      'min/6': 'min6',
      'min/7': 'min7',
      'min/b3': 'min',
      'min/b6': 'min(b13)',
      'min/b7': 'min7',
      'min11': 'min(11)',
      'min11/5': 'min(11)',
      'min11/b3': 'min(11)',
      'min11/b7': 'min7(11)',
      'min6(7)': 'min7(13)',
      'min6/2': 'min9(13)',
      'min6/5': 'min6',
      'min6/b3': 'min6',
      'min7(11)': 'min7(11)',
      'min7(13)': 'min7(13)',
      'min7(4)/4': 'min7(11)',
      'min7(4)/b7': 'min7(11)',
      'min7/2': 'min7(9)',
      'min7/4': 'min7(11)',
      'min7/5': 'min7',
      'min7/6': 'min7(13)',
      'min7/b2': 'min7',
      'min7/b3': 'min7',
      'min7/b7': 'min7',
      'min9': 'min9',
      'min9/5': 'min9',
      'min9/b3': 'min9',
      'min9/b7': 'min7(9)',
      'minmaj7': 'minmaj7',
      'minmaj7/5': 'minmaj7',
      'minmaj7/7': 'minmaj7',
      'sus2': 'sus2',
      'sus2(4)': 'sus2',
      'sus2(6)': 'sus2',
      'sus2/5': 'sus2',
      'sus4': 'sus4',
      'sus4(9)': 'sus4',
      'sus4(b7)': 'sus4',
      'sus4(b7)/4': 'sus4',
      'sus4(b7)/b7': 'sus4',
      'sus4(b7,9)': 'sus4',
      'sus4(b7,9,13)': 'sus4',
      'sus4/4': 'sus4',
  }

def getChordsNotes():
    return {'11': {'type': 'maj', 'add_notes': [5,10], 'bass': 0},
    '7': {'type': 'maj', 'add_notes': [10], 'bass': 0},
    '7(4)': {'type': 'maj', 'add_notes': [5, 10], 'bass': 0},
    '7/2': {'type': 'maj', 'add_notes': [2, 10], 'bass': 2},
    '7/3': {'type': 'maj', 'add_notes': [10], 'bass': 4},
    '7/4': {'type': 'maj', 'add_notes': [5,10], 'bass': 5},
    '7/5': {'type': 'maj', 'add_notes': [10], 'bass': 7},
    '7/6': {'type': 'maj', 'add_notes': [9,10], 'bass': 9},
    '7/b2': {'type': 'maj', 'add_notes': [1,10], 'bass': 1},
    '7/b7': {'type': 'maj', 'add_notes': [10], 'bass': 10},
    '9': {'type': 'maj', 'add_notes': [2,10], 'bass': 0},
    '9(13)': {'type': 'maj', 'add_notes': [2, 9, 10], 'bass': 0},
    '9/3': {'type': 'maj', 'add_notes': [2,10], 'bass': 4},
    '9/5': {'type': 'maj', 'add_notes': [2,10], 'bass': 7},
    '9/b7': {'type': 'maj', 'add_notes': [2, 10], 'bass': 10},
    'aug': {'type': 'aug', 'add_notes': [], 'bass': 0},
    'aug(7)': {'type': 'aug', 'add_notes': [11], 'bass': 0},
    'aug(b7)': {'type': 'aug', 'add_notes': [10], 'bass': 0},
    'dim': {'type': 'dim', 'add_notes': [], 'bass': 0},
    'dim/7': {'type': 'dim', 'add_notes': [11], 'bass': 11}, #
    'dim/b2': {'type': 'dim', 'add_notes': [1], 'bass': 1},
    'dim/b3': {'type': 'dim', 'add_notes': [], 'bass': 3},
    'dim/b5': {'type': 'dim', 'add_notes': [], 'bass': 6},
    'dim/b7': {'type': 'dim', 'add_notes': [10], 'bass': 10}, #
    'dim7': {'type': 'dim', 'add_notes': [9], 'bass': 0},
    'hdim7': {'type': 'dim', 'add_notes': [10], 'bass': 0},
    'hdim7/4': {'type': 'dim', 'add_notes': [5,10], 'bass': 5},
    'hdim7/b3': {'type': 'dim', 'add_notes': [10], 'bass': 3},
    'hdim7/b5': {'type': 'dim', 'add_notes': [10], 'bass': 6},
    'maj': {'type': 'maj', 'add_notes': [], 'bass': 0},
    'maj(11)': {'type': 'maj', 'add_notes': [5], 'bass': 0},
    'maj(2)/2': {'type': 'maj', 'add_notes': [2], 'bass': 2},
    'maj(4)/4': {'type': 'maj', 'add_notes': [5], 'bass': 5},
    'maj(9)': {'type': 'maj', 'add_notes': [2], 'bass': 0},
    'maj(9)/3': {'type': 'maj', 'add_notes': [2], 'bass': 4},
    'maj(9)/5': {'type': 'maj', 'add_notes': [2], 'bass': 7},
    'maj(9)/6': {'type': 'maj', 'add_notes': [2, 9], 'bass': 9},
    'maj/#4': {'type': 'maj', 'add_notes': [6], 'bass': 6},
    'maj/2': {'type': 'maj', 'add_notes': [2], 'bass': 2},
    'maj/3': {'type': 'maj', 'add_notes': [], 'bass': 4},
    'maj/4': {'type': 'maj', 'add_notes': [5], 'bass': 5},
    'maj/5': {'type': 'maj', 'add_notes': [], 'bass': 7},
    'maj/6': {'type': 'maj', 'add_notes': [9], 'bass': 9},
    'maj/7': {'type': 'maj', 'add_notes': [11], 'bass': 11},
    'maj/b2': {'type': 'min', 'add_notes': [1], 'bass': 1},
    'maj/b3': {'type': 'maj', 'add_notes': [3], 'bass': 3},
    'maj/b6': {'type': 'maj', 'add_notes': [8], 'bass': 8},
    'maj/b7': {'type': 'maj', 'add_notes': [10], 'bass': 10},
    'maj6': {'type': 'maj', 'add_notes': [9], 'bass': 0},
    'maj6(2)/2': {'type': 'maj', 'add_notes': [2, 9], 'bass': 2},
    'maj6(7)': {'type': 'maj', 'add_notes': [9, 11], 'bass': 0},
    'maj6(9)': {'type': 'maj', 'add_notes': [2, 9], 'bass': 0},
    'maj6(9)/3': {'type': 'maj', 'add_notes': [2, 9], 'bass': 4},
    'maj6(9)/5': {'type': 'maj', 'add_notes': [2, 9], 'bass': 7},
    'maj6(b7)': {'type': 'maj', 'add_notes': [9, 10], 'bass': 0},
    'maj6/2': {'type': 'maj', 'add_notes': [2,9], 'bass': 2},
    'maj6/3': {'type': 'maj', 'add_notes': [9], 'bass': 4},
    'maj6/4': {'type': 'maj', 'add_notes': [5,9], 'bass': 5},
    'maj6/5': {'type': 'maj', 'add_notes': [9], 'bass': 7},
    'maj6/6': {'type': 'maj', 'add_notes': [9], 'bass': 9},
    'maj7': {'type': 'maj', 'add_notes': [11], 'bass': 0},
    'maj7(2)/2': {'type': 'maj', 'add_notes': [2, 11], 'bass': 2},
    'maj7(9)/7': {'type': 'maj', 'add_notes': [2, 11], 'bass': 11},
    'maj7/2': {'type': 'maj', 'add_notes': [2,11], 'bass': 2},
    'maj7/3': {'type': 'maj', 'add_notes': [11], 'bass': 4},
    'maj7/5': {'type': 'maj', 'add_notes': [11], 'bass': 7},
    'maj7/7': {'type': 'maj', 'add_notes': [11], 'bass': 11},
    'maj9': {'type': 'maj', 'add_notes': [2], 'bass': 0},
    'maj9(13)': {'type': 'maj', 'add_notes': [2, 9], 'bass': 0},
    'maj9/3': {'type': 'maj', 'add_notes': [2], 'bass': 4},
    'min': {'type': 'min', 'add_notes': [], 'bass': 0},
    'min6': {'type': 'min', 'add_notes': [9], 'bass': 0},
    'min7': {'type': 'min', 'add_notes': [10], 'bass': 0},
    'min(11)': {'type': 'min', 'add_notes': [5], 'bass': 0},
    'min(2)/2': {'type': 'min', 'add_notes': [2], 'bass': 2},
    'min(6)/6': {'type': 'min', 'add_notes': [9], 'bass': 9},
    'min(9)': {'type': 'min', 'add_notes': [2], 'bass': 0},
    'min(9)/5': {'type': 'min', 'add_notes': [2], 'bass': 7},
    'min(9)/b3': {'type': 'min', 'add_notes': [2], 'bass': 3},
    'min/2': {'type': 'min', 'add_notes': [2], 'bass': 2},
    'min/4': {'type': 'min', 'add_notes': [5], 'bass': 5},
    'min/5': {'type': 'min', 'add_notes': [], 'bass': 7},
    'min/6': {'type': 'min', 'add_notes': [9], 'bass': 9},
    'min/7': {'type': 'min', 'add_notes': [11], 'bass': 11},
    'min/b3': {'type': 'min', 'add_notes': [], 'bass': 3},
    'min/b6': {'type': 'min', 'add_notes': [8], 'bass': 8},
    'min/b7': {'type': 'min', 'add_notes': [10], 'bass': 10},
    'min11': {'type': 'min', 'add_notes': [5], 'bass': 0},
    'min11/5': {'type': 'min', 'add_notes': [5], 'bass': 7},
    'min11/b3': {'type': 'min', 'add_notes': [5], 'bass': 3},
    'min11/b7': {'type': 'min', 'add_notes': [5,10], 'bass': 10},
    'min6(7)': {'type': 'min', 'add_notes': [9, 10], 'bass': 0},
    'min6/2': {'type': 'min', 'add_notes': [2,9], 'bass': 2},
    'min6/5': {'type': 'min', 'add_notes': [9], 'bass': 7},
    'min6/b3': {'type': 'min', 'add_notes': [9], 'bass': 3},
    'min7(11)': {'type': 'min', 'add_notes': [5, 10], 'bass': 0},
    'min7(13)': {'type': 'min', 'add_notes': [9, 10], 'bass': 0},
    'min7(4)/4': {'type': 'min', 'add_notes': [5, 10], 'bass': 5},
    'min7(4)/b7': {'type': 'min', 'add_notes': [5, 10], 'bass': 10},
    'min7/2': {'type': 'min', 'add_notes': [2,10], 'bass': 2},
    'min7/4': {'type': 'min', 'add_notes': [5,10], 'bass': 5},
    'min7/5': {'type': 'min', 'add_notes': [10], 'bass': 7},
    'min7/6': {'type': 'min', 'add_notes': [9,10], 'bass': 9},
    'min7/b2': {'type': 'min', 'add_notes': [1,10], 'bass': 1},
    'min7/b3': {'type': 'min', 'add_notes': [10], 'bass': 3},
    'min7/b7': {'type': 'min', 'add_notes': [10], 'bass': 10},
    'min9': {'type': 'min', 'add_notes': [2], 'bass': 0},
    'min9/5': {'type': 'min', 'add_notes': [2], 'bass': 7},
    'min9/b3': {'type': 'min', 'add_notes': [2], 'bass': 3},
    'min9/b7': {'type': 'min', 'add_notes': [2,10], 'bass': 10},
    'minmaj7': {'type': 'min', 'add_notes': [11], 'bass': 0},
    'minmaj7/5': {'type': 'min', 'add_notes': [11], 'bass': 7},
    'minmaj7/7': {'type': 'min', 'add_notes': [11], 'bass': 11},
    'sus2': {'type': 'sus', 'add_notes': [2], 'bass': 0}, #sus: tonica, quinta (sem terca)
    'sus2(4)': {'type': 'sus', 'add_notes': [2, 5], 'bass': 0},
    'sus2(6)': {'type': 'sus', 'add_notes': [2, 9], 'bass': 0},
    'sus2/5': {'type': 'sus', 'add_notes': [2], 'bass': 7},
    'sus4': {'type': 'sus', 'add_notes': [5], 'bass': 0},
    'sus4(9)': {'type': 'sus', 'add_notes': [2, 5], 'bass': 0},
    'sus4(b7)': {'type': 'sus', 'add_notes': [5, 10], 'bass': 0},
    'sus4(b7)/4': {'type': 'sus', 'add_notes': [5, 10], 'bass': 5},
    'sus4(b7)/b7': {'type': 'sus', 'add_notes': [5, 10], 'bass': 10},
    'sus4(b7,9)': {'type': 'sus', 'add_notes': [2, 5, 10], 'bass': 0},
    'sus4(b7,9,13)': {'type': 'sus', 'add_notes': [2, 5, 9, 10], 'bass': 0},
    'sus4/4': {'type': 'sus', 'add_notes': [5], 'bass': 5}
    }


def extractAnnotation(chordLabel):
  comps = chordLabel.split(":")
  if len(comps) > 1:
    _,annotation = comps
  else:
    annotation = 'maj'
  return annotation

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

def compareExtensions(predictedExtensions, expectedExtensions):
    if len(expectedExtensions) == 0:
        # for len = 0,1,2 : scores 1 ,0.5, 0.25 
        return 2 ** (-len(predictedExtensions))
    expectedExtensions = set(expectedExtensions)
    predictedExtensions = set(predictedExtensions)

    # Calculate intersection and difference
    correct = expectedExtensions.intersection(predictedExtensions)
    incorrect = predictedExtensions.difference(expectedExtensions)
    missing = expectedExtensions.difference(predictedExtensions)

    # Calculates score
    score = len(correct) / (len(correct) + len(incorrect) + len(missing))

    return score

def jaccardScore(predictedChordInfo, expectedChordInfo):
   basicStructure = {'maj': set([0,4,7]), 
                     'min': set([0,3,7]), 
                     'aug': set([0,4,8]), 
                     'dim': set([0,3,6]), 
                     'sus': set([0,7])}
   predictedChordAddNotes = set(predictedChordInfo['add_notes'])
   predictedChordBasicNotes = basicStructure[predictedChordInfo['type']]
   predictedChordNotes = predictedChordAddNotes.union(predictedChordBasicNotes)
   expectedChordAddNotes = set(expectedChordInfo['add_notes'])
   expectedChordBasicNotes = basicStructure[expectedChordInfo['type']]
   expectedChordNotes = expectedChordAddNotes.union(expectedChordBasicNotes)

   intersection = predictedChordNotes.intersection(expectedChordNotes)
   union = predictedChordNotes.union(expectedChordNotes)
   print(f'Jaccard between {sorted(list(predictedChordNotes))} {sorted(list(expectedChordNotes))}: {len(intersection) / len(union)}')
   return len(intersection) / len(union)


def compareChords(predictedLabel,expectedLabel, errorsDict,successDict,minScore = 0.3, relaxType = False):
    chordsDict = getChordsNotes()
    enharmonicNotes = getEnharmonicNotes()
    predictedChordComponents = predictedLabel.split(":")
    expectedChordComponents = expectedLabel.split(":")
    if len(predictedChordComponents) > 1:
        rootPredicted, annotationPredicted = predictedChordComponents
    else:
        rootPredicted = predictedChordComponents[0]
        annotationPredicted = 'maj'
    altrootPredicted = enharmonicNotes[rootPredicted]
    if len(expectedChordComponents) > 1:
        rootExpected, annotationExpected = expectedChordComponents
    else:
        rootExpected = expectedChordComponents[0]
        annotationExpected = 'maj'
    predictedChordInfo = chordsDict[annotationPredicted]
    expectedChordInfo = chordsDict[annotationExpected]
    equalTypes = predictedChordInfo['type'] == expectedChordInfo['type']
    equalRoots = rootPredicted == rootExpected or altrootPredicted == rootExpected
    predictedChordExtensions = predictedChordInfo['add_notes']
    expectedChordExtensions = expectedChordInfo['add_notes']
    #extensionsScore = compareExtensions(predictedChordExtensions,expectedChordExtensions)
    extensionsScore = jaccardScore(predictedChordInfo,expectedChordInfo)
    equal = True
    if not equalRoots:
        equal = False
    if not relaxType and not equalTypes:
        equal = False
    if extensionsScore < minScore:
        equal = False
    if not equal:
        if expectedLabel not in errorsDict:
            errorsDict[expectedLabel] = [predictedLabel]
        else:
            errorsDict[expectedLabel].append(predictedLabel)
    else:
      if expectedLabel not in successDict:
        successDict[expectedLabel] = 1
      else:
        successDict[expectedLabel] += 1
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
        ax.text((start_time + end_time) / 2, 0.5, chord, ha="center", va="center", fontsize=10)

        # Add a dashed line for time marker
        ax.plot([end_time, end_time], [0, 1], linestyle="--", color="gray")

    # Configure axes
    ax.set_xlim(0, max(times))
    ax.set_ylim(0, 1)
    ax.set_xlabel("Time")
    ax.set_yticks([])

    # Display the chart
    plt.show()

## CALCULATE PERFORMANCE OF LAB FILES FUNCTIONS #########################

def getPerformance(expectedLabelsFile,predictedLabelsFile,errorsDict,successDict,minScore = 0.3, relaxType = False):
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
    startTimePredicted, endTimePredicted = readLabelsFromFile(predictedLabelsFile,True)
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
        if compareChords(predictedChordLabel,expectedChordLabel,errorsDict,successDict,minScore,relaxType):
            coloredLength += actualTime - anteriorTime
    recall = coloredLength / fullColoredLength
    precision = coloredLength / (endTimePredicted - startTimePredicted)
    f1 = (2*precision*recall) / (precision + recall)
    return {'recall': recall , 'precision': precision , 'f1': f1}


def getMeanPerformance(expectedFolder, predictedFolder,errorsDict,successDict,minScore=0.3, relaxType = False):
    files_ = []
    for dir, subDir, files in os.walk(expectedFolder):
        for file in files:
            if os.path.splitext(file)[1] == ".lab":
                if os.path.exists(os.path.join(predictedFolder,file)):
                    performance = getPerformance(os.path.join(expectedFolder,file),os.path.join(predictedFolder,file),errorsDict,successDict,minScore,relaxType)
                    files_.append((performance,file))
    sortedFiles = sorted(files_,key=lambda x: x[0]['f1'], reverse=True)
    return sortedFiles

## OTHER ##############################################################

def getTypeErrors(errorsDict):
    def countRepetitions(elem):
      map = {}
      map['count'] = len(elem)
      for annotation in elem:
        if annotation not in map:
          map[annotation] = 1
        else:
          map[annotation] += 1
      return map

    chordQualities = getChordsQualities()
    annotationsDictKeys = []
    annotationsDict = {}
    countingDict = {}
    simplifiedCountingDict = {}
    for key in errorsDict:
        if extractAnnotation(key) not in annotationsDict:
          annotationsDict[extractAnnotation(key)] = []
        for elem in errorsDict[key]:
            annotationsDict[extractAnnotation(key)].append(extractAnnotation(elem))
    for key in annotationsDict:
      annotationsDictKeys.append(key)
      annotationsDict[key] = countRepetitions(annotationsDict[key])
    annotationsDictKeys.sort()
    for key in annotationsDictKeys:
      countingDict[key] = annotationsDict[key]
    for key in countingDict:
      temp = {}
      subtract = 0
      for elem in countingDict[key]:
        if elem != key:
          temp[elem] = countingDict[key][elem]
        else:
          subtract = countingDict[key][elem]
      count = countingDict[key]['count'] - subtract
      countingDict[key] = temp
      countingDict[key]['count'] = count
    for key in countingDict:
      for elem in countingDict[key]:
        if elem == 'count': continue
        if chordQualities[key] not in simplifiedCountingDict: simplifiedCountingDict[chordQualities[key]] = {}
        if chordQualities[elem] not in simplifiedCountingDict[chordQualities[key]]: simplifiedCountingDict[chordQualities[key]][chordQualities[elem]] = 0
        simplifiedCountingDict[chordQualities[key]][chordQualities[elem]] += countingDict[key][elem]
      simplifiedCountingDict[chordQualities[key]]['count'] = 0
      for elem in simplifiedCountingDict[chordQualities[key]]:
        if elem != 'count':
          simplifiedCountingDict[chordQualities[key]]['count'] += simplifiedCountingDict[chordQualities[key]][elem]
    return countingDict,simplifiedCountingDict

def simplifySuccessDict(successDict):
  simplified = {}
  chordQualities = getChordsQualities()
  for key in successDict:
    if chordQualities[extractAnnotation(key)] not in simplified:
      simplified[chordQualities[extractAnnotation(key)]] = successDict[key]
    else:
      simplified[chordQualities[extractAnnotation(key)]] += successDict[key]
  return simplified

rootDir = os.getcwd()
resultsFolder = os.path.join(rootDir,'results','pop909')
expectedLabelsDir = os.path.join(resultsFolder,'expected')
modelFolder = 'btc-ismir19'
predictedLabelsDir = os.path.join(resultsFolder,modelFolder)
errorsDict = {}
successDict = {}
minScore = 0

'''
files = getMeanPerformance(expectedLabelsDir,predictedLabelsDir,errorsDict,successDict,minScore)
print(f'## {len(files)} Files ##')
map = {file[1]:file[0]['f1'] for file in files if file[0]['f1'] < 0.6}
print(map)
print('\n## Metrics ##')
metrics = getMeanMetrics(files)
print(f'Precision: {metrics["precision"]}')
print(f'Recall: {metrics["recall"]}')
print(f'F1: {metrics["f1"]}')
#'''

#createChordChart(os.path.join(dir,'example1.lab'))
#createChordChart(os.path.join(dir,'example2.lab'))

#chords = ['A#','B','B:7','B:min7','A#:minmaj7','C:aug']
#for c in chords:
    #print(extractChordComponents(c))
#shiftFiles(expectedLabelsDir,predictedLabelsDir,'queen_lab_expected_shifted')
#file = "Somebody To Love.lab"
#shiftIntervals(os.path.join(expectedLabelsDir,file),os.path.join(shiftedLabelsDir,file),shift=2.52)


####################### Test Cases
'''
testCasesFolder = 'test_cases_lab'
testCasesExpected = os.path.join(dir,testCasesFolder,'expected')
testCasesPredicted = os.path.join(dir,testCasesFolder,'predicted')
file = '4.lab'
expectedFile = os.path.join(testCasesExpected,file)
predictedFile = os.path.join(testCasesPredicted,file)
testErrorsDict = {}
testSuccessDict = {}
testAcc = getPerformance(expectedFile,predictedFile,testErrorsDict,testSuccessDict,0)
print(f'Min Score [0] Accuracy: {testAcc}')

testAcc = getPerformance(expectedFile,predictedFile,testErrorsDict,testSuccessDict,0.25)
print(f'Min Score [0.25] Accuracy: {testAcc}')

testAcc = getPerformance(expectedFile,predictedFile,testErrorsDict,testSuccessDict,0.5)
print(f'Min Score [0.5] Accuracy: {testAcc}')

testAcc = getPerformance(expectedFile,predictedFile,testErrorsDict,testSuccessDict,1)
print(f'Min Score [1] Accuracy: {testAcc}')
'''

majchords = []
all = getChordsNotes()
for c in all:
   if all[c]['type'] == 'maj':
      majchords.append(c)
print(majchords)
for c in majchords:
  jaccardScore(all[c],all["maj"])