"""
This is a worked example. This code is starter code; you should edit and run it to 
solve the problem. You can click the blue show solution button on the left to see 
the answer if you get too stuck or want to check your work!
"""

def get_list_of_ints():
    """
    Reads in integers until the user presses enter and returns the resulting list.
    """
    lst = []
    user_input = input("Enter an integer or press enter to stop: ")
    while user_input != "":
        lst.append(int(user_input))
        user_input = input("Enter an integer or press enter to stop: ")

    return lst

def main():
    #print( "Enter an integer or press enter to stop: ")
    lst=get_list_of_ints()
    number_of_even=0

    for elem in lst:
        if elem%2!=0:
            number_of_even+=1

    print(number_of_even)
    


# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()
