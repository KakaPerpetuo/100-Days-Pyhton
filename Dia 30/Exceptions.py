#FileNotFound
#with open("a_file.txt") as file:
#     file.read()

#KeyError
#a_dictionary = {"key": "value"}
#value = a_dictionary["non_existent_key"]

#IndexError
#fruit_list = ["Apple", "Banana", "Pear"]
#fruit = fruit_list[3]

#TypeError
#text = "abc"
#print(text + 5)

# try : Something that might cause an exception

# except : Do this if there was an exception

# else : Do this if there were no exceptions

# finally : Do this no matter what happens

#FileNotFound
try:
    file = open("a_file.txt")
except:
    print("There was an error")
    file = open("a_file.txt", "w")
    file.write("Something")  

# Da pra especificar qual erro quer q a excessao capiture
try:
    file = open("a_file.txt")
    a_dictionary = {"key": "value"}
    print(a_dictionary["sdhakshd"])
except FileNotFoundError:
    print("There was an error")
    file = open("a_file.txt", "w")
    file.write("Something")  
except KeyError as error_message:
    print(f"Key {error_message} error occurred")
else:
    content = file.read()
    print(content)
finally:
    # Fazer um erro ocorrer por querer
    raise KeyError

