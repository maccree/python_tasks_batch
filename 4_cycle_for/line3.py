# -*- coding: utf-8 -*-

'''
We ask the user for two numbers 'a' and 'b'
Create a loop in which we put a - (a + 1) % 2, b - b % 2, -2 -> with this expression, we get odd numbers from all the numbers
'''

a = int(input())
b = int(input())


print('')
for i in range(a - (a + 1) % 2, b - b % 2, -2):
    print(i)
