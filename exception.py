
import pstats


a = 5
b = 0

try:
    print('Open file')
    print(a/b)
except ZeroDivisionError as e:
    print('Not possible to devide your fool', e)
except ValueError as e:
    print('Invalid input')
except Exception as e:
    print('Something wrong happen')

finally:
    print('close file')


#-- Custom exception --#
#----------------------#
class ErrorOne(Exception):
    pass

class age_out_of_range(ErrorOne):
    pass

year = int(input('Enter the year'))

age = 2022 - year

try:
    if(age < 20 | age > 30):
        raise age_out_of_range
except age_out_of_range:
    print('NOT ELIGIABLE | Your age:%i < 20 or > 30' % (age))

print("Exit")