weight, height = int(input('Введите ваш вес в килограммах: ')), int(input('Введите ваш рост в сантиметрах: '))
bmi = weight / (height*0.01)**2
print('Your BMI is normal:', 18.5 <= bmi <= 25)