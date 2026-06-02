"""
This is a worked example. This code is starter code; you should edit and run it to 
solve the problem. You can click the blue show solution button on the left to see 
the answer if you get too stuck or want to check your work!
"""

# Write your function here!

def main():
    num = int(input("Enter a number: "))
    # Call your function here with `num` as a parameter!
    print(f"Here are the divisors of {num}")
    find_divisors(num)
def find_divisors(num):
    for i in range(1,num+1):
        if num%(i)==0:
            print(i)
# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()
