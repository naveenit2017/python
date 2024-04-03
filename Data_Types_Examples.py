a = 10  # 
b = 9.0
c = 3+5j

print("This value from int " +str(a))
print("this is from float ",b)
print('This is from complex', c)

#sring --immutable once they are created the content can't be modified.
my_str="Hello world from double quotes string"
my_str="naveen sir"
#my_str[0]='s'  #This is string immutable
my_str1='I am from single quote string'
print(my_str)
print(my_str1)

my_list=[6,8,"sai"]
my_list[1]=27  #mutable concept
my_list[0]="baba"
print("this is input from list ",my_list)

my_tuple=(1,3,56,6,9,"sai")
print(my_tuple[2:4])
print(my_tuple)
print(my_tuple[3])  #this should be work
