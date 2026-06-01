"""
This is a worked example. This code is starter code; you should edit and run it to 
solve the problem. You can click the blue show solution button on the left to see 
the answer if you get too stuck or want to check your work!
"""

def main():
    degrees_fahrenheit=float(input("Enter temperature in Fahrenheit: "))
    degrees_celsius = (degrees_fahrenheit - 32) * 5.0/9.0
    print(f"Temperature: {degrees_fahrenheit}F = {degrees_celsius}C")
  

# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()
