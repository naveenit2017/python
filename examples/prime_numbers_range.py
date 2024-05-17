#Read the input from Keyboard
#Logic number is divsble 1 and itself called Prime number.
#print the out put:
num=int(input("Enter the number : "))
total=0
if num==1:
    print("please enter a valid number")
elif num>1:
    for i in range(2,num+1):
        for s in range(2,i):
            if i %s ==0:
                break
        else:
            total+=1
            print(i)

    print("The totan number of   prime numbers in given range",total)

else:
    print("Enter a valid positive number")
