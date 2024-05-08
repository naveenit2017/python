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