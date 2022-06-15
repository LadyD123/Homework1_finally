stop = input ("Please enter a number between 1 and 100:")
stop =int(stop)
for homework in range (1,stop+1):
    if homework %3 ==0 and homework %5 ==0:
        print ("fizzbuzz")
    elif homework % 3== 0:
        print("fizz")
    elif homework % 5 ==0:
        print ("buzz")
    else:
        print(homework)

