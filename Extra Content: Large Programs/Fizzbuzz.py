MAX_VALUE = 17

def main():
    # modify this starter code to call fizzbuzz
    # on every number from 1 to MAX_VALUE
    for i in range(MAX_VALUE):
        to_say = fizzbuzz(i+1)
        print(to_say)

def fizzbuzz(n):
    """
    Takes in a positive integer (n) and returns
    what the player should say at that value.
    Here are a few examples:
    fizzbuzz(3) returns "Fizz"
    fizzbuzz(15) returns "Fizzbuzz"
    fizzbuzz(2) returns 2
    """
    # TODO: fill in this function
    if n%3==0 and n%5==0:
        return "Fizzbuzz" 
    elif n%3==0:
        return "Fizz"
    elif n%5==0:
        return "Buzz"
    else:
        return n

    return n

if __name__ == '__main__':
    main()
