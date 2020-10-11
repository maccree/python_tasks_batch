# -*- coding: utf-8 -*-

'''
Checking all possible values of 'n'
And calculate the time using the formula: time = n*45 + (n / 2) * 5 + ((n + 1) / 2 - 1) * 15
Next, output the time('time' / 60 + 9(hours) and the remainder of dividing 'time' by 60(minutes))
'''

n = int(input())

if n == 0:
    print('Нулевой урок?')
elif n < 0:
    print('Это вообще как?')
else:
    time = n*45 + (n//2)*5 + ((n+1)//2-1)*15
    print(str(time // 60 + 9) + ':' + str(time % 60))
