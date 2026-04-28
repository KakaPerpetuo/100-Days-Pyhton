def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
    
def days_in_month(year, month):
    
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    day = month_days[month - 1]

    if is_leap(year) and month == 2:
        day += 1
    
    return day

## Outra forma de fazer 
# def days_in_month(year, month):
#    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#    if month == 2 and is_leap(year):
#        return 29
#    else:
#        return month_days[month - 1]
    
year = int(input())
month = int(input())
days = days_in_month(year, month)
print(days)