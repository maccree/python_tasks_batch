# -*- coding: utf-8 -*-



print('S = 1/2*bh')
b = int(input('b = '))
h = int(input('h = '))


pr_s = b * h % 2 

s1 = b * h // 2
s2 = b * h / 2

if pr_s == 0:
    print('S = ' + str(s1))
elif pr_s != 0:
    print('S = ' + str(s2))
else:
    print('ERROR')

#print('S = ' + str(s))



