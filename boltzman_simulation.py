import matplotlib.pyplot as plt
import matplotlib.animation as anm
import random

POPULATION = 100
INITIAL_MONEY = 50
STAGES = 100000000
x = [INITIAL_MONEY]*POPULATION

for i in range(STAGES):
    move_from = random.randint(0,POPULATION-1)
    move_to = random.randint(0,POPULATION-1)
    if x[move_from]>0:
        x[move_from] -= 1
        x[move_to] += 1
    # if (i+1)%100==0:
        # plt.bar(range(POPULATION),x)
        # plt.show()

plt.bar(range(POPULATION),x)
plt.show()