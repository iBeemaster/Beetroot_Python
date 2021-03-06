#1. Основные особенности языка программирования Python:
# кроссплатформенный интерппретируемый язык
# простота синтаксиса и логики программного кода, которая обеспечивается философией языка
#
# Текст философии
# Красивое лучше, чем уродливое.
# Явное лучше, чем неявное.
# Простое лучше, чем сложное.
# Сложное лучше, чем запутанное.
# Плоское лучше, чем вложенное.
# Разреженное лучше, чем плотное.
# Читаемость имеет значение.
# Особые случаи не настолько особые, чтобы нарушать правила.
# При этом практичность важнее безупречности.
# Ошибки никогда не должны замалчиваться.
# Если они не замалчиваются явно.
# Встретив двусмысленность, отбрось искушение угадать.
# Должен существовать один и, желательно, только один очевидный способ сделать это.
# Хотя он поначалу может быть и не очевиден, если вы не голландец [^1].
# Сейчас лучше, чем никогда.
# Хотя никогда зачастую лучше, чем прямо сейчас.
# Если реализацию сложно объяснить — идея плоха.
# Если реализацию легко объяснить — идея, возможно, хороша.
# Пространства имён — отличная штука! Будем делать их больше!
#
# 2. Название переменной в Python должно начинаться с алфавитного символа
# или со знака подчеркивания и может содержать алфавитно-цифровые символы и знак подчеркивания.
# И кроме того, название переменной не должно совпадать с названием ключевых слов языка Python.
#
# 3.
major_version = '3'
minor_version = '.9'
version = major_version + minor_version
language = 'Python'
language_version = language + ' ' + version
print(language_version)