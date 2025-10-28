import random
def choose_secret_word(words: list[str]) -> str:
    len_word = len(words)
    word = random.randint(0, len_word)
    secret_word = words[word]
    return secret_word
