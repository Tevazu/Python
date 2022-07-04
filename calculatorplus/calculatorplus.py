# You should put your module into the same folder with your program, so that you can use it like below
import math1
print(""" ___________________________________________________________________
|                                                                   |
|                 *** Welcome to calculatorplus ***                 |
|                                                                   |
| ce: To calculate the ceiling of your number.                      |
| fl: To calculate the floor of your number.                        |
| ra: To calculate the radian of a degree.                          |
| de: To calculate the degree of a radian.                          |
| sq: To calculate the square root of a number.                     |
| hy: To calculate the root of the two values' squares' sum.        |
| fa: To calculate the absolute value of a number.                  |
| fm: To calculate the remainder of the division of the num1 / num2.|
| fac: To calculate the factorial of a number.                      |
| sin: To calculate the sine of your number.                        |
| cos: To calculate the cosine of your number.                      |
| tan: To calculate the tangent of your number.                     |
|                                                                   |
 ___________________________________________________________________""")



letter = str(input("Which operation do you want to use?:"))

if (letter == 'sq'):

    while True:
        print("Type '0' to quit.")
        sayi = float(input("Enter the number:"))
        if (999999999 >= sayi > 0):
            print("The square root of your number is:", math1.sq(sayi))
        elif (sayi == 0):
            print("You quitted from the calculatorplus.")
            break

if (letter == 'ra'):

    while True:
        print("Type '0' to quit.")
        sayi = float(input("Enter a degree:"))
        if (999999999 >= sayi > 0):
            print("The radian of this degree is:", math1.ra(sayi))
        elif (sayi == 0):
            print("You quitted from the calculatorplus.")
            break

if (letter == 'ce'):
    while True:
        print("Type '0' to quit.")
        sayi = float(input("Enter the number:"))
        if (999999999 >= sayi > 0):
            print("The ceiling of your number is:", math1.ce(sayi))
        elif (sayi == 0):
            print("You quitted from the calculatorplus.")
            break

if (letter == 'fl'):
    while True:
        sayi = float(input("Enter the number:"))
        if (999999999 >= sayi > 0):
            print("The floor of your number is:", math1.fl(sayi))
        elif (sayi == 0):
            print("You quitted from the calculatorplus.")
            break

if (letter == 'de'):
    while True:
        print("Type '0' to quit.")
        sayi = float(input("Enter your radian:"))
        if (999999999 >= sayi > 0):
            print("The degree of this radian is:", math1.de(sayi))
        elif (sayi == 0):
            print("You quitted from the calculatorplus.")
            break

if (letter == 'hy'):
    while True:
        print("Type '0, 0' to quit.")
        sayi1 = float(input("Enter two numbers:"))
        sayi2 = float(input())
        if (999999999 >= sayi1 > 0 or 999999999 >= sayi2 > 0):
            print("The sum:", math1.hy(sayi1, sayi2))
        elif (sayi1 == 0 or sayi2 == 0):
            print("You quitted from the calculatorplus.")
            break

if (letter == 'fa'):
    while True:
        print("Type '0' to quit.")
        sayi = float(input("Enter the number:"))
        if ( sayi < 0 or sayi > 0):
            print("The absolute value of your number is:", math1.fa(sayi))
        elif (sayi == 0):
            print("You quitted from the calculatorplus.")
            break

if (letter == 'fm'):
    while True:
        print("Type '0, 0' to quit.")
        sayi1 = float(input("Enter two numbers:"))
        sayi2 = float(input())
        if (999999999 >= sayi1 > 0 or 999999999 >= sayi2 > 0):
            print("The remainder of your number is:", math1.fm(sayi1, sayi2))
        elif (sayi1 == 0 or sayi2 == 0):
            print("You quitted from the calculatorplus.")
            break

if (letter == 'fac'):
    while True:
        print("Type '0' to quit.")
        sayi = int(input("Enter a integer number:"))
        if (999999999 >= sayi > 0):
            print("The factorial of your number is:", math1.fac(sayi))
        elif (sayi == 0):
            print("You quitted from the calculatorplus")
            break

if (letter == "sin"):
    while True:
        print("Type '1.000.000.000' without dots to quit.")
        sayi = int(input("Enter a number:"))
        if (999999999 >= sayi > -999999999):
            print("Sine of your number is:", math1.sin(sayi))
        elif (sayi == 1000000000):
            print("You quitted from the calculatorplus.")
            break

if (letter == "cos"):
    while True:
        print("Type '1.000.000.000' without dots to quit.")
        sayi = int(input("Enter your number:"))
        if (999999999 >= sayi > -999999999):
            print("The cosine of your number is:", math1.cos(sayi))
        elif (sayi == 1000000000):
            print("You quitted from the calculatorplus.")
            break

if (letter == "tan"):
    while True:
        print("Type '1.000.000.000' without dots to quit.")
        sayi = int(input("Enter your number:"))
        if (999999999 >= sayi > -999999999):
            print("The tangent of your number is:", math1.tan(sayi))
        elif (sayi == 1000000000):
            print("You quitted from the calculator plus.")
            break


