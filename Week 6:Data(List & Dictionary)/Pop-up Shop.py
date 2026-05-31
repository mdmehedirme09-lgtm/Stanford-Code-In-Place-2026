"""
This is a worked example. This code is starter code; you should edit and run it to 
solve the problem. You can click the blue show solution button on the left to see 
the answer if you get too stuck or want to check your work!
"""

def main():
    # fruits is a dictionary with keys being fruit names and values being the price of the corresponding fruit
    fruits = {'apple': 1.5, 'durian': 50, 'jackfruit': 80, 'kiwi': 1, 'rambutan': 1.5, 'mango': 5}
    
    # Write your code here!
    total=0
    for keys in fruits:
        number=0
        number=int(input(f"How many ({keys}) do you want to buy?: "))
        
        total+=number*fruits[keys]

    print(f"Your total is ${total}")

# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()
