from tkinter import *
import json
import pandas as pd

SETTING_FOR_OPERATIONS = ["condition",
                           "TimeInWork",
                           "CodePrior",
                           "IDcont",
                           "PPR",
                           "MotorTime",
                           "FreshMotorTime",
                            "RunTime"]

SETTING_FOR_MANIPULATOR = ['condition',
                           'TimeEnd',
                           'IDdestination',
                           'IDcont',
                           'PPR',
                           'MotorTime',
                           'FreshMotorTime']

CONDITIONS = ['Статусы состояния оборудования :',
              '0 - готов к выполнению операции',
              '1 - выполнение операции',
              '2 - ожидание манипулятора',
              '3 - ППР']


LABEL_NAMES = ['Время начала моделирования',
               'Время окончания моделирования',
               'Сколько контейнеров на участке?',
               'Содержание контейнера: content, ID',
               'Состояние ячеек склада: IDcont, IDcell',
               'Настройки манипулятора:',
               'Настройки операций участка:',
               'Имя файда для настройки усреднителя']

CONTENTS = ['0 - нет контейнера',
            '1 - пустой',
            '2 - с гранулятом',
            '3 - с усреднëнным гранулятом',
            '4 - с качественным гранулятом',
            '5 - с бракованным гранулятом',
            "6 - со стеаратом цинка",
            '7 - с усредненным пресс - порошком',
            "8 - с качественным пресс - порошком",
            '9 - с бракованным пресс - порошком'
            ]


def xlsx_read(file_name, sheet_name):
    try:
        data = pd.read_excel(file_name, sheet_name=sheet_name)
    except FileNotFoundError:
        print("Файл xlsx не прочитан. Проверьте его наличие, наименование")
    except ValueError:
        print('Неверное название страницы у xlsx файла (только английский)')
        return [], []
    layers_info = {
        "layers": [
        ]
    }
    row = 2
    while data.iloc[row, 0] != 0:
        layers_info['layers'].append({"m_Pu": 0,
                                      "Mass": 0,
                                      "dencity": 0,
                                      "V": 0,
                                      "C_Pu": 00
                                      })
        layers_info["layers"][row-2]["m_Pu"] = round(data.iloc[row, 1], 3)
        layers_info["layers"][row-2]["Mass"] = round(data.iloc[row, 2], 3)
        layers_info["layers"][row-2]["dencity"] = round(data.iloc[row, 3], 3)
        layers_info["layers"][row-2]["V"] = round(data.iloc[row, 4], 3)
        layers_info["layers"][row-2]["C_Pu"] = round(data.iloc[row, 5], 3)
        row += 1

    model_params = {
        'volume': data.columns[2],
        'frequency': data.columns[4],
        'constuct_k': data.columns[6],
        'n_opt': data.iloc[0, 9],
        'n_crit': data.iloc[0, 11],
        'time': data.iloc[data.shape[0]-1, 8],
    }

    return layers_info, model_params


