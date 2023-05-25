# collatz.py
# Author: Asheley Mudzinwga
# Source: Automate the Boring Stuff Chpt 3 Project

def collatz(number):
    # If number is even (number//2) else (3*number+1)
    if number%2==0:
        print(number//2)
        return number//2

    else:
        print(3*number+1)
        return 3*number+1


if __name__ == '__main__':

    try:

        number = int(input('Enter a number: '))
        result = collatz(number)
        while (result != 1):
            result = collatz(result)

    except ValueError:
        print('Please Enter a Valid Number')
