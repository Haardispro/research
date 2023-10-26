from matplotlib import pyplot as plt, patches
import random

fig = plt.figure()
ax = fig.add_subplot()

circle1 = patches.Circle((0, 0), radius=1, fill=False)

circle_points = 0
total_points = 0
n = 1000
for i in range(n):
    x = random.uniform(-1,1)
    y = random.uniform(-1,1)
    ax.scatter(x,y, s = 2, c = "blue")
    distance = x**2 + y**2 
    if distance <= 1:
        circle_points += 1
    total_points += 1

pi = 4*(circle_points/total_points)

ax.add_patch(circle1)
ax.axis('square')

plt.title("Estimated Value of Pi = " + str(pi))

plt.show()
