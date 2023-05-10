# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

import pandas as pd
alphabet_data = pd.read_csv("D:\\Pyhton_Dir\\Projects\\Working_repo\\ListComprehantion\\NatoAlphabet\\nato_phonetic_alphabet.csv")
# print(alphabet_data.head(5))

alphabet_dict = {row.letter: row.code for (_, row) in alphabet_data.iterrows()}
# print(alphabet_dict)


def generate_phonetic():
    word = input('Enter a word to spell: ')
    try:
        spelling = [alphabet_dict[letter.upper()] for letter in word]
    except KeyError:
        print('Please use only letters from eng alphabet')
        generate_phonetic()
    else:
        print(spelling)

generate_phonetic()

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
# input_list = list(input('Enter a word to spell: '))
# print(input_list)
# spelling = []
# got_a_word = False
# while not got_a_word:
#     try:
#         spelling = [alphabet_dict[letter.upper()] for letter in input_list]
#     except KeyError:
#         print('Please use only letters from eng alphabet')
#         input_list = list(input('Enter a word to spell: '))
#     else:
#         got_a_word = True
# print(spelling)
