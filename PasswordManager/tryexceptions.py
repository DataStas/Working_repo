# try something that might cause an cxception
# except do this if there was an exception
# else do this if there was no exception
# finally do this no matter what happens

# KeyError
# IndexError
# TypeError
# FileNotFound
# try: 
#     file = open("a_file.txt")
#     a_dictionary = {"key" : "value"}
#     print(a_dictionary["ssssaf"])
# except:
#     # do not use bare 'except'
#     file = open("a_file.txt", 'w')
#     file.write("Something")
#     print("There was an error")


# use specific situation
# try: 
#     file = open("a_file.txt")
#     a_dictionary = {"key": "value"}
#     print(a_dictionary["key"])
# except FileNotFoundError as error_message2:
#     # do not use bare 'except'
#     file = open("a_file.txt", 'w')
#     file.write("Something")
#     print(f"There was an error: {error_message2}")    
# except KeyError as error_message:
#     print(f"That key {error_message} does not exist.")
# else:
#     content = file.read()
#     print('file_content: ' + content + ' in else')
# finally:
#     file.close()
#     print('File was closed')



# Rising own exceptions 
# try: 
#     file = open("a_file.txt")
#     a_dictionary = {"key": "value"}
#     print(a_dictionary["key"])
# except FileNotFoundError as error_message2:
#     # do not use bare 'except'
#     file = open("a_file.txt", 'w')
#     file.write("Something")
#     print(f"There was an error: {error_message2}")    
# except KeyError as error_message:
#     print(f"That key {error_message} does not exist.")
# else:
#     content = file.read()
#     print('file_content: ' + content + ' in else')
# finally:
#     raise TypeError("This is an error that I made up")


# height = float(input('height '))
# weight = float(input('weight '))

# if height > 3:
#     raise ValueError("Human height should not be over 3 meters")

# if weight > 300:
#     raise ValueError("Human weight should not be over 3 meters")

# bmi = weight / height ** 2
# print(bmi)


# handle index error
# fruits = ["Apples", "Pear", "Orange"]

# # catch the exception and make sure the code runs without crashing
# def make_pie(index):
#     try:
#         fruit = fruits[index]
#     except IndexError as error_message:
#         print(f"You typed a wrong index and got {error_message}")
#     else:
#         print(fruit + " pie")


# make_pie(4)

# handle KeyError
# facebook_posts = [
#     {'Likes': 21, 'Comments': 2},
#     {'Likes': 21, 'Comments': 2, 'Shares': 1},
#     {'Likes': 21, 'Comments': 2, 'Shares': 2},
#     {'Comments': 2, 'Shares': 3},
#     {'Comments': 2, 'Shares': 1},
#     {'Likes': 21, 'Comments': 2}
# ]

# total_likes = 0
# for post in facebook_posts:
#     try:
#         total_likes = total_likes + post['Likes']
#     except KeyError:
#         pass

# print(total_likes)

# See NatoAlphabet
# def generate_phonetic():
#     word = input('Enter a word to spell: ')
#     try:
#         spelling = [alphabet_dict[letter.upper()] for letter in word]
#     except KeyError:
#         print('Please use only letters from eng alphabet')
#         generate_phonetic()
#     else:
#         print(spelling)

# generate_phonetic()