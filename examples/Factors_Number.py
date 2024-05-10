def factors_no(number):
    print("The factors of ",number)
    for i in range(1,number+1):
        if number % i == 0:
            print(i)

number=int(input("Enter the valid number"))
factors_no(number)