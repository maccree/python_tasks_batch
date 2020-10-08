# -*- coding: utf-8 -*-



class1 = int(input('Сколько человек в первом классе? '))
class2 = int(input('Сколько человек во втором классе? '))
class3 = int(input('Сколько человек в третьем классе? '))


dasks = class1 // 2 + class2 // 2 + class3 // 2 + class1 % 2 + class2 % 2 + class3 % 2

print('Парт нужно: ' + str(dasks))
