x = int(input("Gib eine Zahl ein:"))
y = int(input("Gib eine weitere Zahl ein:"))

operation = input("Wie möchtest du rechnen?:")

if operation == "+":
    print(x+y)
elif operation == "-":
    print(x-y)
elif operation == "/":
    print(x/y)
elif operation == "*":
    print(x*y)
else:
    print ("Das gibt es doch gar nicht!")