# 4. Послідовність Фібоначчі
num1, num2, num3 = 0, 1, 0
total = 0
while num2 < 100_000:
    num3 = num1 + num2
    num1, num2 = num2, num2 + num1
    if num1 % 2 != 0:
        total += num1
print(total)
