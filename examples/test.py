#leap year if year is divded by 4 that number is leap year.
#make use the functions concept and 

def is_leap_year(year):
    if year%4==0:
        return True
    else :
        return False

#Enter the input from key board.
year=int(input("Enter the year :"))
if is_leap_year(year):
    print("This is leap year",year)
else:
    print("This is not leap year",year)




