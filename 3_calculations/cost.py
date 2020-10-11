# -*- coding: utf-8 -*-

'''
We check all possible values of variables a, b and n.
If all values passed the check, then create the 'cost' variable'which is equal to ((a * 100(converting rubles to kopecks) + b) * n)
Find out the cost in kopecks.
Next, output separately rubles and kopecks -> 'cost' / 100 (this is rubles) and find out the remainder of the division (this is kopecks)
'''

a = int(input('Рубли: '))
if a <= 0:
    print('Это как?')
else:
    b = int(input('Копейки: '))
    if b < 0:
        print('Это как?')
    else:
        n = int(input('Сколько нужно пирожков? '))
        if n < 0:
            print('Это как?')
        else:
            cost = n * (100 * a + b)
            print('Цена: ' + str(cost // 100) + ' рублей и ' + str(cost % 100) + ' копеек.')
