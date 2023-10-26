#prime

limit = int(input("Enter range: "))

prime_numbers = []
factors = []
for i in range(1, limit+1):
    if limit % i == 0:
        factors.append(i)


print(factors)

