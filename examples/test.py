#factorial 5-->5*4*3*2*1
#1.take input 
#2.logic
#3.print output
n=int(input("Enter the factorial number : "))
res=1
for i in range(1,n+1):
    res=res*i
print(res)