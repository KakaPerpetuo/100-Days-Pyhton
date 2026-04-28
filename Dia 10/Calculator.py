import art

# Add
def add(n1, n2):
    """ Sum function """
    return n1 + n2

# Subtract
def subtract(n1, n2):
    """ Subtract function """
    return n1 - n2

# Multiply
def multiply(n1, n2):
    """ Multiply function """
    return n1 * n2

# Divide
def divide(n1, n2):
    """ Divide function """
    return n1 / n2

operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide,
}

def calculator():

    print(art.logo)

    will_continue = True           ## Isso é uma flag

    num_1 = float(input("What's the first number?: "))

    for symbol in operations:
        print(symbol)
    operation_symbol = input("Pick an operation from the line above: ")

    num_2 = float(input("What's the second number?: "))

    operation_function = operations[operation_symbol]
    answer = operation_function(num_1, num_2)

    print(f"{num_1} {operation_symbol} {num_2} = {answer}")

    while will_continue:
        continue_ = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") 
        
        if continue_ == "y":
            operation_symbol = input("Pick an operation: ")
            num_3 = int(input("What's the next number?: "))

            old_answer = answer

            operation_function = operations[operation_symbol]
            answer = operation_function(old_answer, num_3)

            print(f"{old_answer} {operation_symbol} {num_3} = {answer}")
        else:
            will_continue = False
            calculator()          ## Recursao

calculator()

## Outra forma de fazer 
#def calculator():
#    print(art.logo)

#    will_continue = True           ## Isso é uma flag

#    num_1 = float(input("What's the first number?: "))

#    for symbol in operations:
#        print(symbol)

#    while will_continue:
#        operation_symbol = input("Pick an operation: ")

#        num_2 = float(input("What's the next number?: "))

#        operation_function = operations[operation_symbol]
#        answer = operation_function(num_1, num_2)

#        print(f"{num_1} {operation_symbol} {num_2} = {answer}")

#        continue_ = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") 
        
#        if continue_ == "y":
#            num_1 = answer
#        else:
#            will_continue = False
#            calculator()          ## Recursao

#calculator()





