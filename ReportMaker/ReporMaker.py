import json
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import random
import seaborn as sns
from pdf_maker import PDF

STATUSES_FILE = './jsons/statuses.js'
PLANT_NAMES = ['Manipulator',
               'Granulating',
               'Press',
               'Averaging',
               'Lab',
               'Probe',
               'AddStZn']
FILES_TO_PDF = ['statuses.png',
                'pie_quality.png',
                'pie_risk.png',
                'mass_plot.png']
FONT = {'family': 'Arial', 'color': 'black', 'size': 24}

def read_data(file_name):
    try:
        with open(file_name, 'r') as file:
            data_json = json.load(file)
    except FileNotFoundError:
        print('Файл не найден')
        return 0
    else:
        try:
            data = pd.DataFrame(data_json)
        except ValueError:
            print('Нельзя преобразовать в DataFrame, вернул json')
            return data_json
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


def make_statuses_plot(start: int, stop: int, y_plot, save=False, show=False):
    start_window = start
    window = stop
    fig = plt.figure(figsize =(12, 8))
    x = [t for t in range(start_window, window)]
    for ind in range(len(PLANT_NAMES)):
        # plt.plot([t for t in range(start_window, window)], y_plot[start_window:window][ind], label=PLANT_NAMES[ind])
        plt.plot(x,
                 [y[ind] for y in y_plot[start_window:window]],
                 label=PLANT_NAMES[ind])
    plt.ylim(-11, 10)
    plt.yticks([])
    plt.xticks(fontsize=FONT['size'])
    plt.legend(loc='upper right',
               prop={'family': 'Arial', 'size': 14})
    plt.xlabel('Время, с', fontdict=FONT)
    plt.ylabel('Статус оборудования', fontdict=FONT)
    plt.ticklabel_format(useOffset=False)
    plt.suptitle('График работы оборудования',
                 fontsize=24)
    plt.grid()
    if show:
        plt.show()
    if save:
        fig.savefig("./pngs/statuses.png", bbox_inches='tight')
    return fig
    

def exact_from_batches(in_file, res_name):
    total_res = []
    for product in in_file['Batches']:
        total_res.append(product[res_name])
    return total_res


def make_pie_risk(risk_data, save=False, show=False):
    risk_range = {bound: 0 for bound in range(0, 100, 10)}
    previous = 0
    for risk in risk_data:
        for key in risk_range.keys():
            if risk <= key and risk >= previous:
                risk_range[key] += 1
            previous = key
    risk_range = {key: value for key, value in risk_range.items() if value != 0}
    fig = plt.figure(figsize =(12, 8))
    plt.pie(x=risk_range.values(),
            labels=[f'Группа риска: {ris}-{ris+10}' for ris in risk_range.keys()],
            labeldistance=0.2,
            rotatelabels=True,
            autopct='%1.1f%%',
            pctdistance=1.2,
            textprops={'family': 'Arial', 'color': 'black', 'size': 14})
    plt.rcParams['axes.facecolor'] = 'white'
    plt.legend(title='Оценки проведения процесса усреднения',
               loc='lower left',
               prop={'family': 'Arial', 'size': 14})
    if show:
        plt.show()
    if save:
        fig.savefig("./pngs/pie_risk.png", bbox_inches='tight')
    return fig


def make_pie_quality(quality_share, save=False, show=False):
    label = ['Не брак', 'Брак']
    quality = [quality_share, 1-quality_share]
    fig = plt.figure(figsize =(12, 8))
    plt.pie(x=quality,
            labels=label,
            labeldistance=0.23,
            rotatelabels=True,
            autopct='%1.1f%%',
            pctdistance=1.2,
            textprops={'family': 'Arial', 'size': 14})
    plt.rcParams['axes.facecolor'] = 'white'
    plt.legend(title='Отношение бракованной продукции к нормальной',
               loc='lower left',
               prop={'family': 'Arial', 'size': 14})
    if show:
        plt.show()
    if save:
        fig.savefig("./pngs/pie_quality.png", bbox_inches='tight')
    return fig


