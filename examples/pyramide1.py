#1
#12
#123
#1234
#12345  #range(5)-->0,1,2,3,4 #range(1,5)-->1,2,3,4
n=int(input("Enter the number"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()