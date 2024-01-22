#
#
# By Aahan 1/22/24

def is_divisible(number ,divisor ):
    result = number % divisor
    if result == 0:
        return True
    else:
        return False

number = int(input("What is the number: "))
divisor = int(input("What is the divisor: "))

if is_divisible(number, divisor) == True:
    print(str(number) + " is divisible by " + str(divisor))
else:
    print(str(number) + " is NOT divisible by " + str(divisor))


