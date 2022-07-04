import random
import sys
import requests
import words
import colorama
from colorama import Back
colorama.init(autoreset=True)

def validation(x):
    try:
        r = requests.get(url = f'https://new-kbbi-api.herokuapp.com/cari/{x}')
        deskripsi = r.json()['data'][0]['arti'][0]['deskripsi']
    except:
        return False
    return deskripsi

def check(userInput, word):
    checkList = []
    i = 0
    while i < 5:
        if userInput[i] == word[i]:
            checkList.append('G')
        elif userInput[i] in word:
            checkList.append('B')
        else:
            checkList.append('R')
        i += 1
    return checkList

WORDS = words.WORDS
wordResult = ''

while True:
    x = input('\nSelamat datang di Katadel 5 huruf! Apakah kamu ingin bermain? (Y/N)\n')
    if x == 'N' or x == 'n':
        sys.exit()
    elif x == 'Y' or x == 'y':
        print("\nSelamat bermain! Inputkan 'clue' untuk mendapatkan clue. Inputkan 'help' untuk mendapatkan petunjuk\nHarap tunggu beberapa saat...")
        while True:
            word = random.choice(WORDS)
            valid = validation(word)
            if valid != False:
                break

        turn = 1
        while turn < 6:
            while True:
                userInput = (input(f'\nTebakan ke-{turn}: ')).lower()
                if userInput == 'clue':
                    print(valid)
                elif userInput == 'help':
                    print('Hijau berarti huruf tersebut benar dan posisinya benar\nBiru berarti huruf tersebut benar tetapi posisinya salah\nMerah berarti huruf tersebut salah')
                elif userInput.isalpha() == False or len(userInput) != 5:
                    print('Input yang diperbolehkan hanya 5 huruf')
                elif userInput not in WORDS:
                    print('Kata tersebut tidak ada dalam KBBI')
                else:
                    break
            result = check(userInput, word)
            i = 0
            while i < 5:
                if result[i] == 'G':
                    wordResult += Back.GREEN + userInput[i]
                elif result[i] == 'B':
                    wordResult += Back.BLUE + userInput[i]
                elif result[i] == 'R':
                    wordResult += Back.RED + userInput[i]
                i += 1
            print(wordResult)
            wordResult = ''
            if result == ['G', 'G', 'G', 'G', 'G']:
                print(f'Kamu menang!\nJawabannya adalah: {word.upper()}')
                break
            if turn == 5:
                print(f'\nKamu kehabisan kesempatan :( \nJawabannya adalah: {word.upper()}')
                break
            turn += 1
    else:
        print("\nInput Kamu tidak dapat dipahami")

    





