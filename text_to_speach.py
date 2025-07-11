from dotenv import load_dotenv
from elevenlabs.client import ElevenLabs
from elevenlabs import play
import os
load_dotenv()

class Audio:
    def __init__(self, voice_id = "iK3JGPDhpWyubGKeK29u", model_id = "eleven_multilingual_v2"):
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

    def task_exist(self, task):
        self.speak(f"BŁĄD!!! ... Zadanie '{task}' jest już na Twojej liście")

    def task_deleted(self, task):
        self.speak(f"Usunięto zadanie: {task}.")

    def task_not_found(self, task):
        self.speak(f"Nie znaleziono zadania: {task}.")

    def task_index_invalid(self, idx):
        self.speak(f"Zadanie o numerze {idx} nie istnieje.")

    def list_size(self, size):
        if size == 0:
            self.speak("Twoja lista zadań jest pusta!!!")
        elif size == 1:
            self.speak("Na liście jest jedno zadanie.")
        else:
            self.speak(f"Na liście znajduje się {size} zadań.")

    def ordinal(self, n):
        # tylko 1-5 – wystarczy do testów
        return {
            1: "Pierwsze",
            2: "Drugie",
            3: "Trzecie",
            4: "Czwarte",
            5: "Piąte"
        }.get(n, f"Zadanie numer {n}")

    def read_list(self, tasks):
        if not tasks:
            self.list_size(0)
            return

        spoken = "Oto twoja lista zadań. "
        for i, task in enumerate(tasks, 1):
            spoken += f"{self.ordinal(i)} zadanie. {task}. "
        self.speak(spoken)

ad = Audio()
ad.task_exist("matma")
ad.list_size(0)
#ad.read_list(["matma", "polski"])

#FF7KdobWPaiR0vkcALHF
#vfaqCOvlrKi4Zp7C2IAm
#QttbagfgqUCm9K0VgUyT
#iK3JGPDhpWyubGKeK29u
