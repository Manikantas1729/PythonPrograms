'''
# Pythons are first class objects. This means that functions can be passed around
and used as arguments just like any other objects(string, int, float etc).

'''

def play(game):
    return f'Lets play {game}'

def win(game):
    return f"lets have a {game} contest and win."

#N Note that only refeence to the fucntion "invite_func" is passed, note no parenthesis.
def invite(invite_func):
    return invite_func("cricket")

print(invite(play))
# prints --> Lets play cricket
print(invite(win))
# prints --> lets have a cricket contest and win.
