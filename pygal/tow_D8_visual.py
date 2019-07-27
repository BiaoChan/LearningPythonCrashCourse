import pygal

from die import Die

#创建一个Die()
die_1 = Die(8)
die_2 = Die(8)

#掷几次骰子，并将结果存储在一个列表中
results = []
for roll_num in range(10000000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

#分析结果
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# print(frequencies)

#对结果进行可视化
hist = pygal.Bar()

hist.title = "Result of rolling tow D8 10,000,000 times."
hist.x_labels = [str(value) for value in range(2, max_result+1)]
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D8 + D8', frequencies)
hist.render_to_file('dice_visual.svg')
