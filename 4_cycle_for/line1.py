# -*- coding: utf-8 -*-

'''
We ask the user for two numbers 'a' and 'b'
Next, we check:
if a > b -> We display an error message
In other cases, we create a loop in which we put a, b +1
And output the result of the loop
'''

a = int(input())
b = int(input())

if a > b:
    print('Не нарушай условие...')
else:
    print('')
    for i in range(a, b + 1):
        print(i)
