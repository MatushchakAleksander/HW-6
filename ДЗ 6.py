N = int(input('Enter a value for the width of the triangle: '))

counter = N
sb = '*'
print('1)')
while counter > 0:
    print(sb * counter)
    counter -= 1

counter = 0
print('2)')
while counter < N:
    counter += 1
    print(sb * counter)

counter = N
counter_3 = 0
print('3)')
while counter > 0:
    print(' ' * counter_3 + sb * counter)
    counter_3 = counter_3 + 1
    counter -= 1

counter = 0
counter_4 = N - 1
print('4)')
while counter < N:
    counter = counter + 1
    print(' ' * counter_4 + sb * counter)
    counter_4 -= 1
