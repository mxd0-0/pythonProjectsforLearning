import numpy as np
from matplotlib import pyplot as plt


# 1. Génération du signal
t = np.arange(0, 1, 0.01)
x = np.sin(2 * np.pi * 5 * t) + 0.5 * np.sin(2 * np.pi * 15 * t) + 0.25 * np.sin(2 * np.pi * 30 * t)

plt.figure()
plt.plot(t, x)
plt.title('Signal composé')
plt.xlabel('Temps')
plt.ylabel('Amplitude')
plt.grid(True)
plt.show()

# 2. Calcul de la FFT
N = len(x)
X = np.fft.fft(x)
f = np.fft.fftfreq(N, d=t[1] - t[0])

plt.figure()
plt.stem(f[:N//2], np.abs(X)[:N//2], use_line_collection=True)
plt.title('Spectre de Fourier')
plt.xlabel('Fréquence (Hz)')
plt.ylabel('Amplitude')
plt.grid(True)
plt.show()

# 3. Étude de la structure FFT (exemple simple avec N=8 pour visualiser)
# Pour un cas éducatif, vous pouvez visualiser les poids manuellement
N_small = 8
x_small = np.sin(2 * np.pi * np.arange(N_small) / N_small)
X_small = np.fft.fft(x_small)
W = np.exp(-2j * np.pi * np.outer(np.arange(N_small), np.arange(N_small)) / N_small)

print("Poids W_{} :".format(N_small))
print(np.round(W, 2))  # Affiche les poids complexes de la FFT

# 4. Filtrage fréquentiel : supprimer les hautes fréquences
X_filtered = X.copy()
X_filtered[15:] = 0  # Supprimer les hautes fréquences (au-delà de 15)
x_filtered = np.fft.ifft(X_filtered)

plt.figure()
plt.plot(t, x_filtered.real)  # On ne garde que la partie réelle
plt.title('Signal filtré (basses fréquences)')
plt.xlabel('Temps')
plt.ylabel('Amplitude')
plt.grid(True)
plt.show()

# 5. Comparaison
plt.figure()
plt.plot(t, x, label='Original')
plt.plot(t, x_filtered.real, label='Filtré', linestyle='--')
plt.title('Comparaison du signal original et filtré')
plt.xlabel('Temps')
plt.ylabel('Amplitude')
plt.legend()
plt.grid(True)
plt.show()
