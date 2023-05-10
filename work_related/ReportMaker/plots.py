import matplotlib.pyplot as plt
import numpy as np
import random

FONT = {'family': 'Arial', 'color': 'black', 'size': 24}

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


def make_fake_data():
    synthesized_data = []
    synthesized_m = np.array([random.gauss(mu=2.3, sigma=0.6) for _ in range(1000)])
    # synthesized_m = [data for data in synthesized_m if data < 1]
    synthesized_data.append(synthesized_m)

    synthesized_f = np.array([random.gauss(mu=10, sigma=3) for _ in range(1000)])
    synthesized_data.append(synthesized_f)

    synthesized_t = np.array([random.gauss(mu=12.3, sigma=0.15) for _ in range(1000)])
    synthesized_data.append(synthesized_t)
    x_labels = ['Давление прессования, т/см3', 'Скорость прессования мм/с', 'Плотность продукта г/см3']
    # 1,8-2,8 7-12 12.2 12.5
    boundaries = [(1.8, 2.8), (7, 12), (12.2, 12.5)]
    file_names = ['Pressure', 'Speed', 'Dencity']

    drow_info = zip(synthesized_data, x_labels, file_names, boundaries)
    return drow_info



for data, label, file_name, bound in make_fake_data():
    density_plot(data,
                 file_name_to_save=file_name,
                 save=True,
                 reg_top=bound[0],
                 reg_bot=bound[1],
                 x_label=label,
                 y_label='Количество произведённых продуктов')
    