from model import Dice
from view import greeting, create_dice, give_user_directions, format_roll_result

sides = int(greeting())

dice = create_dice(Dice, sides)

give_user_directions()

while True:
    command = input()

    if command == "stop":
        break
    else:
        format_roll_result(dice.roll())