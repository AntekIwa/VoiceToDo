from text_to_speech import Audio
from wake_listener import recognize_speech

audio = Audio()

while True:
    audio.speak("Słucham.")
    cmd = recognize_speech()
    print(">> zwrócone cmd:", cmd)
    if not cmd:
        audio.speak("Nie dosłyszałem.")
        continue
    # dalej logika TODO…
