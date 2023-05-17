import random
from itertools import combinations


def calculate_factorial(n):
    if n <= 1:
        return 1
    else:
        return n * calculate_factorial(n - 1)

n = 5
factorial = calculate_factorial(n)
print(factorial)

permutation = []

i = 0
permutation_unique = []
while i != factorial:
    # create a sequence of 6 random numbers from 1 to 6
    random_numbers = [random.randint(1, n) for _ in range(n)]
    # check if all numbers are individual
    if all(num1 != num2 for num1, num2 in combinations(random_numbers, 2)):
        if random_numbers not in permutation:
            permutation.append(random_numbers)
            i += 1

for seq in permutation:
    print(' ')
    for el in seq:
        print(el, end=' ')
