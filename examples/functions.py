'''
def add():
    return
add()
function is a block of code
when ever call the function then only it will execute. 
'''
def outer():
    print("this is from outer function")
    def inner():
        print("it is from inneer or nested function")
    inner()
outer()

def abc(**a):
    print(a)
abc(a=1,b=2,c=3)