def mass_plot(masses: list(), quality: list(), save=False, show=False):
    mass_plot_info = []
    cumulative = 0
    for mass in masses:
        mass_plot_info.append(mass+cumulative)
        cumulative += mass
    if quality != []:
        good_mass_plot_info = []
        cumulative = 0
        for ind, mass in enumerate(masses):
            if quality[ind] == True:
                good_mass_plot_info.append(mass+cumulative)
                cumulative += mass
            else:
                good_mass_plot_info.append(cumulative)

        fig = plt.figure(figsize =(12, 8))
        x = [n for n in range(len(mass_plot_info))]
        plt.bar(x=x,
            height=mass_plot_info,
            width=1,
            color='r',
            label='Весь продукт')
        plt.bar(x=x,
            height=good_mass_plot_info,
            width=1,
            color='g',
            label='Хороший продукт')
    plt.xlabel('Число произведенных продуктов',
               fontdict={'family': 'Arial', 'size': 14})
    plt.ylabel('Масса произведенных продуктов',
               fontdict={'family': 'Arial', 'size': 14})
    plt.legend()
    if show:
        plt.show()
    if save:
        fig.savefig("./pngs/mass_plot.png", bbox_inches='tight')
    return fig


def avg_process_plot(mixing_degree, mixing_params, file_name_to_save: str, save=False, show=False):
    fig = plt.figure(figsize=(12, 8))
    mixing_degree = [degree[1] for degree in mixing_degree] 
    plt.plot([n for n in range(len(mixing_degree))], mixing_degree)
    plt.xlabel('Время, с', fontdict=FONT)
    plt.ylabel('Степень смешения', fontdict=FONT)
    plt.suptitle(mixing_params,
                 fontsize=24)
    plt.yticks(fontsize=FONT['size'])
    plt.xticks(fontsize=FONT['size'])
    plt.grid()
    if show:
        plt.show()
    if save:
        file_name_to_save = "./pngs/" + file_name_to_save + '.png'
        fig.savefig(file_name_to_save, bbox_inches='tight')
    return fig


def pdf_saver(file_name, list_of_filenames_to_save):
    pdf = PDF(file_name)
    # pdf.set_title('Заголовок')
    pdf.print_chapter(1,
                      'Графики по статусам',
                      'exp_info.txt',
                      list_of_filenames_to_save)
    try:
        file_name = './pdfs/' + file_name + '.pdf'
        pdf.output(file_name, 'F')
    except FileNotFoundError:
        print("ошибка с записью. Проверьте наличие шрифтов")
    

statuses = read_data(STATUSES_FILE)
y_plot = make_y_plots_statuses(statuses)
figures_storage = []
statuses_plot_to_print = make_statuses_plot(0, 3600, y_plot, save=True)
figures_storage.append(make_statuses_plot(1000, 1400, y_plot))

products = read_data('./jsons/Batches2.js')

make_pie_quality(products['Consunption']['QualityCoef'], save=True)

risks = exact_from_batches(products, 'RiskAssessment')
make_pie_risk(risks, save=True)

total_mass = exact_from_batches(products, 'TotalMass')
quality = exact_from_batches(products, 'IsGood')
mass_plot(total_mass, quality, save=True)

avg_name = "avg_plot_"
avg_names = []
mixing_params = ""
for ind, product in enumerate(products['Batches']):
    avg_name += str(ind)
    mixing_params += f"Частота: {product['Frequency'][0]} "
    mixing_params += f"Коэффициент заполнения: {product['FillCoef']:.2f} "
    mixing_params += f"Начальная степень смешения {product['StartDegreeMixing']}"
    avg_process_plot(product['DegreeMixingGraph'], mixing_params, avg_name, save=True)
    avg_names.append(avg_name + '.png')
    avg_name = "avg_plot_"
    mixing_params = ""



pdf_saver('Отчёт по усреднителю', FILES_TO_PDF+avg_names)

