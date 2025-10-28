import data.words
from hangman.words import *
from data.words import *
from hangman.game import *
from hangman.io import *




def play(words: list[str], max_tries: int = 6) -> None:
    word = choose_secret_word(words)
    print(word)
    status = init_state(word,max_tries)
    flag = True
    while flag:
        while status["wrong_guesses"] != status["max_tries"]:
            print_status(status)
            print(status["display"])
            render_display(status)
            ch = prompt_guess()
            valid = validate_guess(ch,status["guessed"])
            if valid == (True, "already enter that input!!"):
                print("already enter that input!!")
                break
            if valid == (False, "not in the word try again"):
                guess = apply_guess(status,ch)
                if guess:
                    print("correct")
                    break
                else:
                    print("try again")
                    break
        see_if_win = is_won(status)
        if see_if_win:
            flag =False
            break
        if status["wrong_guesses"] == status["max_tries"]:
            break
    print(render_summary(status))
    see_if_lose = is_lost(status)
    if see_if_lose:
        print(print_result(status))
    if not see_if_lose:
        print(print_result(status))




if __name__ == "__main__":
    play(data.words.words)





