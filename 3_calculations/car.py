# -*- coding: utf-8 -*-
from math import ceil

'''
Import math because I didn't find any other way to perform this task.

We ask the user for two numbers and write them to the variables n and m.
Next, we check:
if n < or is equal to 0, we output an error message.
If m < or is equal to 0, we output an error message.
In all other cases:
Create a new variable 'days' which is equal to m / n(and if the result of division is not an integer, then add +1 to it. this will make 'math')
And output 'days'
'''

n = int(input('Сколько проезжет за день? '))
m = int(input('Длина маршрута? '))

if n <= 0:
    print('Это как?')
elif m <= 0:
    print('Это как?')
else:
    days = ceil(m / n)
    print('Нужно дней: ' + str(days))
