# -*- coding: utf-8 -*-

'''
We ask the user for two numbers 'a' and 'b'
Next, we check:
If a > b -> then create a loop and put a, b +1 in it
If a < b -> then create a loop and put a, b -1, -1 in it
'''

a = int(input())
b = int(input())



if a < b:
    for i in range(a, b + 1):
        print(i)
else:
    for i in range(a, b - 1, -1):
        print(i)
