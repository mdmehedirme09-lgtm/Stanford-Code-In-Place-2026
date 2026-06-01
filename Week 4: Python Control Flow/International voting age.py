"""
This is a worked example. This code is starter code; you should edit and run it to 
solve the problem. You can click the blue show solution button on the left to see 
the answer if you get too stuck or want to check your work!
"""

PETURKSBOUIPO_AGE = 16
STANLAU_AGE = 25
MAYENGUA_AGE = 48

def main():
    age=int(input(("How old are you? ")))
    if age>=48:
        print(f"You can vote in Peturksbouipo where the voting age is 16.")
        print(f"You can vote in Stanlau where the voting age is 25.")
        print(f"You can vote in Mayengua where the voting age is 48.")
    elif age>=25 and age<48:
        print(f"You can vote in Peturksbouipo where the voting age is 16.")
        print(f"You can vote in Stanlau where the voting age is 25.")
        print(f"You cannot vote in Mayengua where the voting age is 48.")
    else:
        print('You can vote in Peturksbouipo where the voting age is 16.') 
        print('You cannot vote in Stanlau where the voting age is 25.') 
        print('You cannot vote in Mayengua where the voting age is 48.')


# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()
