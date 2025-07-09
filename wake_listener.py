import sounddevice as sd
import webrtcvad
import numpy as np
import whisper
import scipy.io.wavfile as wav
import tempfile
import os

# Ustawienia
SAMPLE_RATE = 16000
FRAME_DURATION_MS = 30                     # długość jednej ramki w ms
FRAME_SIZE = int(SAMPLE_RATE * FRAME_DURATION_MS / 1000)
MAX_SILENCE_MS = 500                       # po 0.5 s ciszy przerywamy nagranie
vad = webrtcvad.Vad(3)                     # 0–3: 3 = najwyższa czułość
model = whisper.load_model("medium")       # lub "base"/"small"/"large"

def record_until_silence():
    print("🎤 Czekam na początek mowy...")
    stream = sd.InputStream(channels=1,
                            samplerate=SAMPLE_RATE,
                            blocksize=FRAME_SIZE,
                            dtype='int16')
    stream.start()

    # początkowo tylko czekamy, aż usłyszymy mowę
    while True:
        data, _ = stream.read(FRAME_SIZE)
        pcm = data.tobytes()
        if vad.is_speech(pcm, SAMPLE_RATE):
            print("🔊 Mowa wykryta, nagrywanie...")
            break

    # teraz faktyczne buforowanie od pierwszej ramki mowy
    audio_buffer = [data]
    silence_ms = 0

    while True:
        data, _ = stream.read(FRAME_SIZE)
        pcm = data.tobytes()
        is_speech = vad.is_speech(pcm, SAMPLE_RATE)

        if is_speech:
            silence_ms = 0
            print("🔊 mowa")
            audio_buffer.append(data)
        else:
            silence_ms += FRAME_DURATION_MS
            print(f"🤫 cisza ({silence_ms} ms)")
            audio_buffer.append(data)
            if silence_ms > MAX_SILENCE_MS:
                print("⏹️ Koniec nagrania (cisza).")
                break

    stream.stop()
    stream.close()

    recorded = np.concatenate(audio_buffer, axis=0)
    duration = len(recorded) / SAMPLE_RATE
    print(f"🧾 Nagranie zakończone, długość: {duration:.2f}s")

    tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".wav")
    wav.write(tmp.name, SAMPLE_RATE, recorded)
    print("🎧 Zapisano WAV:", tmp.name)
    return tmp.name

def recognize_speech():
    wav_path = record_until_silence()
    print("📥 Rozpoznaję...")
    try:
        res = model.transcribe(wav_path, language="pl", fp16=False)
        text = res["text"].strip()
        print("🧠 Rozpoznano:", repr(text))
    except Exception as e:
        print("❌ Whisper error:", e)
        text = ""
    finally:
        try: os.remove(wav_path)
        except: pass
    return text
