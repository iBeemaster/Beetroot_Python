# Printing 'O' letter
for i in range(1, 6): 
    if i == 1 or i == 5:
        print('#' * 9)
    else:
        print('#', ' ' * 7, '#', sep='')
print('')
# Printing 'H' letter
for i in range(1, 6):
    if i == 3:
        print('#' * 9)
    else:
        print('#', ' ' * 7, '#', sep='')
print()