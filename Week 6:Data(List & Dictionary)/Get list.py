"""
This is a worked example. This code is starter code; you should edit and run it to 
solve the problem. You can click the blue show solution button on the left to see 
the answer if you get too stuck or want to check your work!
"""

def main():
    lst=[]
    elem=input("Enter a value: ")
    while elem!="":
        lst.append(elem)
        elem=input("Enter a value: ")
    print(f"Here's the list: {lst}")



# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()
