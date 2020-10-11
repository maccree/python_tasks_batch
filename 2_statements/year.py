# -*- coding: utf-8 -*-

'''
We ask the user for a number and write it to the 'year'variable
Next, we check whether
the number is a multiple of 2 and not a multiple of 100 or a multiple of 400. if Yes, we output 'YES'
In other cases, output 'NO'
'''

year = int(input())


if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
    print('YES')
else:
    print('NO')
