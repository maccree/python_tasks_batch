# -*- coding: utf-8 -*-
'''
We ask the user for their number and write it to the 'numb' variable. Next, we create two new variables: next(this is the user's number +1) and previous(this is the user's number -1)
and output a message With this data
'''


numb = int(input('Your number: '))

next = numb + 1
previous = numb - 1

print('The next number for the number ' + str(numb) + ' is ' + str(next) + '. The previous number for the number ' + str(numb) + ' is ' + str(previous) + '.' )
