from hangmanStages import stages
from Words import word_list
import random


def PrintHangmanStage():
    print(stages[6])


def GetRandomWordfromList():
    global word
    word = random.choice(word_list).upper()


def GetWordIndices(word, guess):
    indices = []
    for index, letter in enumerate(word):
        if letter == guess:
            indices.append(index)

    return indices


def Play():
    word_was_guessed = False
    remaining_tries = 6
    hidden_letter_symbol = "_"
    word_completion = hidden_letter_symbol * len(word)
    word_completion_list = list(word_completion)
    lastGuess = ""

    while not word_was_guessed and remaining_tries > 0:

        guess = input("Buchstabe oder Wort eingeben: ").upper()

        if guess not in word:
            if lastGuess == guess:
                print("Du hast", guess, "schon mal versucht")
                remaining_tries -= 1
                print(stages[remaining_tries])
            else:
                lastGuess = guess
                print("Das gesuchte Wort enthält den Buchstaben", guess, "nicht.")
                remaining_tries -= 1
                print(stages[remaining_tries])
                if remaining_tries == 0:
                    print("Verloren!")

        elif guess in word:
            if guess == word:
                print(stages[remaining_tries])
                print(word)
                print("Glückwunsch!")
                word_was_guessed = True
            else:
                print(f"Das gesuchte Wort enthält den Buchstaben '{guess}'.")
                print(stages[remaining_tries])
                index = GetWordIndices(word, guess)
                for indices in index:
                    word_completion_list[indices] = guess
                print("".join(word_completion_list))

                if "".join(word_completion_list) == word:
                    print("Glückwunsch!")
                    word_was_guessed = True


PrintHangmanStage()
print("Willkommen zu Galgenmännchen")
GetRandomWordfromList()
Play()
