year = int(input("What year is your truck? (Enter 0 to exit) "))

while year != 0:
    if year <= 2010 or year >= 2021:
        print("We only buy trucks manufactured between 2011 and 2020.")
    elif year <= 2015:
        print("We will offer $15,000 for your truck.")
    else:
        print("We will offer $22,000 Tor your truck.")

    year = int(input("What year is your truck? (Enter 0 to exit) "))

print("Thank you for using our truck purchasing service!")
