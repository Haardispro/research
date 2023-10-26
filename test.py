from PIL import Image, ImageDraw
from matplotlib import pyplot as plt, patches


x = 0

x_points = []
y_points = []
for i in range(10):
    y = x**2 - 1
    x = x + 1 
    x_points.append(x)
    y_points.append(y)

plt.plot(x_points, y_points)
plt.scatter(x_points, y_points)
plt.show()


    

