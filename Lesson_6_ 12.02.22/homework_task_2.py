# Exclusive common numbers.
# Generate 2 lists with the length of 10 with random integers from 1 to 10, and make a third list containing
# the common integers between the 2 initial lists without any duplicates.
# Constraints: use only while loop and random module to generate numbers

from random import randint
numbers_1 = []
numbers_2 = []
numbers_3 = []
i = 0
while i < 10:
    numbers_1.append(randint(1, 10))
    numbers_2.append(randint(1, 10))
    i += 1
for i in range(len(numbers_1)):
    if numbers_2[i] in numbers_1 and numbers_2[i] not in numbers_3:
        numbers_3.append(numbers_2[i])
print(numbers_1, numbers_2, numbers_3, sep='\n')