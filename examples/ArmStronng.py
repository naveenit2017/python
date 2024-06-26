#Armstrong number
#153 --> len of the number && and power of the indivduals numbers sum is equal to that number
#153-->len=3=>1**3+5**+3**3

for i in range(1000):
    num=i
    res=0
    n=len(str(num))
    while(i!=0):
        digit=i%10
        res=res+digit**n
        i=i//10
    if res==num:
        print(res)

=============================
#Armstrong number
#logic--
#1.Take the input number
#2.length of that number
#3.power of lenth ,that individual number.

nu=int(input("Enter the number"))
num1=nu
n=len(str(num1))
print(n)
sum=0

print(type(num1))
for num in range(num1):
    while num>0:
        print(sum)
        d=num%10
        sum=sum+d**n
        num=num//10
    if sum==nu:
        print("Armstrong number")
        print(sum)
    else:
        print("It is not amrmstrong number")
