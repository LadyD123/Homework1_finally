print("Hello there! This program converts kilometers into miles")

while True:
    print("Enter the km you want to convert")

    km = float(input("Kilometers: "))

    miles = km * 0.62137119

    print("{0} kilometers is {1} miles.".format(km, miles))

    bruno = input("Would you like to do another Conversion? Please answer y/n")
    if bruno != "y":
        print("Goodbye")
        break