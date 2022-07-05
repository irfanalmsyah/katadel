import random
import sys
import requests
import words
import colorama
from colorama import Back
colorama.init(autoreset=True)


# Validates if the word has KBBI description or not
# so the user will not get a random unknown word
def validation(x):
    try:
        r = requests.get(url=f'https://new-kbbi-api.herokuapp.com/cari/{x}')
        description = r.json()['data'][0]['arti'][0]['deskripsi']
    except:
        return False
    return description


# Compare the inputted word with correct word
# The list that it return will decide the color for user inputted word later
def check(input_word, word):
    check_list = []
    i = 0
    while i < 5:
        if input_word[i] == word[i]:
            check_list.append('G')
        elif input_word[i] in word:
            check_list.append('B')
        else:
            check_list.append('R')
        i += 1
    return check_list


WORDS = words.WORDS
word_result = ''

while True:
    x = input('\nSelamat datang di Katadel 5 huruf! Apakah kamu ingin bermain? (Y/N)\n')
    if x == 'N' or x == 'n':
        sys.exit()
    elif x == 'Y' or x == 'y':
        print("\nSelamat bermain! Inputkan 'clue' untuk mendapatkan clue. Inputkan 'help' untuk mendapatkan petunjuk\nHarap tunggu beberapa saat...")
        while True:
            word = random.choice(WORDS)
            valid = validation(word)
            if valid:
                break

        turn = 1
        while turn < 6:
            while True:
                input_word = (input(f'\nTebakan ke-{turn}: ')).lower()
                if input_word == 'clue':
                    print(valid)
                elif input_word == 'help':
                    print('Hijau berarti huruf tersebut benar dan posisinya benar\nBiru berarti huruf tersebut benar tetapi posisinya salah\nMerah berarti huruf tersebut salah')
                elif input_word.isalpha() is False or len(input_word) != 5:
                    print('Input yang diperbolehkan hanya 5 huruf')
                elif input_word not in WORDS:
                    print('Kata tersebut tidak ada dalam KBBI')
                else:
                    break
            result = check(input_word, word)
            i = 0
            while i < 5:
                if result[i] == 'G':
                    word_result += Back.GREEN + input_word[i]
                elif result[i] == 'B':
                    word_result += Back.BLUE + input_word[i]
                elif result[i] == 'R':
                    word_result += Back.RED + input_word[i]
                i += 1
            print(word_result)
            word_result = ''
            if result == ['G', 'G', 'G', 'G', 'G']:
                print(f'Kamu menang!\nJawabannya adalah: {word.upper()}')
                break
            if turn == 5:
                print(f'\nKamu kehabisan kesempatan :( \nJawabannya adalah: {word.upper()}')
                break
            turn += 1
    else:
        print("\nInput Kamu tidak dapat dipahami")
