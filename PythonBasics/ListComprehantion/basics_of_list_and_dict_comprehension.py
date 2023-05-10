# new_list = [new_item for item in list]
# new_list = [new_item for item in list if test]
# new_dict = {new_key:new_value for item in list} ???
# new_dict = {new_key:new_value for (key, value) in dict.items()}
# python sequences - specific order list, tuple,  range, string


numbers = [1, 2, 3]
new_list = [n + 1 for n in numbers]

name = 'Angela'
new_list = [letter for letter in name]
print(new_list)

print(range(1, 5))
lab = [n**2 for n in range(1, 5)]
print(lab)
names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Elanor', 'Freddie']
short_names = [name for name in names if len(name) < 5]
print(short_names)
long_names = [name.upper() for name in names if len(name) > 5]
print(long_names)

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_numbers = [num**2 for num in numbers]
print(squared_numbers)
odd_numbers = [num for num in numbers if num % 2 == 0]
print(odd_numbers)


import random
numbers = [random.randint(0, 100) for _ in range(50)]
numbers_1 = [random.randint(0, 100) for _ in range(50)]
print(numbers, numbers_1)
same_numbers = [number for number in numbers if number in numbers_1]
print(same_numbers)

new_dict = {name: random.randint(1, 5) for name in names}
passed_students = {name: value for name, value in new_dict.items() if value > 3}

sentence = "What is the Airspeed Velosity of an Unladen Swallow?"
word_letter = {word : len(word) for word in sentence.split()}
print(word_letter)
weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24
}
weather_F = {day: (temp*9/5) + 32 for day, temp in weather_c.items()}
print(weather_F)


import pandas

student_dict = {
    "student": ["Angela", "James", "Lily"],
    'score': [56, 75, 98]
 }
student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)

for (index, row) in student_data_frame.iterrows():
    # print(row)
    # print(row.student)
    if row.student == 'Angela':
        print(row.score)