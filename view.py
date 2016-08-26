def greeting():
    return input("How many sides of dice are there? ")

def create_dice(dice_class, sides):
    print("created a {sided} dice".format(sided=sides))
    return dice_class(sides)

def give_user_directions():
    return print("press 'enter' to roll the dice, type 'stop' to stop rolling")

def format_roll_result(result):
    print("rolled a {result}".format(result=result))
