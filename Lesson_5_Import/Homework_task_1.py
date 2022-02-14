#The Guessing Game.
# Write a program that generates a random number between 1 and 10 and lets the user guess what number was generated.
# The result should be sent back to the user via a print statement.

from random import randint
while True:
    num = randint(1, 10)
    user_answer = int(input('Введите число от 1 до 10: '))
    if num == user_answer:
        print(f'Верно. Было загадано число {num}.')
    else:
        print(f'{user_answer} это неправильный ответ. Было загадано число {num}.')
    print(f'Сыграем ещё? да, нет?: ')
    if input().lower() == 'нет':
        break
print('Спасибо за игру!')
