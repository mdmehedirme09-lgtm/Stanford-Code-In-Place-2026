import random

def main():
    sides=input("How many sides does your dice have? ")
    sides=int(sides)
    roll=random.randint(1,sides)
    print("Your roll is",roll)


if __name__ == '__main__':
    main()
