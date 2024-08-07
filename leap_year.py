def leap_year(year):
    if (year%4==0):
        if(year%100==0):
            if (year%400==0):
                return True
            return False
        return True
        
    
year=2020
if leap_year(year):
    print(year, "is a leap year")
else:
    print(year, "is not a leap year")