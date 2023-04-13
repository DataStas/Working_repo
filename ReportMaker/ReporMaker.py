import json
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import random
import seaborn as sns
from pdf_maker import PDF

STATUSES_FILE = 'statuses.js'
PLANT_NAMES = ['Manipulator',
               'Granulating',
               'Press',
               'Averaging',
               'Lab',
               'Probe',
               'AddStZn']


def read_data(file_name):
    try:
        with open(file_name, 'r') as file:
            data_json = json.load(file)
            data = pd.DataFrame(data_json)
    except FileNotFoundError:
        print('Произошла ошибка чтения файла')
        return 0
    else:
        return data


def make_df_of_statuses(statuses):
    row = 0
    states = []
    for current_condition in statuses['data']:
        statuses_line = []
        for plant in current_condition[:-3]:
            statuses_line.append(plant['state'])
        state = {plant_name: status for plant_name, status in zip(PLANT_NAMES, statuses_line)}
        states.append(state)
        row += 1
    status_state = pd.DataFrame(states)
    # артефакт, но жалко удалять(
    # y_plot = []
    # # manip_y = status_state[PLANT_NAMES[0]] - 3
    # # gran_y = status_state[PLANT_NAMES[1]] + 2
    # # press_y = status_state[PLANT_NAMES[2]] + 3
    # # avg_y = status_state[PLANT_NAMES[3]] + 1
    # # lab_y = status_state[PLANT_NAMES[4]] 
    # # probe_y = status_state[PLANT_NAMES[5]] - 1
    # # add_st_y = status_state[PLANT_NAMES[6]] - 2 

    # y_plot.append(status_state[PLANT_NAMES[0]] - 10)
    # y_plot.append(status_state[PLANT_NAMES[1]] + 5)
    # y_plot.append(status_state[PLANT_NAMES[2]] + 8)
    # y_plot.append(status_state[PLANT_NAMES[3]] + 2)
    # y_plot.append(status_state[PLANT_NAMES[4]] - 1)
    # y_plot.append(status_state[PLANT_NAMES[5]] - 4)
    # y_plot.append(status_state[PLANT_NAMES[6]] - 7)

    return status_state


def make_y_plots_statuses(in_file):
    states = []
    for current_condition in in_file['data']:
        statuses_line = []
        for plant in current_condition[:-3]:
            statuses_line.append(plant['state'])
        states.append(statuses_line)
    # введение смещений для посмтроения графика
    # [n for n in range(-10,10,3)]
    for state in states:
        state[0] -= 10
        state[1] += 5
        state[2] += 8
        state[3] += 2
        state[4] -= 1
        state[5] -= 4
        state[6] -= 7
    return states


def make_statuses_plot(start: int, stop: int, y_plot):
    start_window = start
    window = stop
    font1 = {'family': 'serif',
             'color': 'black',
             'size': 20}
    fig = plt.figure(figsize =(12, 8))
    x = [t for t in range(start_window, window)]
    for ind in range(len(PLANT_NAMES)):
        # plt.plot([t for t in range(start_window, window)], y_plot[start_window:window][ind], label=PLANT_NAMES[ind])
        plt.plot(x,
                 [y[ind] for y in y_plot[start_window:window]],
                 label=PLANT_NAMES[ind])
    plt.ylim(-11, 10)
    plt.yticks([8, 5, 2, 0, -4, -7, -10])
    plt.legend(loc='upper right')
    plt.xlabel('Время, с', fontdict=font1)
    plt.ylabel('Статус оборудования', fontdict=font1)
    plt.ticklabel_format(useOffset=False)
    plt.grid()
    # plt.show()
    # fig.savefig("statuses.png", bbox_inches='tight')
    return fig
    


def pdf_saver(file_name, *args):
    pdf = PDF(file_name)
    # pdf.set_title('Заголовок')
    pdf.print_chapter(1, 'Графики по статусам', 'exp_info.txt', 'statuses.png')
    pdf.output('avg_repot_1.pdf', 'F')
    
    

statuses = read_data(STATUSES_FILE)
y_plot = make_y_plots_statuses(statuses)
figures_storage = []
# statuses_plot_to_print = make_statuses_plot(1000, 1400, y_plot)
figures_storage.append(make_statuses_plot(1000, 1400, y_plot))
pdf_saver('Отчёт по усреднителю', *figures_storage)




