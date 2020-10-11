# -*- coding: utf-8 -*-

'''
We ask the user for 3 numbers and write them to the variables n1, n2 and n3.
Next, we check:
if n1 = n2 = n3, then output '3'
If n1 = n2 or n2 = n3 or n1 = n3 , then output '2'
In all other cases, output '0'
'''

n1 = int(input())
n2 = int(input())
n3 = int(input())


if n1 == n2 == n3:
    print(3)
elif n1 == n2 or n2 == n3 or n1 == n3:
    print(2)
else:
    print(0)
