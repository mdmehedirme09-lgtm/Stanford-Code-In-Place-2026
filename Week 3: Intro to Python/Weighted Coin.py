"""
This is a worked example. This code is starter code; you should edit and run it to 
solve the problem. You can click the blue show solution button on the left to see 
the answer if you get too stuck or want to check your work!
"""

import random

def weighted_coin():
    if random.random()<0.7:
        return "Heads"
    else:
        return "Tails"
def main():
    print(weighted_coin())

# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()
