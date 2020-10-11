# -*- coding: utf-8 -*-

'''
We ask the user for a number and write it to the variable n.
Next , we check:
if n > 0, then its sign is+, so by the condition we output '1'
If n = 0 , then it doesn't have a header, since it is zero and we output '0'
If n < 0 , then it has znk - and output '-1'
'''


n = int(input())


if n > 0:
    print(1)
elif n == 0:
    print(0)
else:
    print(-1)
