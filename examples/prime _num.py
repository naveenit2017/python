#Prime numbers
#take the input 
#impliment logic,number is divisble by 1 and itself is called by prime number.
#print the out put
num=int(input("enter a valid number : "))
if num==1:
    print("it is not a valid number ")
elif num>1:
    for i in range(2,num):
        if num%i==0:
            print("not prime")
            break
    else:
        print("it is a prime")
else:
    print("please enter a positive number")

