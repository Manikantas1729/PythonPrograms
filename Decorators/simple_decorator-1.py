def my_decorator(func):
    def wrapper_my_decorator(*args, **kwargs): # args and kwargs to accept fn with args and kwargs
        print("Something before fucntion is called")
        func(*args, **kwargs)
        print("Something after funciton is called")
    return wrapper_my_decorator

@my_decorator # called pie syntac
def play_game(game):
    print(f"Lets play {game}")

play_game("cricket")