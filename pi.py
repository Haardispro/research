import random 

def calculate_pi(n):
    circle_points = 0
    total_points = 0
    
    for i in range(n):
        x = random.uniform(0,1)
        y = random.uniform(0,1)
        distance = x**2 + y**2 
        if distance <= 1:
            circle_points += 1
        total_points += 1
    print(4 * (circle_points/total_points))

calculate_pi(10000000)



