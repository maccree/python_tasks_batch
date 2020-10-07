# -*- coding: utf-8 -*-

# Enter the number of students
n = int(input('Сколько школьников? '))

# Enter the number of apples
k = int(input('Сколько яблок? '))

'''
Next, we need to check all possible options that the user can enter, for example:
0 school children or 0 apples, so that it does not cause errors, we will output something, some message.
'''

# We check whether the number of students is equal to zero
if n == 0:
    print('Кто делит яблоки? -_-')
# We also check for negative numbers
elif n < 0:
    print('Это вообще как?')
else:
    # We get an integer from dividing the students by by apples
    appls_schoolpboy = k // n
    # and half the remainder of the division
    appls_basket = k % n

#   Checking the number of students
    if k == 0:
        print('Они не могут делить 0 яблок...')
    elif k < 0:
        print('Отрицательные яблоки?')


    else:
        # Output how many apples will each student get
        print('Яблок достанется каждому школьнику: ' + str(appls_schoolpboy))
        if appls_basket == 0:
            # And how many apples will remain in the basket
            print('В корзинке яблок не останется...')
        else:
            print('Яблок останется в корзинке: ' + str(appls_basket))
