# -*- coding: utf-8 -*-

'''
We ask the user for two numbers and write them to the variables m and n.
Next, check the condition:
If m > n , then output n
If m < n , then output m
If two conditions are not met, then the numbers are equal and we output the corresponding message
'''

n = int(input('Первое число: '))
m = int(input('Второе число: '))


if m > n:
    print(n)
elif m < n:
    print(m)
else:
    print('Они равны')
