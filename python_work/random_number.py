from random import randint

sum = 0

for value in range(1000000):
    x = randint(1, 99)
    # print(x)
    sum += x

ave = sum/1000000

print(str(sum) + " " + str(ave))
