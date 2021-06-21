from random import choice

ai_choices = ['rock', 'paper', 'scissors']
def get_integer_input(message, error, low, high):
    while True:
        try:
            inpt = int(input(message))
            if low < inpt < high:
                return inpt
            else:
                print(error)
        except ValueError:
            print(error)


while True:
    choices = ['rock', 'paper', 'scissors']
    print('''
    ~
    ~
    ~
    **********welcome to rock paper scissors your favorite childhood game*******************
    ~      
    ~    
    ~    
    ''')
    while True:
        gamemode = get_integer_input("\nWhat gamemode do you want today \nif you want a single game write 1\nif you want endless write 2 \n", "that is not one of the game modes\n", 0 , 3)
        ai_choice = choice(ai_choices)
        human_choice = get_integer_input("\nwhat do you want if rock write 1, if paper write 2 or if scissors write 3 and write 4 to exit the game\n", "that is not an option", 0,5)
        while gamemode == 2:
            if human_choice == 1:
                if ai_choice == 'rock':
                    print("The ai choose rock its a tie")
                if ai_choice == 'scissors':
                    print("The ai choose scissors you won good job")
                if ai_choice == 'paper':
                    print("The ai choose paper you lost try again")
            if human_choice == 2:
                if ai_choice == 'rock':
                    print("The ai choose rock you won good job")
                if ai_choice == 'scissors':
                    print("The ai choose scissors you lost try again")
                if ai_choice == 'paper':
                    print("The ai choose paper its a tie")
            if human_choice == 3:
                if ai_choice == 'rock':
                    print("The ai choose rock you lost try again")
                if ai_choice == 'scissors':
                    print("The ai choose scissors its a tie")
                if ai_choice == 'paper':
                    print("The ai choose paper you won good job") 
            if human_choice == 4:
                print("have a good day and hope you come back again")
            break