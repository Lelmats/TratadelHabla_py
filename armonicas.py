from cProfile import label
import numpy as np
import matplotlib.pyplot as plt
from scipy.io.wavfile import write

frecuencia_muestreo = 44100
frecuencia = 440
tiempos = np.linspace(0.0, 1.0, frecuencia_muestreo)
amplitud = np.iinfo(np.int16).max

ciclos = frecuencia * tiempos

fracciones, enteros = np.modf(ciclos)
data = fracciones

data = fracciones - 0.5

data = np.abs(data)

data = data - data.mean()

alto, bajo = abs(max(data)), abs(min(data))
data = amplitud * data / max(alto, bajo)

plt.figure()
plt.plot(tiempos, data)
# plt.show()

write("triangular.wav", frecuencia_muestreo, data.astype(np.int16))

cantidad_muestras = len(data)
periodo_muestreo = 1.0 / frecuencia_muestreo
transformada = np.fft.rfft(data)
frecuencias = np.fft.rfftfreq(cantidad_muestras, periodo_muestreo)

plt.figure()
plt.plot(frecuencias, np.abs(transformada))
# plt.show()

# 1.- Obtener en Hz las frecuencias de los armoicos de la señal

armonicos = frecuencias[transformada > 150000]
print(armonicos)

# 2.- Aplicarle un filtro pasa bajas que solo deje pasar la Freq Fundamental 
# y luego aplicarle la transformada inversa
# graficarla en dominio del tiempo
# y crear un archivo wav para escucharla

pasa_bajas = transformada.copy()
pasa_bajas[frecuencias > (frecuencia + 5)] *=0

plt.figure()
plt.plot(frecuencias, np.abs(pasa_bajas), label = "Pasa bajas")
plt.xlabel("Frecuencia (Hz)")
plt.ylabel ("Amplitud")
plt.legend()
# plt.show

pasa_bajas_data = np.fft.irfft(pasa_bajas)
plt.figure()
plt.plot(tiempos, pasa_bajas_data)
plt.legend()
plt.xlabel("Tiempo (seg.)")
plt.ylabel ("Amplitud")

plt.show()

write("pasa_bajas.wav", frecuencia_muestreo, pasa_bajas_data.astype(np.int16))