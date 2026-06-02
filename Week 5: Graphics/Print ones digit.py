"""
This is a worked example. This code is starter code; you should edit and run it to 
solve the problem. You can click the blue show solution button on the left to see 
the answer if you get too stuck or want to check your work!
"""

# Write your helper function here!

def main():
    num = int(input("Enter a number: "))
    # Call your helper function with `num` as a parameter!
    one_digit(num)
def one_digit(x):
    r=x%10
    print(f"The ones digit is {r}")
    
# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()
