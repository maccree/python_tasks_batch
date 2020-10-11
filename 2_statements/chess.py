# -*- coding: utf-8 -*-

'''
Ask the user for 2 numbers(two for x and two for y)
and check the condition:
if the sum of the numbers is a multiple of two, output 'YES'
If it is not a multiple of two, output 'NO'
'''

x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())



if (x1 + y1 + x2 + y2) % 2 == 0:
    print('YES')
else:
    print('NO')
