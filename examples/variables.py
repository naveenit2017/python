#variable it is container store the values
#to check the variable memory location will use id method.

a="10"
print(a)
# a,b,c=10 will get error
a=b=c=12
print(a,b,c)
print(id(a))

'''
data types:
----------
int -->1,3,5
float =2.0
complex =2+3j
boolean =True or 1 ,False or 0
Type casting:
------------
implicit conversion --no data loss (means if we convert 2 into double value will get 2.0)
explicit conversion --Data loss(means if we convert 2.5 in to int value will get 2)
'''
