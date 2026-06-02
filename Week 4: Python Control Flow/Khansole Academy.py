import random

def main():
    print("Khansole Academy")
    # TODO: your code here
    num1=random.randint(10,99)
    #print(num1)
    num2=random.randint(10,99)
    print(f"What is {num1} + {num2}?")
    user_ans=int(input("Your answer: "))
    correct_ans=num1+num2
    if user_ans==correct_ans:
        print("Correct!")
    else:
        print("Incorrect.")
        print(f"The expected answer is {correct_ans}")


if __name__ == '__main__':
    main()
