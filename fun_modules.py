#Function : A peace or block of code which can be reusable.
#module : Collection of functions are called module or .py files also called
#packages : Collection of modules 
from test_modules import test_fun
import my_fun
 
#All the exmples are excucting .
#creating a function here


def my_world_fun() :
    print("Hello this is created from the same file")

#calling a module my_fun
my_fun.greet()
#calling a module from package test_modules
#from test_modules import test_fun
res=test_fun.mysqrtt(5)
print(res)

my_world_fun()
