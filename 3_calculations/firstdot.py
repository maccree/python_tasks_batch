# -*- coding: utf-8 -*-

'''
We ask the user for a number and write it to the variable 'n'
Next , we check:
if n < 0, we output an error
In other cases, multiply the number by 10, and then take the remainder of the division from it
'''

n = float(input())

if n < 0:
    print('Это не положительное число...')
else:
    print(int(n * 10) % 10)
