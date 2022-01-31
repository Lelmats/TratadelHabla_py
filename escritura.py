import numpy as np
import matplotlib.pyplot as plt
from scipy.io.wavfile import write

frecuencia_muestreo = 44100
duracion = 3.0
frecuencia = 200

#amplitud = 32767
amplitud = np.iinfo(np.int16).max

tiempos = np.linspace(0.0, duracion, int(frecuencia_muestreo * duracion))

#f(t) = A sin(2 * pi * f * t)
data = amplitud * np.sin(2 * np.pi * frecuencia * tiempos)

#Frecuencia de muestreo se especifica
#Canales lo saca del shape
#Profundidad de bits del dtype
write("salida.wav", frecuencia_muestreo, data.astype(np.int16))

#transformada = np.fft.fft(data)
transformada = np.fft.rfft(data)

cantidad_muestras = len(data)
periodo_muestreo = 1.0 / frecuencia_muestreo

frecuencias = np.fft.rfftfreq(cantidad_muestras, periodo_muestreo)

plt.figure()
plt.plot(tiempos, data, label = "Canal Mono")
plt.legend()
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")

plt.figure()
plt.plot(frecuencias, np.abs(transformada))
plt.xlabel("Frecuencia (Hz)")
plt.ylabel("Amplitud")

plt.show()