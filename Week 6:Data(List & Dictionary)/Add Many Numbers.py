"""
This is a worked example. This code is starter code; you should edit and run it to 
solve the problem. You can click the blue show solution button on the left to see 
the answer if you get too stuck or want to check your work!
"""

def add_many_numbers(numbers):
    """
    Takes in a list of numbers and returns the sum of those numbers.
    """
    sum=0
    for i in range(len(numbers)):
        sum+=numbers[i]
    return sum
# There is no need to edit code beyond this point

def main():
    numbers = [1, 2, 3, 4, 5]  # Make a list of numbers
    sum_of_numbers = add_many_numbers(numbers)  # Find the sum of the list
    print(sum_of_numbers)  # Print out the sum above
    

if __name__ == '__main__':
    main()
