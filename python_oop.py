'''
Three types of method
-----------------------
1. Instance method 
    [Decorative: None]
    [Parameter: self, ... .. .]
    [Access to only local member of class]
2. Class method 
    [Decorative: @classmethod]
    [Parameter: cls, ... .. .]
    [Access to all member of class]
3. Static method 
    [Decorative: @statickmethod]
    [Parameter: ... .. .]
    [No access to any member of class]
'''

from typing_extensions import Self

from numpy import inner


class ComplexNumber:
    som = 45
    type = "Complex number"

    def __init__(self, n, i):
        self.normal = n
        self.imagenary = i
    
    #--> Instance method
    def disply(self):
        print(self.normal.__str__() + ' + ' + self.imagenary.__str__() + 'i')

    def __str__(self) -> str:
        return self.normal.__str__() + ' + ' + self.imagenary.__str__() + 'i'

    #--> Class method
    @classmethod
    def info(cls): 
        cls.som += 1
        print('Info is printing')
        return

    #--> Static method
    @staticmethod
    def info_s():
        print('I am static, buddy')

    def __add__(self, b):
        return ComplexNumber(self.normal+b.normal, self.imagenary+b.imagenary)




#---- Inner Class ----#
#---------------------#
class Student:
    def __init__(self, name, rollno) -> None:
        self.name = name
        self.rollno = rollno
        self.new_lap = self.Laptop('one', 'two', 3)

    def show(self):
        print(self.name, self.rollno, self.new_lap)

    def __str__(self):
        return "Name:%s \r\n RollNo:%s \r\n Laptop:%s" % (self.name, self.rollno, self.new_lap)

    class Laptop:
        def __init__(self, b='Asus', c='i5', r=8) -> None:
            self.brand = b
            self.cpu = c
            self.ram = r
        
        def __str__(self):
            return "Brand:%s CPU:%s RAM:%s" % (self.brand, self.cpu, self.ram)
            # return "This is the laptop print"

'''
    A -> B [Single Level]
    C -> B -> A [Multi Level]
    A B [Multiple]
    | |
     C
'''
class A:
    def __init__(self) -> None:
        print("A init")

    def feature1(Self):
        print("Feature 1 working")
    
    def feature2(Self):
        print("Feature 2 working")

class B(A):
    def __init__(self) -> None:
        super().__init__()
        print("B init")

    def feature3(Self):
        print("Feature 3 working")
    
    def feature4(Self):
        print("Feature 4 working")

def general_oop():
    cmp = ComplexNumber(85, 97)
    cmp.disply()

    ComplexNumber.info()
    ComplexNumber.info_s()

    print(ComplexNumber.som)

def inner_class():
    st = Student("Bhadrik", '1715')
    st.show()

def inheritance():
    a1 = A()
    a1.feature1()
    a1.feature2()

    b1 = B()
    b1.feature4()
    b1.feature1()


'''
Polymorphism
=============
Dusk Typing: [Class type doesnt matter it need to have appropriate method in it]
Operator Overloading [Ex. In complex class] 
Method Overloading
Method Overriding
'''

def polymorhpism():
    #--Operator over..--#
    c1 = ComplexNumber(1, 3)
    c2 = ComplexNumber(4, 5)
    c3 = c1 + c2
    # c3.disply()
    print(c3)

def main():
    # general_oop()
    # inner_class()
    # inheritance()
    polymorhpism()

if (__name__ == '__main__'):
    main()