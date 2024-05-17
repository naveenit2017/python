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
