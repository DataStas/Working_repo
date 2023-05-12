import json
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import random
import seaborn as sns
from pdf_maker import PDF

STATUSES_FILE = './jsons/Statuses_init_good.js'
BATCHES_FILE = './jsons/GranulatorPlant_containersProduction11_05_23.json'
REPORT_NAME = 'Отчёт по гранулятору'
FILES_TO_PDF = ['statuses.png',
                'pie_quality.png',
                'pie_risk.png',
                'mass_plot.png',
                'Frequency.png',
                'time.png',
                'm.png']
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
        state[0] -= 14
        state[1] += 6
        state[2] += 10
        state[3] += 2
        state[4] -= 2
        state[5] -= 6
        state[6] -= 10
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
    plt.ylim(-15, 14)
    plt.yticks([])
    plt.xticks(fontsize=FONT['size'])
    plt.legend(loc='lower center',
               prop={'family': 'Arial', 'size': 16},
               bbox_to_anchor=(0.5, -0.5),
               borderaxespad=0)
    plt.xlabel('Время, с', fontdict=FONT)
    plt.ylabel('Статус работы оборудования', fontdict=FONT)
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
    plt.suptitle('Диаграмма оценки рисков',
                 fontsize=24)
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
    plt.legend(title='Отношение бракованной продукции к допустимой',
               loc='lower left',
               prop={'family': 'Arial', 'size': 14})
    plt.suptitle('Диаграмма качества',
                 fontsize=24)
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
    p = plt.bar(x=x,
            height=mass_plot_info,
            width=1,
            color='#FF7F50',
            label='Весь продукт')
    plt.bar(x=x,
            height=good_mass_plot_info,
            width=1,
            color='#9ACD32',
            label='Хороший продукт')
    plt.hlines(y=mass_plot_info[-1],
               xmin=0,
               xmax=len(mass_plot_info),
               colors='red',
               linestyles='dashed',
               label=f'Количество произведенного продукта {mass_plot_info[-1]:.2f}',
               linewidths=3)
    plt.hlines(y=good_mass_plot_info[-1],
               xmin=0,
               xmax=len(mass_plot_info),
               colors='green',
               linestyles='dashed',
               label=f'Масса произведенного хорошего продукта {good_mass_plot_info[-1]:.2f}',
               linewidths=3)
    plt.xlabel('Количество произведенных продуктов',
               fontdict=FONT)
    plt.ylabel('Масса произведенных продуктов',
               fontdict=FONT)
    plt.legend(prop={'family': 'Arial', 'size': 16}) # , bbox_to_anchor=(0, -0.01)
    plt.suptitle('График прироста масс продуктов',
                 fontsize=24)
    if show:
        plt.show()
    if save:
        fig.savefig("./pngs/mass_plot.png", bbox_inches='tight')
    return fig


def avg_process_plot(mixing_degree, mixing_params, file_name_to_save: str, save=False, show=False):
    fig = plt.figure(figsize=(12, 8))
    mixing_degree = [degree[1] for degree in mixing_degree] 
    plt.plot([n for n in range(len(mixing_degree))],
             mixing_degree,
             label=mixing_params)
    plt.xlabel('Время, с', fontdict=FONT)
    plt.ylabel('Степень смешения', fontdict=FONT)
    plt.suptitle('График описывающий работу установки усреднения',
                 fontsize=24)
    plt.yticks(fontsize=FONT['size'])
    plt.xticks(fontsize=FONT['size'])
    plt.grid()
    plt.legend(prop={'family': 'Arial', 'size': 18})
    if show:
        plt.show()
    if save:
        file_name_to_save = "./pngs/" + file_name_to_save + '.png'
        fig.savefig(file_name_to_save, bbox_inches='tight')
    return fig


def density_plot(data_to_plot, file_name_to_save='dencity_plot', save=False, show=False, **options):
    """_summary_

    Kwargs:
        **options: набор параметров необходимых для корректной отрисовки:
        reg_top - верхняя рекомендуемая граница
        reg_bot - нижняя рекомендуемая граница
        x_label - наименование оси X
        y_label - наименование оси Y"
    Returns:
        _type_: _description_
    """
    fig = plt.figure(figsize=(12, 8))
    try:
        p = plt.hist(data_to_plot,
                     color='#E69F00',
                     label=options['x_label'])
    except KeyError:
        print('Вы забыли указать наименование оси X')
        return 0
    try:
        plt.vlines(x=[options['reg_top'], options['reg_bot']],
                   ymin=0,
                   ymax=p[0].max(),
                   colors='black',
                   linewidths=5,
                   label='Регламентные границы')
    except KeyError:
        print("Вы забыли указать reg_top или reg_bot")
        return 0
    plt.legend(prop={'family': 'Arial', 'size': 16})
    plt.xlabel(options['x_label'], fontdict=FONT)
    try:
        plt.ylabel(options['y_label'], fontdict=FONT)
    except KeyError:
        print("Вы забыли указать наименование оси Y")
    plt.suptitle('График для анализа отклонений от регламента',
                 fontsize=24)
    if show:
        plt.show()
    if save:
        file_name_to_save = "./pngs/" + file_name_to_save + '.png'
        fig.savefig(file_name_to_save, bbox_inches='tight')
    return fig


