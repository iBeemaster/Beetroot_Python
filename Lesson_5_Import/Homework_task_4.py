# The math quiz program
# Write a program that asks the answer for a mathematical expression, checks whether the user is right or wrong,
# and then responds with a message accordingly.

from random import randrange
from math import sqrt
a, b, c = randrange(-10, 10), randrange(-10, 10), randrange(-10, 10)
answer = []
user_answer = []
print(f'Найдите корни квадратного уравнения: {a}x**2 {b:+}x {c:+} = 0')
D = b ** 2 - 4 * a * c
if D > 0:
    x1 = round((- b - sqrt(D)) / (2 * a), 2)
    x2 = round((- b + sqrt(D)) / (2 * a), 2)
    answer.append(x1)
    answer.append(x2)
    print(min(x1, x2), max(x1, x2), sep='\n')
elif D == 0:
    x1 = - round(b / (2 * a), 2)
    answer.append(x1)
    print(x1)
else:
    x1 = 'корней нет'
    answer.append(x1)
print(f'Введите корни уравнения с новой строки c точностью до двух знаков после запятой.\n'
      f'Пример. Два корня: -2.72 4.23. Один корень: -3.45. Нет корней: корней нет')
print(answer, end='\n')
if x1 == 'корней нет':
    user_answer = [input()]
else:
    user_answer = [float(input()) for _ in range(len(answer))]
if user_answer == ['корней нет']:
    print('Правильно, корней нет.')
elif user_answer[0] in answer and len(answer) == 1:
    print(f'Верно, уравнение имеет один корень {x1}.')
elif user_answer[0] in answer and user_answer[1] in answer and len(answer) == 2:
    print(f'Верно, корни квадратного уравнения {x1} и {x2}.')
else:
    print('Ответ неверный или неполный')