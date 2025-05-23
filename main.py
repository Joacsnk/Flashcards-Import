from os import system as sy
flashcard = str("")
while True:
    sy("cls")
    word = str(input("word: "))
    if word == "0":
        break
    sy("cls")
    explanation = str(input("explanation: "))
    sy("cls")
    flashcard += (word + "," + explanation + ";")
sy("cls")
print(flashcard)