'''
try:
    risk code
except :
    "error"
else:
    "no error"
finally:
    "always execute"
'''
print("This is for Exception Handling Demo Demo ")
try:
    a=10%0
    print(a)
except:
    print("Execute this block")
else:
    print("There is no error")
finally:
    print("it is always executed ")

------------
#Exception handling

#try --will keep the risk code
#except --if try will get error it will execute
#else --no error
#finally:

try:
    a=10%0
    print(a)
except:
    print("Try block have issue please check")
else:
    print("Time god no error")
finally:
    print("It will execute always")

