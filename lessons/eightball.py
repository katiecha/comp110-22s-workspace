"""A magic 8 ball oracle of truth about the future."""

from random import randint

input("Ask a yes or no quesion: ")

response: int = randint(0, 3)

if response == 0:
    print("Yes, definitely!")
elif response == 1:
    print("Looking hopeful.")
elif response == 2:
    print("Ask again laer.")
else:
    print("No way. Not a change.")

