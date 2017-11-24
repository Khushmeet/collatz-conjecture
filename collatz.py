# naive implementation of collatz conjecture

# Recursion problem
def collatz_conjecture(number):
    """
    Collatz Conjecture
    number is even -> number/2
    number is odd -> 3number+1
    """
    if number == 1:
        print(number)
        print('On repeat from value 4, therefore returning!')
        return
    if number % 2 == 0:
        print(number)
        collatz_conjecture(number/2)
    else:
        print(number)
        collatz_conjecture((3*number)+1)

num = input('Enter number for collatz conjecture ')
collatz_conjecture(int(num))
