import random

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
    guess = 0
    guess_num = get_integer_input("\nHow many guesses do you want? \n", "A whole number betweem 1 and 100", 0,100)
    lowest_num = get_integer_input("\nWhat do you want the lowest number to be? \n", "enter a whole number between 1 and 1000000", 0,1000000)
    highest_num = get_integer_input("\nwhat do you want the highest number to be? \n", "enter a whole number between 1 and 1000000", 0,1000000)
    num = random.randrange(lowest_num, highest_num + 1) 
    inp = get_integer_input("\nwhat number are you guessing? \n","that is not a valid guess", lowest_num, highest_num)
    while inp != num:
        if inp < num:
            guess += 1
            print("too low")
            inp = get_integer_input("\nwhat number are you guessing? \n","that is not a valid guess", lowest_num, highest_num)
        if inp > num:
            guess += 1
            print("too high")
            inp = get_integer_input("\nwhat number are you guessing? \n","that is not a valid guess", lowest_num, highest_num)
        if guess == guess_num:
            print("you ran out of guesses \n try again")
            break
        if inp == num:
            print(f"you got the number in {guess} guesses")
            break
