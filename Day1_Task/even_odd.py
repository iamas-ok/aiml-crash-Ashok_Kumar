# printeven Odd number program that handles invalid input.
try:
    num = int(input('Enter a Number : '))
    if num == 0:
        print("Number is Zero!")
    elif num % 2 == 0:
        print("This is EVEN")
    else:
        print("This is ODD")
except Exception as e:
    print('Enter a valid number!!')
