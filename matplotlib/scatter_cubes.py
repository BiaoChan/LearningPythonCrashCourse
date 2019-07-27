import matplotlib.pyplot as plt

x_values = list(range(1, 5001))
y_values = [x**3 for x in x_values]

# plt.scatter(x_values, y_values, s=20, edgecolor='none', c='red')
plt.scatter(x_values, y_values, s=40, c=y_values, cmap = plt.cm.Reds,
    edgecolor='none')
plt.title("Cube Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Cube of Value", fontsize=14)
plt.tick_params(axis='both', which='major', labelsize=14)

plt.axis([0,5100, 0, 130000000000])

plt.savefig('cubes_plot.png')
plt.show()
