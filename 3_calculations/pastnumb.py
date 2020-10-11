# -*- coding: utf-8 -*-

'''
We ask the user for a number and write it to the variable n
Next, we check:
If n < 0, then multiply by -1
In all other cases, output the remainder of dividing n by 10
'''


n = int(input('Ваше число: '))

if n < 0:
    n_plus = n * -1
    print('Последняя цифра вашего числа: ' + str(n_plus % 10))
else:
    print('Последняя цифра вашего числа: ' + str(n % 10))
