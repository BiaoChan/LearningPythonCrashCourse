import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5, 6]
cubes = [1, 8, 27, 64, 125, 196]

plt.plot(input_values, cubes, linewidth=5)
plt.title("Cube Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Cube of Value", fontsize=14)

plt.tick_params(axis='both', labelsize=14)
plt.show()
