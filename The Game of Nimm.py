def main():
    """
    You should write your code here. 
    """
    STONE=20
    stone_left=STONE
    user_1=True
    last_pickup=True
    #user_2=True
    while stone_left>0:
        print(f"There are {stone_left} stones left.")
        #user_1=True
        if user_1==True:
            user_input=int(input("Player 1 would you like to remove 1 or 2 stones? "))
            while(user_input>2):
                user_input = int(input("Please enter 1 or 2: "))
            user_1=False
            user_2=True
            last_pickup=True
        
        elif user_2==True:
            user_input=int(input("Player 2 would you like to remove 1 or 2 stones? "))
            while(user_input>2):
                user_input = int(input("Please enter 1 or 2: "))
            user_2=False
            user_1=True
            last_pickup=False
        stone_left=stone_left-user_input
    if last_pickup==True:
        print('Player 2 wins!')
    else:
        print('Player 1 wins!')

if __name__ == '__main__':
    main()
