#input
#logic //a,e,i,o,u,A,E,I,O,U take this in list and compare.
#output
sentence=input("enter the string : ")
list=["A","a","e","A","E","i","I","O","o","u","U"]
for char in sentence:
    if char in list:
        print(char)