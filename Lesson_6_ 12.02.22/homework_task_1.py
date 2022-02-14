# The greatest number
# Write a Python program to get the largest number from a list of random numbers with the length of 10
# Constraints: use only while loop and random module to generate numbers

from random import randint
numbers = []
i = 0
while i < 10:
    numbers.append(randint(-10, 10))
    i += 1
print(f'В списке {numbers}, самое большое число {max(numbers)}.')
