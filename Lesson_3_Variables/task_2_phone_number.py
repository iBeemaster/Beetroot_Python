phone_number = input('Введите номер телефона: ')
flag = phone_number.startswith('380') == phone_number.isdigit()
flag = len(phone_number) == 12
print('Корректность введённого номера телефона:', flag)