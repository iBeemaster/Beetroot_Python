num = 0
sum_num = 0
while num < 100:
    num = num + 1
    if num % 3 == 0 and num % 5 == 0:
       sum_num = sum_num + num
print(sum_num)