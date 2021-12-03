import numpy as np

data = np.genfromtxt('data', delimiter=1, dtype=np.float64) 
omega = np.mean(data, axis = 0) > 0.5
epsilon = ~omega
binary_base = np.arange(omega.shape[0])
omega_decimal = np.dot(2**np.arange(omega.shape[0])[::-1], omega)
epsilon_decimal = np.dot(2**np.arange(epsilon.shape[0])[::-1], epsilon)
power = epsilon_decimal * omega_decimal
print(power)
