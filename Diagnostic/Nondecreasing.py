def main():
    # TODO write your solution here
    
    print("Enter a sequence of non-decreasing numbers.")
    temp=0
    length=0
    num=int(input("Enter num: "))
    length+=1
    temp=num
    while True:
        num=float(input("Enter num: "))
        
        if num>=temp:
            length+=1
        else:
            print("Thanks for playing!")
            print(f"Sequence length: {length}")
            return
        temp=num


if __name__ == "__main__":
    main()
