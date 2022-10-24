from hangmanStages import stages
import random


def PrintHangmanStage():
    print(stages[6])


def GetRandomWordfromList():
    word_list = ["Giraffe", "Zebra", "Hund", "Katze"]
    word = random.choice(word_list).upper()

    return word


def GetWordIndices(word, guess):
    indices = []
    for index, letter in enumerate(word):
        if letter == guess:
            indices.append(index)

    return indices


def Play():

    word = GetRandomWordfromList()
    word_was_guessed = False
    remaining_tries = 6
    hidden_letter_symbol = "_"
    word_completion = hidden_letter_symbol * len(word)
    word_completion_list = list(word_completion)
    lastGuess = ""

    PrintHangmanStage()

    print("Willkommen zu Galgenmännchen")

    while not word_was_guessed and remaining_tries > 0:

        guess = input("Buchstabe oder Wort eingeben: ").upper()

        if lastGuess == guess:
            print("Du hast", guess, "schon mal versucht")
            remaining_tries -= 1
            print(stages[remaining_tries])
        elif guess not in word:
            lastGuess = guess
            print("Das gesuchte Wort enthält den Buchstaben", guess, "nicht.")
            remaining_tries -= 1
            print(stages[remaining_tries])
        elif guess in word:
            print(f"Das gesuchte Wort enthält den Buchstaben '{guess}'.")
            print(stages[remaining_tries])
            index = GetWordIndices(word, guess)
            for indices in index:
                word_completion_list[indices] = guess
            print("".join(word_completion_list))

        if guess == word or "".join(word_completion_list) == word:
            break

    if remaining_tries == 0:
        print("Verloren!")
    else:
        print(stages[remaining_tries])
        print(word)
        print("Glückwunsch!")
        word_was_guessed = True


Play()

while True:
    decision = input("Noch eine Runde? Dann bestätige mit 'JA': ").upper()
    if decision == "JA":
        Play()
    else:
        print("Auf Wiedersehen!")
        break
