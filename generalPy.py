fi = 3234
str = 'hello, world {}'
print(str.format(fi))


# str -> int

num = '3624'

oth = int(num)

print(oth, type(oth))

#OUTPUT: hello, world 3234



#-- Lamda --#
#-----------#
x = lambda y : y + 43

print(x(10))


#-- Iterator for iterable --#
#---------------------------#
some_tuple = ('safarjan', 'kedu', 'narangi', 'chiku', 'ananas')
its = iter(some_tuple)

print(next(its))
print(next(its))