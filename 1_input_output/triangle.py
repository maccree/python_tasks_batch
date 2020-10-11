# -*- coding: utf-8 -*-

'''
'b' -  is one of catite
'h' is the height, but for a right-angled triangle it is also a catite that is opposite to 'b'
'''
print('S = 1/2*bh')


b = int(input('b = '))
h = int(input('h = '))

# Selecting a fractional part from an area, this is necessary for the next block
pr_s = b * h % 2

# Calculating the area without a fractional part, you need for a beautiful output
s = b * h // 2

# Calculating the area with a fractional remainder
s_withresidue = b * h / 2


# Check whether there is a fractional remainder
# If it is not, that is, it is equal to 0, then output the variable 's'
if pr_s == 0:
    print('S = ' + str(s))
# If the remainder is, that is, not equal to 0, then output the variable 's_withresidue'
elif pr_s != 0:
    print('S = ' +  str(s_withresidue))
# If neither the first nor the second item is executed(which can't be), output 'ERROR'
else:
    print('ERROR')
