#Sept 13 2024

#This code make use of openai whisper model for transcription of speech to test, the user enters the full path in the terminal


#Export the your api key by making it an environment variable - to be run on the terminal
    #export OPENAI_API_KEY="your_api_key_here"

#Install the OpenAI SDK with pip - to be run on the terminal
    #pip install openai

#import the openai package 
from openai import OpenAI
client = OpenAI()

#prompt the user for the path to the file
audio_file_user_prompt = input('Provide the full path to the audio file\n')

#open the audio and save the audio file as a binary
audio_file= open(audio_file_user_prompt , "rb")

#use the audio.transcriptions.create to transcribe the audio
transcription = client.audio.transcriptions.create(
    model="whisper-1",
    file= audio_file
)
#print output to terminal
print(transcription.text)