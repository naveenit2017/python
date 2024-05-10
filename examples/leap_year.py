#take the input from the key board
#If a number is divisble by 4 ,that number is leap year.
#print year
def isLeapYear(year):
    if year%4==0:
        return True
    else:
        return False
year=int(input("enter the year :"))    
if isLeapYear(year):
    print("this is a leap year",year)
else:
    print("non leap year",year)
