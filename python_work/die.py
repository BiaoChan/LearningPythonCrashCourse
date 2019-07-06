from random import randint

class Die():
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        x = randint(1, self.sides)
        return x

# die = Die()
# die = Die(10)
die = Die(20)
statistic = {}
for value in range(1, die.sides+1):
    statistic[value] = 0

for value in range(1000000):
    x = die.roll_die()
    statistic[x] += 1

for key, value in statistic.items():
    print(str(key) + ":" + str(value))
