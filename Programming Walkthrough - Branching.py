age = int(input("How old are you? "))

if age <= 0:
    print("Invalid age - positive numbers only!")
    exit()

elif age <= 12:
    ticketprice = 12

elif age >= 65:
    ticketprice = 6

else:
    ticketprice = 10

print("Your price of admission is: $", ticketprice)