# Exercise 1: Calculate the area of a triangle

length = float(input("Input the length of the triangle: "))
width = float(input("Input the width of the triangle: "))

area = length * width
print(f"The area of the triangle is: {area} cm²")


# Exercise 2: Shopping cart program
item = input("Do you need anything?: ")
price = float(input("Price: "))
quantity = int(input("How many would you like: "))

#operation to calculate 
total_price = price * quantity

#print the total price
print(f"You have bought {quantity} x {item}")
print(f"The total price of {quantity} {item} is: ${total_price} USD")