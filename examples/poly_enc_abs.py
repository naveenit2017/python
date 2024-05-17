'''
Encapsulation-Wrapping of variables and methods into a single unit
access specifiers(Data security):
public:we can access any where
private(__):Only that class
protected(_):We can access only in derived class
'''
class Demo:
    def __init__(self,a,b,c):
        self.a=a
        self.__b=b
        self._c=c
        print("I am from parent",self.__b)
class MyClass(Demo):
    def mout(self):
        print("this are from parent class")
        print(self.a)
        # print(self.__b)
        print(self._c)
m=MyClass(2,3,4)
m.mout()

#def __init__(self,a,b,c)://Intailaization.
def add(a,b):
    print(a+b)
add(1,2)
add('x','y')
add([1,2],[1,3])
