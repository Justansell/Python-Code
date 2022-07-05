print("Hello, and thank you for using The Speedy Shipping Company!")
print()

while True:

    while True:
        try:
            pack_weight = float(input("Please enter package weight in pounds: "))
        except ValueError:
            print("Invalid entry--please try again")
            print()
            continue

        if pack_weight <= 0:
            print("Invalid package weight--please enter weight greater than 0")
            print()
            continue
        elif pack_weight > 10:
            print("Invalid package weight--weight cannot exceed 10 lbs")
            print()
            continue
        else:
            break

    while True:
        try:
            ship_distance = int(input("Please enter shipping distance in miles: "))
        except ValueError:
            print("Invalid entry--please enter positive number")
            print()
            continue

        if ship_distance <= 0:
            print("Invalid shipping distance--please enter distance greater than 0")
            print()
            continue
        elif ship_distance > 12450.73:
            print("Invalid shipping distance--distance cannot be greater than half the circumference of the earth.")
            print()
            continue
        else:
            break

    while True:
        if pack_weight <= 2:
            cost_per_segment = 1.50
            break
        elif pack_weight <= 6:
            cost_per_segment = 3.25
            break
        elif pack_weight <= 10:
            cost_per_segment = 5.15
            break

    ship_cost = cost_per_segment * (((ship_distance - 1) // 500) + 1)

    print(f"Your total shipping cost is ${ship_cost:.2f}.")
    ans = input("Would you like to enter information about another package? ")


    if ans in ['y', 'Y', 'yes', 'Yes', 'YES']:
        print()
        continue
    else:
        print()
        break

print("Thank you for using The Speedy Shipping Company. Have a great day!")
