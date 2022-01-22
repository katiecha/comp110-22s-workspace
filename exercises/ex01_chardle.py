"""EX01 - Chardle - A cute step toward Wordle."""
__author__ = "730460523"

word: str = input("Enter a 5-character word: ")
if len(word) != 5:
    print("Error: Word must contain 5 characters")
    exit()

ch: str = input("Enter a single character: ")
if len(ch) != 1:
    print("Error: Character must be a single character.")
    exit()

print("Searching for " + ch + " in " + word)

i: int = 0
counter: int = 0
while i < 5:
    if word[i] == ch:
        index: str = str(i)
        print(ch + " found at index " + index)
        counter = counter + 1
        i = i + 1
    else:
        i = i + 1

if counter == 0:
    print("No instances of " + ch + " found in " + word)
else:
    if counter == 1:
        print("1 instance of " + ch + " found in " + word)
    else:
        print(str(counter) + " instances of " + ch + "found in " + word)
    