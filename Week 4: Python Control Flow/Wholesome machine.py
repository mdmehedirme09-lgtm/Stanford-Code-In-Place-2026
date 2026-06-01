"""
This is a worked example. This code is starter code; you should edit and run it to 
solve the problem. You can click the blue show solution button on the left to see 
the answer if you get too stuck or want to check your work!
"""

AFFIRMATION = "I am capable of doing anything I put my mind to."

def main():
    user_input = ""

    while user_input != AFFIRMATION:
        print("Please type the following affirmation: " + AFFIRMATION)
        user_input = input()

        if user_input == AFFIRMATION:
            print("That's right! :)")
        else:
            print("That was not the affirmation.")


# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()
