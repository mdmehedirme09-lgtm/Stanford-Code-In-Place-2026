import random

NUM_ROUNDS = 5

def main():
    print("Welcome to the High-Low Game!")
    print('--------------------------------')

    # TODO: Write your code here!!! :)
    # NOTE: For the autograder to work, you must generate the
    # COMPUTER's number FIRST, then the user's

    score=0
    Your_number=0
    comparison=""
    i=1
    for i in range(NUM_ROUNDS):
        print(f"Round {i+1}")
        Computers_number=random.randint(1,100)
        Your_number=random.randint(1,100)
        print(f"Your number is {Your_number}")
        comparison=input("Do you think your number is higher or lower than the computer's?: ")

        if Your_number<Computers_number and comparison=='lower':
            score+=1
            print(f"You were right! The computer's number was {Computers_number}")
            print(f"Your score is now {score}")

        elif Your_number>Computers_number and comparison=='higher':
            score+=1
            print(f"You were right! The computer's number was {Computers_number}")
            print(f"Your score is now {score}")

        else:
            print(f"Aww, that's incorrect. The computer's number was {Computers_number}")
            print(f"Your score is now {score}")
        
        
        print()
    print()
    print("Thanks for playing!")

    
if __name__ == "__main__":
    main()
