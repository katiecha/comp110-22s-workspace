"""EX02 - One shot wordle!"""
__author__ = "730460523"

# Setting secret word.
secret_word: str = "python"
len_word: int = len(secret_word)

# Defining constants.
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

# Processing user input.
guess: str = (input(f"What is your {len_word}-letter guess? "))
while len(guess) != len_word:
    guess = input(f"That was not {len_word} letters! Try again: ")

# Preparing hint.
i: int = 0
hint: str = ""
while i < len_word:
    # Character is in the string in the exact index.
    if guess[i] == secret_word[i]:
        hint += GREEN_BOX
    # Charater is not in the string in the exact index.
    else:
        existence: bool = False
        alt_i: int = 0
        # Checking existance until through length of string.
        while existence is not True and alt_i < len(secret_word):
            if guess[i] == secret_word[alt_i]:
                existence = True
            else:
                alt_i += 1
        # Character is somewhere in the string.
        if existence is True:
            hint += YELLOW_BOX
        # Character is not in string.
        else:
            hint += WHITE_BOX
    i += 1

# Providing feedback.  
print(hint)
if guess == secret_word:
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")