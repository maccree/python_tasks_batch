# -*- coding: utf-8 -*-

'''We ask the user how many students there are in three classes(we write everything in the variables class1, class2 and class3).
Then divide the students in each class by 2(since there are 2 people sitting at the same Desk), and if it is not divided by 2, then add one more Desk'''


class1 = int(input('Сколько человек в первом классе? '))
class2 = int(input('Сколько человек во втором классе? '))
class3 = int(input('Сколько человек в третьем классе? '))


dasks = class1 // 2 + class2 // 2 + class3 // 2 + class1 % 2 + class2 % 2 + class3 % 2

print('Парт нужно: ' + str(dasks))
