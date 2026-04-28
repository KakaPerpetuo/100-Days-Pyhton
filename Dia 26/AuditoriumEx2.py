list_of_strings = input().split(',')

# Use list comprehension to convert the strings to integers
int_list = [int(number) for number in list_of_strings]

# Filter odd numbers and store even numbers in a list called result
result = [number for number in int_list if number % 2 == 0]

print(result)