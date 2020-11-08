import matplotlib.pyplot as plt
import numpy as np
import wave as wave
import scipy.signal as sp


sample_wave_file = ".CMU_ARCTIC/cmu_us_aew_arctic/wav/arctic_a0001.wav"
wav = wave.open(sample_wave_file)

data = wav.readframes(wav.getnframes())
data = np.frombuffer(data, dtype=np.int16)

f, t, stft_data = sp.stft(data, fs=wav.getframerate(), window='hann', nperseg=512, noverlap=256)

fig = plt.figure(figsize=(10,4))

spectrum, freqs, t, im=plt.specgram(data, NFFT=512, noverlap=512/16*15, Fs=wav.getframerate(), cmap="gray")

fig.colorbar(im).set_label('Intensity [dB]')

plt.xlabel("Time [sec]")
plt.ylabel("Frequency [Hz]")
plt.savefig("./spectrogram.png")
plt.show()
