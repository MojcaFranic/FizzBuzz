x = int(raw_input("Vpisi stevilko med 1 in 100 "))

if x <= 100 and x >= 1:
    for x in range(1, x + 1):
        if x % 3 == 0 and x % 5 == 0:
            print ("FizzBuzz")
        elif x % 5 == 0:
            print("Buzz")
        elif x % 3 == 0:
            print("Fizz")
        else:
            print(x)
else:
    print("Stevilo ni med 1 in 100")
