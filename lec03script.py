def lec03script():
    num1 = input('Enter Number 1')
    num1 = float(num1)
    num2 = input('Enter Number 2')
    num2 = float(num2)
    oursum = num1 + num2

    if oursum >= 0:
        print('The sum is', oursum)
    elif oursum < 0:
        print('Output = ', 0)
    else:
        print('You inputted a string')


lec03script()