def pdf_saver(file_name, list_of_filenames_to_save):
    pdf = PDF('Отчёт о результатах экспериментального исследования участка усреднения')
    # pdf.set_title('')
    pdf.print_chapter(1,
                      'Графики по статусам',
                      'exp_info.txt',
                      list_of_filenames_to_save)
    try:
        file_name = './pdfs/' + file_name + '.pdf'
        pdf.output(file_name, 'F')
        print("Отчёт создан")
    except FileNotFoundError:
        print("ошибка с записью. Проверьте наличие шрифтов")


def gran_plot(data_to_plot, file_name_to_save='dencity_plot', save=False, show=False, **options):
    """_summary_

    Kwargs:
        **options: набор параметров необходимых для корректной отрисовки:
        reg_top - верхняя рекомендуемая граница
        reg_bot - нижняя рекомендуемая граница
        x_label - наименование оси X
        y_label - наименование оси Y"
    Returns:
        _type_: _description_
    """
    y_label_data = []
    for data in data_to_plot:
        for y in data.values():
            y_label_data.append(y)
    # x_label_data = [n for n in range(len(data_to_plot))]
    x_label_data = []
    for data in data_to_plot:
        for x in data.keys():
            x_label_data.append(x[11:])

    fig = plt.figure(figsize=(12, 8))
    try:
        p = plt.plot(x_label_data,
                     y_label_data,
                     color='#E69F00',
                     label=options['x_label'])
    except KeyError:
        print('Вы забыли указать наименование оси X')
        return 0
    plt.legend(prop={'family': 'Arial', 'size': 16})
    plt.xlabel(options['x_label'], fontdict=FONT)
    try:
        plt.ylabel(options['y_label'], fontdict=FONT)
    except KeyError:
        print("Вы забыли указать наименование оси Y")
    plt.suptitle('График для анализа гранулометрического состава',
                 fontsize=24)
    plt.xticks
    if show:
        plt.show()
    if save:
        file_name_to_save = "./pngs/" + file_name_to_save + '.png'
        fig.savefig(file_name_to_save, bbox_inches='tight')
    return fig


def reg_plot(data_to_plot, file_name_to_save='dencity_plot', save=False, show=False, **options):
    """_summary_

    Kwargs:
        **options: набор параметров необходимых для корректной отрисовки:
        reg_top - верхняя рекомендуемая граница
        reg_bot - нижняя рекомендуемая граница
        x_label - наименование оси X
        y_label - наименование оси Y"
    Returns:
        _type_: _description_
    """
    fig = plt.figure(figsize=(12, 8))
    x_plot = [n for n in range(len(data_to_plot))]
    try:
        p = plt.plot(x_plot,
                     data_to_plot,
                     color='#E69F00',
                     label=options['x_label'])
    except KeyError:
        print('Вы забыли указать наименование оси X')
        return 0
    try:
        plt.hlines(y=[options['reg_top'], options['reg_bot']],
                   xmin=0,
                   xmax=x_plot[-1],
                   colors='black',
                   linewidths=5,
                   label='Регламентные границы')
    except KeyError:
        print("Вы забыли указать reg_top или reg_bot")
    plt.legend(prop={'family': 'Arial', 'size': 16})
    plt.xlabel(options['x_label'], fontdict=FONT)
    try:
        plt.ylabel(options['y_label'], fontdict=FONT)
    except KeyError:
        print("Вы забыли указать наименование оси Y")
    plt.suptitle('График для анализа отклонений от регламента',
                 fontsize=24)
    if show:
        plt.show()
    if save:
        file_name_to_save = "./pngs/" + file_name_to_save + '.png'
        fig.savefig(file_name_to_save, bbox_inches='tight')
    return fig


def make_fake_data():
    synthesized_data = []
    synthesized_m = np.array([random.gauss(mu=0.95, sigma=0.05) for _ in range(1000)])
    synthesized_m = [data for data in synthesized_m if data < 1]
    synthesized_data.append(synthesized_m)

    synthesized_f = np.array([random.gauss(mu=50, sigma=10) for _ in range(1000)])
    synthesized_data.append(synthesized_f)

    synthesized_t = np.array([random.gauss(mu=500, sigma=100) for _ in range(1000)])
    synthesized_data.append(synthesized_t)
    x_labels = ['Степень смешения', 'Частота смешения', 'Время смешения']
    boundaries = [(0.9, 0.9), (60, 45), (540, 460)]
    file_names = ['m', 'Frequency', 'time']

    drow_info = zip(synthesized_data, x_labels, file_names, boundaries)
    return drow_info



products = read_data(BATCHES_FILE)
# print(products)

# make_pie_quality(products['Consumption']['QualityCoef'], save=False, show=True)
# print(products['batches'][])
# density_plot(products['batches'][0]['BulkDensity'],
#              x_label='Насыпная плотность',
#              y_label='Число слоев в контейнере',
#              show=True)
# gran_plot(products['batches'][0]['DistributionGranVector'],
#              x_label='Группа частиц по размеру',
#              y_label='Доля частиц',
#              show=True)
reg_plot(products['batches'][0]['ScrewFrequencyVector'],
             x_label='Номер слоя',
             y_label='Значение ScrewFrequency',
             reg_top=1550,
             reg_bot=1150,
             show=True)
