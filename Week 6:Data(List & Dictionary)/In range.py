"""
This is a worked example. This code is starter code; you should edit and run it to 
solve the problem. You can click the blue show solution button on the left to see 
the answer if you get too stuck or want to check your work!
"""

def in_range(n, low, high):
    """
    Returns True if n is between low and high, inclusive.
    high is guaranteed to be greater than low.
    """
    if (n >= low) and (n <= high):
        return True
    
# There is no need to edit code beyond this point

def main():
	n = input("n: ")
	low = input("low: ")
	high = input("high: ")
	if in_range(n, low, high):
		print("n is in range!")
	else:
		print("n is not in range...")


if __name__ == '__main__':
    main()
