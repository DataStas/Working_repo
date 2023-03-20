n_students = 7
sum_marks = 42
marks = [5, 3, 7, 6, 3, 10, 1]
max_marks = [5, 5, 9, 7, 8, 10, 1]
marks_zipped = list(zip(marks, max_marks))

""" dic_marks = {}
dic_max_marks = {}
for ind, mark in enumerate(marks):
    dic_marks[ind] = mark
    dic_max_marks[ind] = max_marks[ind]
dic_max_marks = dict(sorted(dic_max_marks.items(), key=lambda x: x[1]))

print(dic_marks, dic_max_marks) """
marks_zipped = list(sorted(marks_zipped))
print(marks_zipped)
remainder = 0
for ind in range(len(marks_zipped)):
    remainder += marks_zipped[ind][0]
remainder = sum_marks - remainder
print(remainder)
pointer = len(marks) // 2
print(marks_zipped[pointer])
while remainder != 0:
    if marks_zipped[pointer][0] < marks_zipped[pointer][1]:
        marks_zipped[pointer][0] += 1
        remainder -= 1
        if marks_zipped[pointer][0] > marks_zipped[pointer + 1][0]:
            temp = marks_zipped[pointer]
            marks_zipped[pointer] = marks_zipped[pointer + 1]
            marks_zipped[pointer + 1] = temp
    else:
        temp = marks_zipped[pointer]
        marks_zipped[pointer] = marks_zipped[pointer - 1]
        marks_zipped[pointer - 1] = temp
    
    