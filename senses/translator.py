import whisper
import os

def trancribe_small():
    file_path = os.path.join(
        os.path.dirname(__file__),
        "recordings",
        "voice.wav"
    )
    small_model = whisper.load_model("small")
    result = small_model.transcribe(file_path, fp16=False)
    return result['text']


def trancribe_tiny():
    file_path = os.path.join(
        os.path.dirname(__file__),
        "recordings",
        "voice.wav"
    )
    small_model = whisper.load_model("tiny")
    result = small_model.transcribe(file_path, fp16=False)
    return result['text']

def trancribe_base():
    file_path = os.path.join(
        os.path.dirname(__file__),
        "recordings",
        "voice.wav"
    )
    small_model = whisper.load_model("base")
    result = small_model.transcribe(file_path, fp16=False)
    return result['text']

def trancribe_medium():
    file_path = os.path.join(
        os.path.dirname(__file__),
        "recordings",
        "voice.wav"
    )
    small_model = whisper.load_model("medium")
    result = small_model.transcribe(file_path, fp16=False)
    return result['text']


