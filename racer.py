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
def roll_two_dice():
    return roll_dice() + roll_dice()
cars = []
for i in range(12):
    cars.append(0)

car_choice = get_integer_input(f"choose a car between 1 and {len(cars)}\n","that is not one of the cars", 0,len(cars) + 1)
race_distance = get_integer_input("what distance do you want between 5 and 15 \n","thats not a number between 5 and 15",4,16)
print(roll_dice())
os.system('cls')
while len([i for i in cars if i >= 15]) < 3:
    for i, car in enumerate (cars):
        if i == car_choice - 1 and car < 15:
            print('_'*car + 'o-o')
    input("push enter to continue")
    os.system('cls')
    cars[roll_two_dice()-1] +=1

winning_car = cars.index(max(cars)) +1
print(f"car {winning_car} won")
if winning_car == car_choice:
    print("your car won")
else:
    print("your car didnt win") 
    for i, car in enumerate(positions):
        print(f"car number {car} came in position {i + 1}")