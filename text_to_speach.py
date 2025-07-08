from dotenv import load_dotenv
from elevenlabs.client import ElevenLabs
from elevenlabs import play
import os
load_dotenv()

class Audio:
    def __init__(self, voice_id = "vfaqCOvlrKi4Zp7C2IAm", model_id = "eleven_multilingual_v2"):
        load_dotenv()  # załaduj dane z pliku .env
        api_key = os.getenv("ELEVEN_API_KEY")
        self.client = ElevenLabs(api_key=api_key)
        self.voice_id = voice_id
        self.model_id = model_id

    def speak(self, text):
        audio = self.client.text_to_speech.convert(
            text=text,
            voice_id=self.voice_id,
            model_id=self.model_id,
            output_format="mp3_44100_128"
        )
        play(audio)

    def task_added(self, task):
        self.speak(f"Zadanie '{task}' zostało dodane ... ")

    def ordinal(self, n):
        return {
            1: "Pierwsze",
            2: "Drugie",
            3: "Trzecie",
            4: "Czwarte",
            5: "Piąte"
        }.get(n, f"Zadanie numer {n}")

    def read_list(self, tasks):
        if not tasks:
            self.list_empty()
            return

        spoken = "Oto twoja lista zadań. "
        for i, task in enumerate(tasks, 1):
            spoken += f"{self.ordinal(i)} zadanie. {task}. "
        self.speak(spoken)

ad = Audio()
#ad.task_added("matma")
ad.read_list(["matma", "polski"])

#FF7KdobWPaiR0vkcALHF
#vfaqCOvlrKi4Zp7C2IAm
#QttbagfgqUCm9K0VgUyT
#iK3JGPDhpWyubGKeK29u
