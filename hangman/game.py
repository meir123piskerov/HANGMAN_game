

def init_state(secret: str, max_tries: int) -> dict:
    display = []
    for chart in range(len(secret)):
         display.append("_")
    game = {"secret": secret,
            "display": display,
            "guessed": [],
            "wrong_guesses": 0,
            "max_tries": max_tries
             }
    return game
def validate_guess(ch: str, guessed: set[str]) -> tuple[bool, str]:
    if len(ch) == 1:
        if ch in guessed:
            return True, "already enter that input!!"
        if ch not in guessed:
            return False, "not in the word try again"
    else:
        return False, "Invalid input"


def apply_guess(state: dict, ch: str) -> bool:
    state["guessed"].append(ch)
    if ch in state["secret"]:
        for i in range(len(state["secret"])):
            if state["secret"][i] == ch:
                state["display"][i] = ch
        return True
    else:
        state["wrong_guesses"] += 1
        return False


def is_won(state: dict) -> bool:
    if state["secret"] == "".join(state["display"]):
        return True

def is_lost(state: dict) -> bool:
    if state["wrong_guesses"] == state["max_tries"]:
        return True
    else:
        return False

def render_display(state: dict) -> str:
    for chart in state["secret"]:
        return chart

def render_summary(state: dict) -> str:
    return state["secret"] + state["guessed"]





