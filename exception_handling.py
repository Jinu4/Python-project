def division(a, b):
    c = a // b
    print("Quotient is : ", c)


try:
    x = int(input("Enter dividend : "))
    y = int(input("Enter divisor : "))
    print(division(x, y))
except:
    print("Division using 0 not possible")
finally:
    print("*" * 5)
