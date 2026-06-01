"""
This is a worked example. This code is starter code; you should edit and run it to 
solve the problem. You can click the show solution button on the left to see 
the answer if you get too stuck or want to check your work!
"""
MIN_HEIGHT=50
def main():
    height=input("How tall are you? ")
    while height!="":
        height=float(height)
        if height<MIN_HEIGHT:
            print("You're not tall enough to ride, but maybe next year!")
            return
        if height>=MIN_HEIGHT:
            print("You're tall enough to ride!")
            return
        #height=input("How tall are you? ")-this is for the extension of this assignment



# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()
