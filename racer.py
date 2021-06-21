import random
import os

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

def roll_dice():
    return random.randint( 1, 6)

car_choice = get_integer_input("choose a car\n","that is not one of the cars", 0,7)
race_distance = get_integer_input("what distance do you want between 5 and 15 \n","thats not a number between 5 and 15",4,16)
print(roll_dice())
cars = [0, 0, 0, 0, 0, 0]
os.system('cls')
while max(cars) < race_distance:
    for i, car in enumerate (cars):
        print('_'*car + 'o-o')
    input("push enter to continue")
    os.system('cls')
    cars[roll_dice()-1] +=1
