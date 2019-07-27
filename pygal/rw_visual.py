import pygal
import sys

sys.path.append("../matplotlib")

from random_walk import RandomWalk

rw = RandomWalk(5000)
rw.fill_walk()

values = []
for value in range(0, len(rw.x_values)):
    values.append((rw.x_values[value], rw.y_values[value]))

xy_chart = pygal.XY(stroke=False)
xy_chart.title = 'Random Walk'
xy_chart.add('random_walk', values)
xy_chart.add('start', [(rw.x_values[0], rw.y_values[0])])
xy_chart.add('end', [(rw.x_values[-1], rw.y_values[-1])])

xy_chart.render_to_file('rw_visual.svg')
