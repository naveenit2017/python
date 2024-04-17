#A list is a fundamental data structure in programming that allows you to store a collection of items.
#Lists are ordered and can contain elements of various data types, 
#such as numbers, strings, and objects.
#list is mutable.

my_list = [1, 2, 3, 'apple', 'banana']
print(my_list)
print(len(my_list))
my_list.append("sai")
print(my_list)
my_list[2]="baba"
print(my_list)
my_list.remove(1)
print(my_list)
new_list=my_list+["naveen","amulya"]
print(my_list)
print(new_list)

for el in new_list:
    print(el)

