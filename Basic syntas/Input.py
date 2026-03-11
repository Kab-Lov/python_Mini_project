# to get the user input in python we can use the input() function
#input("What is your name?: ")
name = input("What is your name?: ")
age = input("How old are you?:")

age = int(age) # convert the age from string to integer
age = age + 1

print(f"Hello, {name} Welcome to python programming")       #if not using f-string we can use 
print(f"Happy birthday {name}!")                            #the + operator to concatenate the string and variable
print(f"you are {age} years old")

# another way to convert the age from string to integer is to use the int() function directly in the input() function
ages = int(input("How old are you?: "))

ages = ages + 1
print(f"Happy birthday! you are {ages} years old")
