import numpy as np
import wave as wave
import scipy.signal as sp
import sounddevice as sd
import matplotlib.pyplot as plt

sample_wave_file = ".CMU_ARCTIC/cmu_us_aew_arctic/wav/arctic_a0001.wav"
wav = wave.open(sample_wave_file)

n_speech = wav.getnframes()
n_noise_only = 40000
n_sample = n_noise_only + n_speech

sampling_rate = wav.getframerate()

speech_signal = wav.readframes(wav.getnframes())
speech_signal = np.frombuffer(speech_signal, dtype=np.int16)

wgn_signal = np.random.normal(scale=0.04, size=n_sample)
wgn_signal = wgn_signal*np.iinfo(np.int16).max
wgn_signal = wgn_signal.astype(np.int16)

mix_signal = wgn_signal
mix_signal[n_noise_only:]+=speech_signal

f, t, stft_data = sp.stft(mix_signal, fs=sampling_rate, window="hann", nperseg=512, noverlap=256)
amp = np.abs(stft_data)
input_power = np.power(amp, 2.0)

n_noise_only_frame = np.sum(t<(n_noise_only/sampling_rate))

alpha = 1.0
mu = 10

noise_power = np.mean(np.power(amp, 2.0)[:, :n_noise_only_frame], axis=1, keepdims=True)
eps = 0.01 * input_power

processed_power = np.maximum(input_power - alpha * noise_power, eps)
wf_ratio = processed_power / (processed_power + mu * noise_power)
processed_stft_data = wf_ratio * stft_data

t, processed_data_post = sp.istft(processed_stft_data, fs=sampling_rate, window="hann", nperseg=512, noverlap=256)
processed_data_post = processed_data_post.astype(np.int16)

wave_out = wave.open("./process_wave_ss.wav", 'w')
wave_out.setnchannels(1)
wave_out.setsampwidth(2)
wave_out.setframerate(sampling_rate)
wave_out.writeframes(processed_data_post)
wave_out.close()

fig=plt.figure(figsize=(10,4))
spectrum, freqs, t, im = plt.specgram(processed_data_post,NFFT=512, noverlap=512/16*15, Fs=sampling_rate, cmap="gray")
fig.colorbar(im).set_label('Intensity [dB]')
plt.xlabel("Time [sec]")
plt.ylabel("Frequency [Hz]")
plt.savefig("./spectrogram_ss_result.png")
plt.show()

t, data_post = sp.istft(stft_data, fs=sampling_rate, window="hann", nperseg=512, noverlap=256)
data_post = data_post.astype(np.int16)

wave_out = wave.open("./input_wave.wav", 'w')
wave_out.setnchannels(1)
wave_out.setsampwidth(2)
wave_out.setframerate(sampling_rate)
wave_out.writeframes(data_post)
wave_out.close()
wav.close()

fig=plt.figure(figsize=(10,4))
spectrum, freqs, t, im = plt.specgram(data_post, NFFT=512, noverlap=512/16*15, Fs=sampling_rate, cmap="gray")
fig.colorbar(im).set_label('Intensity [dB]')
plt.xlabel("Time [sec]")
plt.ylabel("Frequency [Hz]")
plt.savefig("./spectrogram_noisy.png")
plt.show()
