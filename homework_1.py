import math
import random

iter = int(input("Number of interations: "))
step = int(input("Display step: "))

inside = 0 #points inside a circle
pi_estimated = 0 #current pi estimation

for i in range(iter):
    x = random.random()
    y = random.random()
    if (x ** 2 + y ** 2 <= 1):
        inside += 1
    pi_estimated = 4*inside/(i+1)
    if i == step:
        print("Estimation after ", i, "steps: ", pi_estimated)
        step += step
print("Final pi estimation: ", pi_estimated)
print("Actual pi: ", math.pi)


