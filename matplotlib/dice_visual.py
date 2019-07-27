import matplotlib.pyplot as plt
import sys

sys.path.append("../pygal")

from die import Die

#创建一个Die()
die_1 = Die()
die_2 = Die()

#掷几次骰子，并将结果存储在一个列表中
results = []
for roll_num in range(100000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

#分析结果
frequencies = []
x_labels = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)
    x_labels.append(str(value))

plt.bar(x_labels, frequencies, align='center')

plt.title("Result of rolling tow D6 100,000 times.", fontsize=24)
plt.xlabel("Result", fontsize=14)
plt.ylabel("Frequency of Result", fontsize=14)

plt.show()
