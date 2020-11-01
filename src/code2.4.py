import matplotlib.pyplot as plt
import numpy as np

n_sample = 40000

sample_rate = 16000

np.random.seed(0)

data = np.random.normal(size=n_sample)

x = np.linspace(0, n_sample/sample_rate, n_sample)

plt.figure(figsize=(10,4))
plt.xlabel("Time [sec]")
plt.ylabel("Value")
plt.plot(x, data)
plt.savefig("./wave_form.png")
plt.show()
