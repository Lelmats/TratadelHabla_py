import numpy as np

data1=np.array([1,2,3], dtype=np.int32)
data2=np.array([1,2,3], dtype=np.float32)

data3 = data1 + data2

print(data3)
print("Dtype: " + str(data3.dtype))

raiz_cuadrada = np.sqrt(np.array([-1, 0, 144]), dtype=np.complex64)
print("Raiz_cuadrada: " + str(raiz_cuadrada))
print("Dtype Raiz_cuadrada: " + str(raiz_cuadrada.dtype))

data = np.array([1,2,3], dtype=np.complex128)
print(data)
print(str(data.real) + " Dtype: " + str(data.real.dtype))
print(str(data.imag) + " Dtype: " + str(data.imag.dtype))