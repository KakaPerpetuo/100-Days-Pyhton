with open("file1.txt") as file:
    list1_n = file.readlines()

list1 = [number.rstrip('\n') for number in list1_n]

with open("file2.txt") as file:
    list2_n = file.readlines()

list2 = [number.rstrip('\n') for number in list2_n]

result = [int(number) for number in list1 if number in list2]

print(result)