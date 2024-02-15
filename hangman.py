import random

HANGMAN_PICS = [r"""
+--+
|  |
   |
   |
   |
   |
====""",
                r"""
                
                +--+
                |  |
                O  |
                   |
                   |
                   |
                ====""",
                r"""
                +--+
                |  |
                O  |
                |  |
                   |
                   |
                ====""",
                r"""
                    +--+
                    |  |
                    O  |
                   /|  |
                       |
                       |
                    ====""",
                r"""
                    +--+
                    |  |
                    O  |
                   /|\ |
                       |
                       |
                    ====""",
                r"""
                    +--+
                    |  |
                    O  |
                   /|\ |
                   /   |
                       |
                    ====""",
                r"""
                    +--+
                    |  |
                    O  |
                   /|\ |
                   / \ |
                       |
                    ===="""]

CATEGORY = 'Животные'

WORDS = 'орангутан крокодил лошадь обезьяна попугай пингвин кролик бегемот буревестник ондатра альбатрос'.split()


def main():
    missedLetters = []
    correctLetters = []
    rightWord = random.choice(WORDS)

    while True:
        draw_hangman(missedLetters, correctLetters, rightWord)
        guess = get_player_guess(missedLetters + correctLetters)
        if guess in rightWord:
            correctLetters.append(guess)
            foundAllLetters = True
            for rightLetter in rightWord:
                if rightLetter not in correctLetters:
                    foundAllLetters = False
                    break
            if foundAllLetters:
                print(f"Загаданное слово: {rightWord}")
                print("Вы победили!")
                break
        else:
            missedLetters.append(guess)
            if len(missedLetters) == len(HANGMAN_PICS) - 1:
                draw_hangman(missedLetters, correctLetters, rightWord)
                print("Количество попыток закончилось")
                print(f"Загаданное слово:{rightWord}")
                break


def draw_hangman(missedLetters, correctLetters, rightWord):
    print(HANGMAN_PICS[len(missedLetters)])
    print("Слова из группы:", CATEGORY)
    print()

    print('Неправильные буквы:', end=' ')
    for letter in missedLetters:
        print(letter, end=' ')
    print()

    blanks = ['_'] * len(rightWord)

    for i in range(len(rightWord)):
        if rightWord[i] in correctLetters: blanks[i] = rightWord[i]

    print(" ".join(blanks))


def get_player_guess(alredyGuessed):
    while True:
        print("Введите букву:")
        letter = input().lower()
        if len(letter) != 1:
            print("Введите только одну букву")
        elif letter in alredyGuessed:
            print("Вы уже вводили эту букву")
        else:
            return letter


main()
