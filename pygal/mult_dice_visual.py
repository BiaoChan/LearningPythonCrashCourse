import pygal

from die import Die

#对结果进行可视化
hist = pygal.Bar()

hist.title = "Result of rolling tow D6 1,000,000 times."
hist.x_labels = []
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

#创建一个Die()
die_1 = Die()
die_2 = Die()

#掷几次骰子，并将结果存储在一个列表中
results = []
for roll_num in range(1000000):
    result = die_1.roll() * die_2.roll()
    results.append(result)

#分析结果
frequencies = []
max_result = die_1.num_sides * die_2.num_sides
for value in range(1, max_result+1):
    frequency = results.count(value)
    if frequency:
        frequencies.append(frequency)
        hist.x_labels.append(str(value))

# print(frequencies)



hist.add('D6 * D6', frequencies)
hist.render_to_file('mult_dice_visual.svg')
