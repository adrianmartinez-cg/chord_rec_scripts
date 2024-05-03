import os
import re

def splitRoot(label):
    extract = r'([A-Z](?:#|b)?)(.*)'
    parts = re.split(extract, label, maxsplit=2)
    root = parts[1]
    after = parts[2]
    return root,after

def splitRootInFolder(labelsFolder):
    roots = set()
    after = set()
    extract = r'([A-Z](?:#|b)?)(.*)'
    for file in os.listdir(labelsFolder):
        if file.endswith('.lab'):
            with open(os.path.join(labelsFolder,file), "r") as labelFile:
                lines = labelFile.readlines()
            for line in lines:
                _,_,chord = line.split()
                if chord != 'N':
                    parts = re.split(extract, chord, maxsplit=2)
                    roots.add(parts[1])
                    after.add(parts[2])
    return roots,after

def getChordsNotes():
    return {'N': {'type': 'none', 'add_notes': [], 'bass': 0},
    '11': {'type': 'maj', 'add_notes': [5,10], 'bass': 0},
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
    'maj7/4': {'type': 'maj', 'add_notes': [5,11], 'bass': 5},
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


def getChordinoNotes(root,after):
   
   datasetChords = getChordsNotes()
   referenceFrame = {
      '': 0,
      'A': 0,
      'A#': 1,
      'Bb': 1,
      'B': 2,
      'C': 3,
      'C#': 4,
      'Db': 4,
      'D': 5,
      'D#': 6,
      'Eb': 6,
      'E': 7,
      'F': 8,
      'F#': 9,
      'Gb': 9,
      'G': 10,
      'G#': 11,
      'Ab': 11
   }
   untreatedChordInfo = {
        #hdim, maj, 7
        '': {'type': 'maj', 'add_notes': [], 'bass': '', 'label': 'maj'},
        'm7b5/Db': {'type': 'dim', 'add_notes': [10], 'bass': 'Db', 'label': 'hdim7'},
        '/C#': {'type': 'maj', 'add_notes': [], 'bass': 'C#', 'label': 'maj'},
        'm7b5/Eb': {'type': 'dim', 'add_notes': [10], 'bass': 'Eb', 'label': 'hdim7'},
        'm7b5/B': {'type': 'dim', 'add_notes': [10], 'bass': 'B', 'label': 'hdim7'},
        'm6': {'type': 'min', 'add_notes': [9], 'bass': '', 'label': 'min6'},
        'm7b5': {'type': 'dim', 'add_notes': [10], 'bass': '', 'label': 'hdim7'},
        '7/A': {'type': 'maj', 'add_notes': [10], 'bass': 'A', 'label': '7'},
        '/B': {'type': 'maj', 'add_notes': [], 'bass': 'B', 'label': 'maj'},
        '7': {'type': 'maj', 'add_notes': [10], 'bass': '', 'label': '7'},
        '/Bb': {'type': 'maj', 'add_notes': [], 'bass': 'Bb', 'label': 'maj'},
        '7/C': {'type': 'maj', 'add_notes': [10], 'bass': 'C', 'label': '7'},
        '/D#': {'type': 'maj', 'add_notes': [], 'bass': 'D#', 'label': 'maj'},
        'm7': {'type': 'min', 'add_notes': [10], 'bass': '', 'label': 'min7'},
        'maj7': {'type': 'maj', 'add_notes': [11], 'bass': '', 'label': 'maj7'},
        'm7b5/E': {'type': 'dim', 'add_notes': [10], 'bass': 'E', 'label': 'hdim7'},
        '/C': {'type': 'maj', 'add_notes': [], 'bass': 'C', 'label': 'maj'},
        'm7b5/Ab': {'type': 'dim', 'add_notes': [10], 'bass': 'Ab', 'label': 'hdim7'},
        '7/B': {'type': 'maj', 'add_notes': [10], 'bass': 'B', 'label': '7'},
        '7/D': {'type': 'maj', 'add_notes': [10], 'bass': 'D', 'label': '7'},
        '/Ab': {'type': 'maj', 'add_notes': [], 'bass': 'Ab','label': 'maj'},
        'aug': {'type': 'aug', 'add_notes': [], 'bass': '', 'label': 'aug'},
        '7/D#': {'type': 'maj', 'add_notes': [10], 'bass': 'D#', 'label': '7'},
        '/G': {'type': 'maj', 'add_notes': [], 'bass': 'G', 'label': 'maj'},
        'm': {'type': 'min', 'add_notes': [], 'bass': '', 'label': 'min'},
        'm7b5/C': {'type': 'dim', 'add_notes': [10], 'bass': 'C', 'label': 'hdim7'},
        'm7b5/Bb': {'type': 'dim', 'add_notes': [10], 'bass': 'Bb', 'label': 'hdim7'},
        '/A#': {'type': 'maj', 'add_notes': [], 'bass': 'A#', 'label': 'maj'},
        'dim': {'type': 'dim', 'add_notes': [], 'bass': '', 'label': 'dim'},
        '7/A#': {'type': 'maj', 'add_notes': [10], 'bass': 'A#', 'label': '7'},
        '/D': {'type': 'maj', 'add_notes': [], 'bass': 'D', 'label': 'maj'},
        '/F': {'type': 'maj', 'add_notes': [], 'bass': 'F', 'label': 'maj'},
        '7/G#': {'type': 'maj', 'add_notes': [10], 'bass': 'G#', 'label': '7'},
        '/Db': {'type': 'maj', 'add_notes': [], 'bass': 'Db', 'label': 'maj'},
        'm7b5/D': {'type': 'dim', 'add_notes': [10], 'bass': 'D', 'label': 'hdim7'},
        '7/F#': {'type': 'maj', 'add_notes': [10], 'bass': 'F#', 'label': '7'},
        '7/G': {'type': 'maj', 'add_notes': [10], 'bass': 'G', 'label': '7'},
        'm7b5/F': {'type': 'dim', 'add_notes': [10], 'bass': 'F', 'label': 'hdim7'},
        'm7b5/G': {'type': 'dim', 'add_notes': [10], 'bass': 'G', 'label': 'hdim7'},
        '7/C#': {'type': 'maj', 'add_notes': [10], 'bass': 'C#', 'label': '7'},
        'm7b5/Gb': {'type': 'dim', 'add_notes': [10], 'bass': 'Gb', 'label': 'hdim7'},
        '/Eb': {'type': 'maj', 'add_notes': [], 'bass': 'Eb', 'label': 'maj'},
        '6': {'type': 'maj', 'add_notes': [9], 'bass': '', 'label': 'maj6'},
        '/A': {'type': 'maj', 'add_notes': [10], 'bass': 'A', 'label': 'maj'},
        '/E#': {'type': 'maj', 'add_notes': [10], 'bass': 'F', 'label': 'maj'},
        '7/E#': {'type': 'maj', 'add_notes': [10], 'bass': 'F', 'label': '7'},
        '/G#': {'type': 'maj', 'add_notes': [10], 'bass': 'G#', 'label': 'maj'},
        '7/E': {'type': 'maj', 'add_notes': [10], 'bass': 'E', 'label': '7'},
        'm7b5/A': {'type': 'dim', 'add_notes': [10], 'bass': 'A', 'label': 'hdim7'},
   }

   bassNotation = {
       2: '2',
       3: 'b3',
       4: '3',
       5: '4',
       6: 'b5',
       7: '5',
       8: 'b6',
       9: '6',
       10: 'b7',
       11: '7'
   }

   chordInfo = untreatedChordInfo[after]
   basicLabel = chordInfo['label']
   bass = chordInfo['bass']
   chordLabel = basicLabel
   if bass != '':
    referenceBass = referenceFrame[bass]
    referenceRoot = referenceFrame[root]
    relativeBass = (referenceBass - referenceRoot) % 12
    chordInfo['bass'] = relativeBass
    chordBass = bassNotation[relativeBass]
    completeLabel = basicLabel + f"/{chordBass}"
    if completeLabel in datasetChords:
        chordLabel = completeLabel
    else:
        if relativeBass == 6:
            altLabel = basicLabel + "/#4"
            if altLabel in datasetChords:
                chordLabel = altLabel
   return chordInfo , chordLabel

def correctNotation(labelsFolder,saveFolder):
    for file in os.listdir(labelsFolder):
        if file.endswith('.lab'):
            with open(os.path.join(labelsFolder,file),'r') as originalLab:
                with open(os.path.join(saveFolder,file), 'w') as newLab:
                    for line in originalLab:
                        init,end,chord = line.split()
                        if chord != 'N':
                            root, after = splitRoot(chord)
                            info, label = getChordinoNotes(root,after)
                            correctedChord = f"{root}:{label}"
                            chord = correctedChord
                        newLab.write(f"{init} {end} {chord}\n")

rootDir = os.getcwd()
resultsFolder = os.path.join(rootDir,'results','pop909')
expectedLabelsDir = os.path.join(resultsFolder,'expected')
modelFolder = 'chordino'
predictedLabelsDir = os.path.join(resultsFolder,modelFolder)
correctedLabelsDir = os.path.join(resultsFolder,'chordino_corrected')

'''
roots,after = splitRoot(predictedLabelsDir)
print("roots: ")
for r in roots:
   print(r)
print("after: ")
for a in after:
   print(f"'{a}'")
'''
correctNotation(predictedLabelsDir, correctedLabelsDir)