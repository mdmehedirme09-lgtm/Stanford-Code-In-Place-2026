import random

NUM_PAIRS = 3

def main():
    """
    You should write your code here. Make sure to delete 
    the 'pass' line before starting to write your own code.
    """
    lst=[]
    for i in range(NUM_PAIRS):
        lst.append(i)
        lst.append(i)
    #print(lst)
    random.shuffle(lst)
    #print(lst)

    displayed=[]
    for i in range(2*NUM_PAIRS):
        displayed.append('*')
    #print(displayed)

    #get_valid_index(displayed)

    while '*' in displayed:
        print(displayed)
        first = get_valid_index(displayed)
        second = get_valid_index(displayed)

        while second == first:
            print("You entered the same index twice. Try again.")
            second = get_valid_index(displayed)

        if lst[first] == lst[second]:
            displayed[first] = lst[first]
            displayed[second] = lst[second]
            print("Match!")
        else:
            print(f"Value at index {first} is {lst[first]}")
            print(f"Value at index {second} is {lst[second]}")
            print("No match. Try again.")
            input("Press Enter to continue...")
    print(displayed)
    print("Congratulations! You won!")
def clear_terminal():
    for i in range(20):
      print('\n')

def get_valid_index(displayed):

    while True:

        value = input("Enter an index: ")

        try:
            index = int(value)

            if index < 0 or index >= len(displayed):
                print("Invalid index. Try again.")

            elif displayed[index] != '*':
                print("This number has already been matched. Try again.")

            else:
                return index

        except:
            print("Not a number. Try again.")
if __name__ == '__main__':
    main()
