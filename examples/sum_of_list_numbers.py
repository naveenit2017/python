#sum of list numbers
#1.take the input as list ex:my_list=[1,2,3,4]
#create function and pass the list as parameter and use for loop to get the values and them and return the sum to the function
def sum_of_list(numbers):
    sum=0
    for i in numbers:
        sum=sum+i
    return sum
numbers=[1,2,3,4,5]
print(sum_of_list(numbers))
