import numpy as np
import wave as wave
import scipy.signal as sp


sample_wave_file = ".CMU_ARCTIC/cmu_us_aew_arctic/wav/arctic_a0001.wav"
wav = wave.open(sample_wave_file)

data = wav.readframes(wav.getnframes())
data = np.frombuffer(data, dtype=np.int16)

f, t, stft_data = sp.stft(data, fs=wav.getframerate(), window='hann', nperseg=512, noverlap=256)

print("短時間フーリエ変換後のsahpe: ", np.shape(stft_data))
print("周波数軸[Hz]", f)
print("時間軸[sec]", t)
