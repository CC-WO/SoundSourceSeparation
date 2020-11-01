import numpy as np
import wave as wave
import sounddevice as sd

sample_wave_file = "wgn_wave.wav"
wav = wave.open(sample_wave_file)
data = wav.readframes(wav.getnframes())
data = np.frombuffer(data, dtype=np.int16)

sd.play(data, wav.getframerate())

print("再生開始")

status = sd.wait()

print("再生停止")
