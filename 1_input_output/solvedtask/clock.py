# -*- coding: utf-8 -*-

# We ask the user how many minutes should be shown on the electronic clock
n = int(input('Минуты: '))

# We check if it is at least 0 minutes, and if it is less, we output a message
if n < 0:
    print('Это как?')
    # we check if the day has passed
elif n == 1440:
    # if exactly one day has passed, we display the message
    print('Прошли целые сутки!')
    # if more than one day
elif n > 1440:
    # counting 'n' without a day
    n_without_days = n - 1440
    # counting how many days
    days = n // 1440
    # counting hours and minutes without a day
    hours_without_days = n_without_days % (60 * 24) // 60
    minutes_without_days = n_without_days % 60
    # we count whether more than one day has passed or not, in order to comply with grammar
    if days == 1:
        print(str(hours_without_days) + ':' + str(minutes_without_days) + ' и ' + str(days) + ' сутки')
    else:
        print(str(hours_without_days) + ':' + str(minutes_without_days) + ' и ' + str(days) + ' суток')
# If everything is in order:
else:
    # counting the hours
    hours = n % (60 * 24) // 60
    # counting minutes
    minutes = n % 60

    print(str(hours) + ':' + str(minutes))
