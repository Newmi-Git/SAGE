import sounddevice as sd
import numpy as np
import wave
import os

sample_rate = 16000
duration = 5

file_path = os.path.join(os.path.dirname(__file__), "recordings","voice.wav")
def recorder():
    print("Speak now...")

    recording = sd.rec(
        int(duration * sample_rate),
        samplerate = sample_rate, 
        channels=1,
        dtype=np.int16
    )

    sd.wait()

    print("Finished Recording")

    with wave.open(file_path, "wb") as file:
        file.setnchannels(1)
        file.setsampwidth(2)
        file.setframerate(sample_rate)
        file.writeframes(recording.tobytes())

    print("saved as wav file")
    print("Full Path:", file_path)