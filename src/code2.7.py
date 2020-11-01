import numpy as np
import wave as wave
import sounddevice as sd

wave_length = 5

sample_rate = 16000

print("録音開始")

data = sd.rec(int(wave_length*sample_rate), sample_rate, channels=1)

sd.wait()

print("録音終了")

data_scale_adjust = data * np.iinfo(np.int16).max

data_scale_adjust = data_scale_adjust.astype(np.int16)

wave_out = wave.open("./wgn_wave.wav", "w")

wave_out.setnchannels(1)

wave_out.setsampwidth(2)

wave_out.setframerate(sample_rate)

wave_out.writeframes(data_scale_adjust)

wave_out.close()
