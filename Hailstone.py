"""
Write a program that implements the following process.
Have the user input a positive integer, call it n.
If n is even, divide it by two.
If n is odd, multiply it by three and add one.
Continue this process until n is equal to one.
"""

def main():
    # your code here
    n=int(input("Enter a number: "))
    while(n>1):
        if check_odd(n):
            #n=3*n+1
            print(f"{n} is odd, so I make 3n + 1: {3*n+1}")
            n=3*n+1
        if check_even(n):
            #n=int(n/2)
            print(f"{n} is even, so I take half: {int(n/2)}")
            n=int(n/2)


def check_odd(n):
    if n%2!=0:
        return True
def check_even(n):
    if n%2==0:
        return True
if __name__ == "__main__":
    main()
