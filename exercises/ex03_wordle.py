"""EX03 - Wordle with fuctions!"""
__author__ = "730460523"

# Defining constants.
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def main() -> None:
    """The entrypoint of the program and main game loop."""
    # Setting state of game (variables).
    secret_word: str = "codes"
    len_secret_word: int = len(secret_word)
    user_guess: str = ""
    emoji_hint: str = ""
    turns: int = 1

    while turns <= 6:
        print(f"=== Turn {turns}/6 ===")
        # Collecting the guess of the player.
        user_guess = input_guess(len_secret_word)
        # Producing a hint with colored emojis based on character existance.
        emoji_hint = emojified(user_guess, secret_word)
        print(emoji_hint)

        # Declaring whether the player won or not.
        if user_guess == secret_word:
            print(f"You won in {turns}/6 turns!")
            turns = 7
        elif user_guess != secret_word and turns < 6:
            turns += 1
        else:
            turns += 1
            print("X/6 - Sorry try again tomorrow!")


def contains_char(word: str, char: str) -> bool:
    """Determines if a word has a character in it."""
    assert len(char) == 1
    i: int = 0
    word_len = int(len(word))

    # Iteratively checks every character in the word.
    while i < word_len:
        if word[i] == char:
            return True
        else:
            i += 1
    return False


def emojified(guess: str, secret: str) -> str:
    """Produces an emoji hint."""
    assert len(guess) == len(secret)
    hint: str = ""
    count: int = 0
    guess_len = int(len(guess))

    # Uses contains_char function to check if the character is within the guess.
    while count < guess_len:
        if guess[count] == secret[count]:
            hint += GREEN_BOX
        elif contains_char(secret, guess[count]):
            hint += YELLOW_BOX
        else:
            hint += WHITE_BOX
        count += 1        
    return hint


def input_guess(length: int) -> str:
    """Collects input from user."""
    iguess: str = (input(f"Enter a {length} character word: "))
    # Assures the inputed guess will be the proper length of the secret word.
    while len(iguess) != length:
        iguess = input(f"That wasn't {length} chars! Try again: ")
    return(iguess)


if __name__ == "__main__":
    main()