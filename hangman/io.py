from hangman.game import *
def prompt_guess() -> str:
    input_word = input("guess a chart:")
    return input_word

def print_status(state: dict) -> None:
   print("guessed:", state["guessed"] , "wrong_guesses:",state["wrong_guesses"])

def render_summary(state: dict) -> str:
    summary = str(state["display"])
    return "word is:"  + state["secret"] +",\n," "guessed char are" + summary

def print_result(state: dict) :
    if is_won(state):
        print("You won!")
        return state
    if is_lost(state):
        print("You lost!")
        return state