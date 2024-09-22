#Sept 13 2024

#This repo make use of openai whisper model for transcription of speech to test


#Export the your api key by making it an environment variable - to be run on the terminal
    #export OPENAI_API_KEY="your_api_key_here"

#Install the OpenAI SDK with pip - to be run on the terminal
    #pip install openai

#import the openai package 
from openai import OpenAI
client = OpenAI()

#open the audio and save the audio file as a binary
audio_file= open("/replace/with/the/path/to/the/audio/file", "rb")

#use the audio.transcriptions.create to transcribe the audio
transcription = client.audio.transcriptions.create(
    model="whisper-1",
    file= audio_file
)
#print output on terminal
print(transcription.text)