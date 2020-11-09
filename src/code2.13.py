import numpy as np
import wave as wave
import scipy.signal as sp
import sounddevice as sd
import matplotlib.pyplot as plt


sample_wave_file = ".CMU_ARCTIC/cmu_us_aew_arctic/wav/arctic_a0001.wav"
wav = wave.open(sample_wave_file)
framerate = wav.getframerate()

data = wav.readframes(wav.getnframes())
data = np.frombuffer(data, dtype=np.int16)

f, t, stft_data = sp.stft(data, fs=framerate, window='hann', nperseg=512, noverlap=256)

# LPF
stft_data[:50,:] = 0
# HPF
# stft_data[100:,:] = 0

t, data_post = sp.istft(stft_data, fs=framerate, window="hann", nperseg=512, noverlap=256)

data_post = data_post.astype(np.int16)

sd.play(data_post, framerate)

print("再生開始")

status = sd.wait()

print("再生停止")

wav.close()

fig = plt.figure(figsize=(10,4))

spectrum, freqs, t, im=plt.specgram(data_post, NFFT=512, noverlap=512/16*15, Fs=wav.getframerate(), cmap="gray")

fig.colorbar(im).set_label('Intensity [dB]')

plt.xlabel("Time [sec]")
plt.ylabel("Frequency [Hz]")
plt.savefig("./spectrogram.png")
plt.show()
