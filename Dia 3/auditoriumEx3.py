year = int(input())

if year % 4 == 0:
    if year % 100 == 0:                         # Colocar os complementos do if, o que é o else, antes de colocar as condicoes de dentro
        if year % 400 == 0:
            print("This is a leap year!")
        else:
            print("This is not a leap year.")
    else:
        print("This is a leap year!")
else:
    print("This is not a leap year.")