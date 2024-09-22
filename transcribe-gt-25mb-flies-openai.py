#Sept 22 2024

#This code make use of openai whisper model for transcription of speech to test, the user enters the full path in the terminal. This handles files that are greater than 25mb

#Dependencies

    #Export the your api key by making it an environment variable - to be run on the terminal
        #export OPENAI_API_KEY="your_api_key_here"

    #Install the OpenAI SDK with pip - to be run on the terminal
        #pip install openai

    #Install pydub
#import the os and openai package 
import os
from pydub import AudioSegment
from datetime import datetime
from openai import OpenAI
client = OpenAI()
#The slice_audio function’s primary purpose is to take an input audio file and split it into smaller segments of a specified duration (defaulting to 10 minutes), saving each segment as an individual MP3 file in a designated output directory. 
def slice_audio(audio_path, output_dir, slice_duration=10*60*1000): #slices the audio input in 10 minutes segments
    audio = AudioSegment.from_file(audio_path)      # Load the audio file

    # Get the total length of the audio in milliseconds
    audio_length = len(audio)

    # Initialize start and end times
    start_time = 0
    slice_count = 1

    # Create a new directory for sliced files
    now_utc = datetime.now()
    path =  f"{output_dir}/{now_utc}"
    print(path)
    os.mkdir(path)

    while start_time < audio_length:
        end_time = min(start_time + slice_duration, audio_length)  #Ensure not to exceed audio length # the min() function takes the value that is the lowest i.e. start_time + slice_duration = 600000ms or 10 minutes and the audio_lenght is 120000ms or 20 minutes the end_time variable will be 10 minutes 
        audio_slice = audio[start_time:end_time]
        
        #Save the slice
        slice_filename = f"{path}/slice_{slice_count}.mp3"
        audio_slice.export(slice_filename, format="mp3")
        print(f"Saved slice {slice_count} from {start_time} to {end_time} ms")

        # Update for the next slice
        start_time = end_time
        slice_count += 1

    return path


#prompt the user for the path to the file
audio_file_user_prompt = input('Provide the full path to the audio file\n')

# #get the size of the file in bytes
audio_file_size = os.path.getsize(audio_file_user_prompt)

# #convert file size to megabybes - mb
audio_file_size_in_mb = audio_file_size / (1024 * 1024)
print(audio_file_size_in_mb)

#Replace with the directory where sliced files should be saved
#TODO Make to be dynamic 
output_directory = "/replace/with/the/path/to"
#put a condition to only call the slice function if the file is large than 25mb
if (audio_file_size_in_mb >= 25):
    path_to_sliced_audiofiles = slice_audio(audio_file_user_prompt, output_directory)


#Check if the path to the audiofile is not empty if it is empty abort else get the count of the files in the directory
# Check if the directory exists
if os.path.isdir(path_to_sliced_audiofiles):
    file_count = len([file for file in os.listdir(path_to_sliced_audiofiles) if os.path.isfile(os.path.join(path_to_sliced_audiofiles, file))])
    file_names = [file for file in os.listdir(path_to_sliced_audiofiles) if os.path.isfile(os.path.join(path_to_sliced_audiofiles, file))]
    # counter = 0
    # while (counter < file_count):
        
    
    for mp3file in file_names:
        mp3filefullpath = f"{path_to_sliced_audiofiles}/{mp3file}"
        audio_file= open(mp3filefullpath, "rb")

        #use the audio.transcriptions.create to transcribe the audio
        transcription = client.audio.transcriptions.create(
            model="whisper-1",
            file= audio_file  )
        
        with open('output.txt', 'a') as file:
            file.write(transcription.text + '\n')

else:
    print(f"The directory does not exist.")