import os
from midi2audio import FluidSynth

def convert_mid_to_mp3(input_folder, output_folder):
    fs = FluidSynth()

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for file in os.listdir(input_folder):
        if file.endswith(".mid"):
            input_file = os.path.join(input_folder, file)
            output_file = os.path.join(output_folder, file.replace(".mid", ".wav"))

            # Convert .mid to .wav
            fs.midi_to_audio(input_file, output_file)

            # Convert .wav to .mp3
            os.system(f"ffmpeg -i {output_file} {output_file.replace('.wav', '.mp3')}")

            # Remove the .wav file
            os.remove(output_file)

# Use the function
dir = os.getcwd()
convert_mid_to_mp3(
    os.path.abspath(
        os.path.join(dir,'..','repos','BTC-ISMIR19','pop909_audio3')
        ), 
        os.path.abspath(
            os.path.join(dir,'..','repos','BTC-ISMIR19','pop909_audio_mp3')
        )
    )