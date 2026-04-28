print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120: # Ficar atento com a identacao
    
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    
    if age < 12:
        cash = 5
        print("Child tickets are $5")
    elif age <= 18:                 # Em python usa-se AND nao &&
        cash = 7
        print("Youth tickets are $7")      # elif == else if
    elif age >= 45 and age <= 55:
        print("Everything is gonna be ok. Have a ride on us!")  # Nao precisa declarar a variavel aqui
    else:
        cash = 12
        print("Adult tickets are $12")
    
    want_photo = input("Want photos? ")
    
    if want_photo == "yes":
        cash += 3
    
    print(f"The total bill is ${cash}")
else:
    print("Sorry, you have to grow taller before you can ride.")



