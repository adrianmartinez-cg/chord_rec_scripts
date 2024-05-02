from chord_extractor.extractors import Chordino
import os
from chord_extractor import LabelledChordSequence

def save(results: LabelledChordSequence):
    # Every time one of the files has had chords extracted, receive the chords here 
    # along with the name of the original file and then run some logic here, e.g. to 
    # save the latest data to DB

    outputFolder = os.path.abspath(os.path.join(dir,os.pardir,os.pardir,'chord_rec_scripts','results','pop909','chordino'))
    filepath = results[0]
    filename = os.path.basename(filepath)
    sequence = results[1]
    labFile = filename.replace(".mp3",".lab") 
    convertToLab(sequence,os.path.join(outputFolder,labFile))
    
def predict(inputFolder,outputFolder):
    for file in os.listdir(inputFolder):
        if file.endswith(".mp3"):
            inputFile = os.path.join(inputFolder, file)
            outputFile = file.replace(".mp3", ".lab")
            chords = chordino.extract(inputFile)
            convertToLab(chords,os.path.join(outputFolder,outputFile))

def convertToLab(chords,labFile):
    initTime = 0
    with open(labFile, 'w') as file:
        for chord in chords:
            chordName = chord[0]
            endTime = chord[1]
            file.write(f"{initTime} {endTime} {chordName}\n")
            initTime = endTime

# Setup Chordino with one of several parameters that can be passed
chordino = Chordino(roll_on=1)
dir = os.getcwd()
filesFolder = os.path.abspath(os.path.join(dir,os.pardir,os.pardir,'pop909mp3','mp3'))
outputFolder = os.path.abspath(os.path.join(dir,os.pardir,os.pardir,'chord_rec_scripts','results','pop909','chordino'))
filesPaths = []
for i in range(1,910):
    mp3File = os.path.join(filesFolder,f"{i:03}.mp3")
    filesPaths.append(mp3File)

res = chordino.extract_many(filesPaths, callback=save, num_extractors=2,
                            num_preprocessors=2, max_files_in_cache=10, stop_on_error=False)