# Button
def generate():
    # Load the JSON data from the file
    try:
        with open('empty.json', 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        print("Поместите файл empty.json в директорию с проектом")

    fields_list = [
        "TimeStart",
        "TimeEnd",
        "CountContainers",
        "Containers",
        "Cells",
        "Manipulator",
        "Operations"
    ]
    # Update the values in the JSON data
    data[fields_list[0]] = int(entry1.get())
    data[fields_list[1]] = int(entry2.get())
    data[fields_list[2]] = int(entry3.get())

    # Update the Containers array
    containers = int(entry3.get())
    containers_info = list(text.get("1.0", END).split())
    xlsx_file_name = entry5.get().split()[0]
    sheet_name = entry5.get().split()[1]
    layers_info, model_params = xlsx_read(xlsx_file_name, sheet_name)
    if len(containers_info)/2 != containers:
        print("Ввод параметров контейнеров был осуществлен неверно")
    else:
        ind = 0
        while ind < containers*2-1:
            try:
                data[fields_list[3]].append({'content': int(containers_info[ind]),
                                            'ID': int(containers_info[ind+1]),
                                            'Volume': model_params['volume'] if int(containers_info[ind]) != 0 else 0,
                                            'Layers': layers_info["layers"] if int(containers_info[ind]) >= 2 else []})
                ind += 2
            except TypeError:
                print('При вводе произошла ошибка, файл не создан')
                return 0
    
    # Update the Cells array
    cells_info = list(text2.get("1.0", END).split())
    cell_num = 0
    for ind in range(0, 6, 2):
        data[fields_list[4]][cell_num]['IDCont'] = int(cells_info[ind])
        data[fields_list[4]][cell_num]['IDCont'] = int(cells_info[ind+1])
        cell_num += 1

    # Update the Manipulator object
    manip_info = list(text3.get("1.0", END).split())
    if len(manip_info) == 7:
        data[fields_list[5]]['condition'] = int(manip_info[0])
        data[fields_list[5]]['TimeEnd'] = int(manip_info[1])
        data[fields_list[5]]['IDdestination'] = int(manip_info[2])
        data[fields_list[5]]['IDcont'] = int(manip_info[3])
        data[fields_list[5]]['PPR'] = int(manip_info[4])
        data[fields_list[5]]['MotorTime'] = int(manip_info[5])
        data[fields_list[5]]['FreshMotorTime'] = int(manip_info[6])
    else:
        print("Параметры манипулятора были введены неверно")

    # Update the Operations array
    operation_names = ['Granulator',
                       'Press',
                       'Averator',
                       'Laba',
                       'Probe',
                       'AddStZn']
    operation_parameters = list(text4.get("1.0", END).split())
    num_params = 8
    sliced_parms = []
    for ind in range(len(operation_names)):
        sliced_parms.append(operation_parameters[ind*num_params:(ind+1)*num_params])
    for ind in range(len(operation_names)):
        data['Operations'].append({'Name': operation_names[ind],
                                   'condition': int(sliced_parms[ind][0]),
                                    'TimeInWork': int(sliced_parms[ind][1]),
                                    'CodePrior': int(sliced_parms[ind][2]),
                                    'IDCont': int(sliced_parms[ind][3]),
                                    'PPR': int(sliced_parms[ind][4]),
                                    'MotorTime': int(sliced_parms[ind][5]),
                                    'FreshMotorTime': int(sliced_parms[ind][6]),
                                    'RunTime': int(sliced_parms[ind][7])})
    file_name = entry4.get() + '.json'
    with open(file_name, 'w') as f:
        json.dump(data, f, indent=2)
    
    avg_params = {
        "WorkParameters": [
            {"WorkTime": model_params['time'],
             "Frequncy": model_params['frequency']}],
        'ConstructionCoef': model_params['constuct_k'],
        'n_opt': model_params['n_opt'],
        'n_crit': model_params['n_crit']
    }
    
    file2_name = "AvgParams_" + entry4.get() + '.json'
    with open(file2_name, 'w') as f:
        print('Файлы успешно созданы')
        json.dump(avg_params, f, indent=2)


def listbox_used():
    pass


try:
    with open('pre_set.json', 'r') as f:
        pre_settrings_data = json.load(f)
except FileNotFoundError:
    print("Поместите в директорию файл pre_set.json")

window = Tk()
window.title("Генератор входных файлов для усреднителя")
window.minsize(width=500, height=500)

column = 0 
row = 0

# Основные подписи
label = Label(text=LABEL_NAMES[0])
label.config(text=LABEL_NAMES[0])
label.grid(column=0, row=row)
row += 1

label = Label(text=LABEL_NAMES[1])
label.config(text=LABEL_NAMES[1])
label.grid(column=0, row=row)
row += 1

label = Label(text=LABEL_NAMES[2])
label.config(text=LABEL_NAMES[2])
label.grid(column=0, row=row)
row += 1

label = Label(text=LABEL_NAMES[3])
label.config(text=LABEL_NAMES[3])
label.grid(column=0, row=row)
row += 1


label = Label(text=LABEL_NAMES[4])
label.config(text=LABEL_NAMES[4])
label.grid(column=0, row=row)
row += 1

label = Label(text=LABEL_NAMES[5])
label.config(text=LABEL_NAMES[5])
label.grid(column=0, row=row)
row += 1

label = Label(text=LABEL_NAMES[6])
label.config(text=LABEL_NAMES[6])
label.grid(column=0, row=row)
row += 1

# label = Label(text=LABEL_NAMES[7])
# label.config(text=LABEL_NAMES[7])
# label.grid(column=0, row=row)
# row += 1

label = Label(text="")
label.config(text="Введите имя выходного файла в первую строчку" +
             "\n" +
             "Введите имя страницы xlsx файла во вторую строчку")
label.grid(column=0, row=row)

entry4 = Entry(width=30)
# Add some text to begin with
entry4.insert(END, string="init_1")
# Gets text in entry
entry4.grid(column=1, row=row)
row += 1


column = 1 
row = 0

# Поля ввода
entry1 = Entry(width=30)
# Add some text to begin with
entry1.insert(END, string="0")
# Gets text in entry
entry1.grid(column=1, row=row)
row += 1

entry2 = Entry(width=30)
# Add some text to begin with
entry2.insert(END, string='86400')
# Gets text in entry
entry2.grid(column=1, row=row)
row += 1

entry3 = Entry(width=30)
# Add some text to begin with
entry3.insert(END, string=3)
# Gets text in entry
entry3.grid(column=1, row=row)
row += 1

# Параметры контейнеров
listbox = Listbox(height=4)


for item in CONTENTS:
    listbox.insert(CONTENTS.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.grid(column=4, row=row)

containers = len(pre_settrings_data['Containers'])
pre_setting_containers = ''
for ind in range(containers):
    pre_setting_containers += str(pre_settrings_data['Containers'][ind]['content']) + " "
    pre_setting_containers += str(pre_settrings_data['Containers'][ind]['ID']) + " "

label = Label(text="Пример ввода:")
label.config(text="Пример ввода:" + '\n' + pre_setting_containers)
label.grid(column=1, row=row)

text = Text(height=5, width=30)
text.focus()
text.insert(END, pre_setting_containers)
text.grid(column=2, row=row)

row += 1

# Параметры ячеек
cells = len(pre_settrings_data['Cells'])
pre_setting_cells = ''
for ind in range(containers):
    pre_setting_cells += str(pre_settrings_data['Cells'][ind]['IDCont']) + " "
    pre_setting_cells += str(pre_settrings_data['Cells'][ind]['ID']) + " "

label = Label(text="Пример ввода:" + '\n' + pre_setting_cells)
label.config(text="Пример ввода:" + '\n' + pre_setting_cells)
label.grid(column=1, row=row)

text2 = Text(height=5, width=30)
text2.focus()
text2.insert(END, pre_setting_cells)
text2.grid(column=2, row=row)

listbox6 = Listbox(height=5)
for item in CONDITIONS:
    listbox6.insert(CONDITIONS.index(item), item)
listbox6.bind("<<ListboxSelect>>", listbox_used)
listbox6.grid(column=4, row=row)

row += 1

# Параметры манипулятора
pre_setting_manip = ''
pre_setting_manip += str(pre_settrings_data['Manipulator'][SETTING_FOR_MANIPULATOR[0]]) + " "
pre_setting_manip += str(pre_settrings_data['Manipulator'][SETTING_FOR_MANIPULATOR[1]]) + " "
pre_setting_manip += str(pre_settrings_data['Manipulator'][SETTING_FOR_MANIPULATOR[2]]) + " "
pre_setting_manip += str(pre_settrings_data['Manipulator'][SETTING_FOR_MANIPULATOR[3]]) + " "
pre_setting_manip += str(pre_settrings_data['Manipulator'][SETTING_FOR_MANIPULATOR[4]]) + " "
pre_setting_manip += str(pre_settrings_data['Manipulator'][SETTING_FOR_MANIPULATOR[5]]) + " "
pre_setting_manip += str(pre_settrings_data['Manipulator'][SETTING_FOR_MANIPULATOR[6]]) + " "

label = Label(text="Пример ввода:" + '\n' + pre_setting_manip)
label.config(text="Пример ввода:" + '\n' + pre_setting_manip)
label.grid(column=1, row=row)

listbox2 = Listbox(height=5)
for item in SETTING_FOR_MANIPULATOR:
    listbox2.insert(SETTING_FOR_MANIPULATOR.index(item), item)
listbox2.bind("<<ListboxSelect>>", listbox_used)
listbox2.grid(column=4, row=row)

text3 = Text(height=5, width=30)
text3.focus()
text3.insert(END, pre_setting_manip)
text3.grid(column=2, row=row)

row += 1

pre_setting_oper = ''
num_operations = len(pre_settrings_data['Operations'])
for ind in range(num_operations):
    pre_setting_oper += str(pre_settrings_data['Operations'][ind][SETTING_FOR_OPERATIONS[0]]) + " "
    pre_setting_oper += str(pre_settrings_data['Operations'][ind][SETTING_FOR_OPERATIONS[1]]) + " "
    pre_setting_oper += str(pre_settrings_data['Operations'][ind][SETTING_FOR_OPERATIONS[2]]) + " "
    pre_setting_oper += str(pre_settrings_data['Operations'][ind][SETTING_FOR_OPERATIONS[3]]) + " "
    pre_setting_oper += str(pre_settrings_data['Operations'][ind][SETTING_FOR_OPERATIONS[4]]) + " "
    pre_setting_oper += str(pre_settrings_data['Operations'][ind][SETTING_FOR_OPERATIONS[5]]) + " "
    pre_setting_oper += str(pre_settrings_data['Operations'][ind][SETTING_FOR_OPERATIONS[6]]) + " "
    pre_setting_oper += str(pre_settrings_data['Operations'][ind][SETTING_FOR_OPERATIONS[7]]) + "\n"

label = Label(text="Пример ввода:" + '\n' + pre_setting_oper)
label.config(text="Пример ввода:" + '\n' + pre_setting_oper)
label.grid(column=1, row=row)

listbox3 = Listbox(height=5)
for item in SETTING_FOR_OPERATIONS:
    listbox3.insert(SETTING_FOR_OPERATIONS.index(item), item)
listbox3.bind("<<ListboxSelect>>", listbox_used)
listbox3.grid(column=4, row=row)

text4 = Text(height=5, width=30)
text4.focus()
text4.insert(END, pre_setting_oper)
text4.grid(column=2, row=row)
row += 1

entry5 = Entry(width=30)
# Add some text to begin with
entry5.insert(END, string="super.xlsx OK")
entry5.grid(column=2, row=row)


# calls action() when pressed
button = Button(text="Сгенерировать", command=generate)
button.grid(column=1, row=15)

window.mainloop()