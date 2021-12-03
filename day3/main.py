import numpy as np

data = np.genfromtxt('data', delimiter=1, dtype=np.float64)
omega = np.mean(data, axis = 0) >= 0.5
epsilon = ~omega
binary_base = 2**np.arange(omega.shape[0])[::-1]
omega_decimal = np.dot(binary_base, omega)
epsilon_decimal = np.dot(binary_base, epsilon)
power = epsilon_decimal * omega_decimal

index = np.arange(data.shape[0])
col = 0
while(index.shape[0] != 1):
    bv = np.mean(data[index, col]) >= 0.5
    index = index[data[index, col] == bv]
    col += 1
oxygen = data[index,:][0]

index = np.arange(data.shape[0])
col = 0
while(index.shape[0] != 1):
    bv = np.mean(data[index, col]) < 0.5
    index = index[data[index, col] == bv]
    col += 1
scrubber = data[index,:][0]

oxygen_decimal = np.dot(binary_base, oxygen)
scrubber_decimal = np.dot(binary_base, scrubber)
life_support = scrubber_decimal * oxygen_decimal
print(life_support)
