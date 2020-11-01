import numpy as np
import wave as wave
import pyroomacoustics as pa

pa.datasets.CMUArcticCorpus(basedir=".CMU_ARCTIC", download=True, speaker=["aew","axb"])
sample_wave_file = ".CMU_ARCTIC/cmu_us_aew_arctic/wav/arctic_a0001.wav"

wav = wave.open(sample_wave_file)

print("サンプリング周波数[Hz]: ", wav.getframerate())
print("サンプルサイズ[Byte]: ", wav.getsampwidth())
print("サンプル数: ", wav.getnframes())
print("チャンネル数: ", wav.getnchannels())

data = wav.readframes(wav.getnframes())
data = np.frombuffer(data, dtype=np.int16)

wav.close()
