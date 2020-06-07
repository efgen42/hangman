# -*- coding utf-8 -*-
"""
Hangman - игра, в которой игрок должен угадывать слово,
буква за буквой, в ограниченном количестве попыток.
"""
import random
words = ['python', 'java', 'kotlin', 'javascript']
index_list_open = []  # список угаданных букв
set_letters = set()  # множество всех названных букв
word = random.choice(words)
prompt = '-' * len(word)
print("H A N G M A N")
count = 8


def find_all(letter, word):
    # функция создаёт список индексов угаданных букв
    index_list = []
    i = word.find(letter)
    while i != -1:
        index_list.append(i)
        i = word.find(letter, i + 1, len(word))
        # print(f'i=  {i}')
    return index_list


while True:
    answer = str(input('Type "play" to play the game, "exit" to quit:'))
    if answer == 'exit':
        break
    elif answer == 'play':

        while count > 0:
            print(f"\n{prompt}")
            print(f"The number of remaining attempts: {count}")
            letter = input(str('Input a letter:'))
            if len(letter) != 1:
                print("You should input a single letter")
                continue
            if not (letter.isascii() and letter.islower()):
                print("It is not an ASCII lowercase letter")
                continue
            if not letter in set_letters:  # если не назывли эту букву - запоминаем её
                set_letters.add(letter)
            else:
                print("You already typed this letter")  # иначе возвращаемся в начало цикла с свыводом сообщения
                continue
                # print("Индекс угаданной буквы {}".format(find_all(letter, word)))
            if not find_all(letter, word):  # Если указанная буква отсутствует в слове
                print("No such letter in the word")
                count -= 1
                continue
            else:
                index_list_open += find_all(letter, word)  # список индексов угаданых букв
                # print(index_list_open)
                index_list_closed = set(range(len(word))) - set(index_list_open)  # множество индексов неуг. букв
            # print(f"Индексы неуг букв: {index_list_closed}")
            # print(f"prompt = {word}")
            prompt = word
            for i in index_list_closed:
                prompt = prompt.replace(word[i], '-')  # подготавливаем слово для вывода (j-v-)
            if prompt == word:
                print(f"\n{prompt}")
                print("You guessed the word!\nYou survived!")
                break
        else:
            print("You are hanged!")
