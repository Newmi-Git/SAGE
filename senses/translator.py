import whisper
import os

def transcribe_small():
    file_path = os.path.join(
        os.path.dirname(__file__),
        "recordings",
        "voice.wav"
    )
    small_model = whisper.load_model("small")
    result = small_model.transcribe(file_path, fp16=False)
    return result['text']


def transcribe_tiny():
    file_path = os.path.join(
        os.path.dirname(__file__),
        "recordings",
        "voice.wav"
    )
    small_model = whisper.load_model("tiny")
    result = small_model.transcribe(file_path, fp16=False)
    return result['text']

def transcribe_base():
    file_path = os.path.join(
        os.path.dirname(__file__),
        "recordings",
        "voice.wav"
    )
    small_model = whisper.load_model("base")
    result = small_model.transcribe(file_path, fp16=False)
    return result['text']

def transcribe_medium():
    file_path = os.path.join(
        os.path.dirname(__file__),
        "recordings",
        "voice.wav"
    )
    small_model = whisper.load_model("medium")
    result = small_model.transcribe(file_path, fp16=False)
    return result['text']


def transcribe_turbo():
    file_path = os.path.join(
        os.path.dirname(__file__),
        "recordings",
        "voice.wav"
    )
    small_model = whisper.load_model("large-v3-turbo")
    result = small_model.transcribe(file_path, fp16=False)
    return result['text']
