#1.take the input 
#2.reverse that input 
#3.compare that input
string=input("enter the string  : ")
revrse_string=string[::-1]
if string == revrse_string:
    print("It is palindrome")
else:
    print("this is not a palindrome")