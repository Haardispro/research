# To Plot prime numbers on a graph 

from matplotlib import pyplot as plt


# Python program to print all
# prime number in an interval
def prime(x, y):
	prime_list = []
	for i in range(x, y):
		if i == 0 or i == 1:
			continue
		else:
			for j in range(2, int(i/2)+1):
				if i % j == 0:
					break
			else:
				prime_list.append(i)
	return prime_list

# Driver program
starting_range = 1
ending_range = 100
lst = prime(starting_range, ending_range)

x_points = lst 
y_points = lst 

plt.scatter(x_points, y_points)
plt.show()



print(lst)
