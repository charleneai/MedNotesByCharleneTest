#Sept 22 2024

# Install the Deepgram Python SDK
# https://github.com/deepgram/deepgram-python-sdk

#pip install deepgram-sdk

# Install python-dotenv to protect your API key

#pip install python-dotenv

import os
from dotenv import load_dotenv

from deepgram import (
    DeepgramClient,
    PrerecordedOptions,
    FileSource,
)

#create a .env file and save the api key the variable DG_API_KEY
load_dotenv()

# Path to the audio file
AUDIO_FILE = "song.mp3"

API_KEY = os.getenv("DG_API_KEY")


def main():
    try:
        # STEP 1 Create a Deepgram client using the API key
        deepgram = DeepgramClient(API_KEY)
        with open (AUDIO_FILE, "rb") as file:
            buffer_data = file.read()

        payload: FileSource = {
            "buffer": buffer_data,
        }

        #STEP 2: Configure Deepgram options for audio analysis
        options = PrerecordedOptions(
            model="nova-2",
            smart_format=True
        )

        # STEP 3: Call the transcribe_file method with the text payload and options
        response = deepgram.listen.prerecorded.v("1").transcribe_file(payload, options)

        # STEP 4: Print the response
        print(response.to_json(indent=4))

    except Exception as e:
        print(f"Exception: {e}")


if __name__ == "__main__":
    main()
