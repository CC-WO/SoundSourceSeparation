import matplotlib.pyplot as plt
import numpy as np
import wave as wave

sample_wave_file = ".CMU_ARCTIC/cmu_us_aew_arctic/wav/arctic_a0001.wav"
wav = wave.open(sample_wave_file)
data = wav.readframes(wav.getnframes())
data = np.frombuffer(data, dtype=np.int16)

data = data / np.iinfo(np.int16).max

x = np.array(range(wav.getnframes()))/wav.getframerate()

plt.figure(figsize=(10,4))
plt.xlabel("Time [sec]")
plt.ylabel("Value[-1,1]")
plt.plot(x, data)
plt.savefig("./wave_form.png")
plt.show()
