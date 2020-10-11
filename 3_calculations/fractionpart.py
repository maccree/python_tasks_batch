# -*- coding: utf-8 -*-

'''
we ask the user for a number and write it to the variable 'n'
Next, we check:
if n < 0, we output an error message.
In all other cases: output the remainder of the division by 1, thus output the fractional part.
'''


n = float(input())

if n < 0:
    print('Это не положительное число...')
else:
    print(n % 1)
