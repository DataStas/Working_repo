def sorting(marks, max_marks):
    marks_zipped = list(zip(marks, max_marks))
    marks_zipped = list(sorted(marks_zipped))

    marks = []
    max_marks = []

    for mark, max_mark in marks_zipped:
        marks += [mark]
        max_marks += [max_mark]
    return marks, max_marks


""" n_students = 7
sum_marks = 42
marks = [5, 3, 7, 6, 3, 10, 1]
max_marks = [5, 5, 9, 7, 8, 10, 1] """
""" n_students = 3
sum_marks = 27
marks = [11, 2, 11]
max_marks = [14, 10, 14] """
input_list = [int(i) for i in input().split()]
number_input = ''
all_marks = []
count = 0
while True:
  number_input = str(input())
  count = count + 1# ввод строк
  all_marks.append([int(s) for s in number_input.split()])
  if count == input_list[0]:
     break
n_students = input_list[0]
sum_marks = input_list[1]
marks = []
max_marks = []
for i in range(len(all_marks)):
    marks.append(all_marks[i][0])
    max_marks.append(all_marks[i][1])
# preset
remainder = 0
for mark in marks:
    remainder += mark
remainder = sum_marks - remainder
p = len(marks) // 2  # pointer on center

marks, max_marks = sorting(marks, max_marks)

while remainder != 0:
    # print(marks, max_marks, remainder)
    if marks[p] < max_marks[p]:
        marks[p] += 1
        remainder -= 1
        if marks[p] > marks[p+1]:
            temp = marks[p]
            marks[p] = marks[p+1]
            marks[p+1] = temp

            temp = max_marks[p]
            max_marks[p] = max_marks[p+1]
            max_marks[p+1] = temp
    else:
        ind = 1
  
        if max_marks[p-ind] == marks[p-ind]:
            while max_marks[p-ind] <= marks[p-ind]:
                ind += 1
                # print(max_marks[p-ind], marks[p-ind])
        temp = marks[p]
        marks[p] = marks[p-ind]
        marks[p-ind] = temp
          
        temp = max_marks[p]
        max_marks[p] = max_marks[p-ind]
        max_marks[p-ind] = temp

marks, max_marks = sorting(marks, max_marks)
print(marks[p])