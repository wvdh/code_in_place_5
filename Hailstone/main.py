"""
Hailstone is a program that reads in a number from the user
and then displays the Hailstone sequence for that number,
just as in Hofstadter"s book, followed by a line showing
the number of steps taken to reach 1.
"""

def main():
    """
    Have the user input a positive integer, call it n.
    If n is even, divide it by two.
    If n is odd, multiply it by three and add one.
    Continue this process until n is equal to one.
    """
    n = int(input("Enter a number: "))
    while n != 1:
        # What is the remainder when n is divided by 2?
        # If the remainder is 1, then n was odd.
        remainder = n % 2
        if remainder == 1:
            print(f"{n} is odd, so I make 3n + 1: {3 * n + 1}")
            n = ((3 * n) +1)
        else:
            print(f"{n} is even, so I take half: {int(n / 2)}")
            n = int(n / 2)

# necessary boilerplate to start execution
if __name__ == "__main__":
    main()