# -*- coding: utf-8 -*-

'''
We ask the user for two numbers. the speed and time.
Next, we check:
if t < 0, we output an error message.
In other cases: v * t and from the result of multiplication output the remainder of division by 109
'''

v = int(input('v: '))
t = int(input('t: '))

if t < 0:
    print('Это как?')
else:
    print((v * t) % 109)
