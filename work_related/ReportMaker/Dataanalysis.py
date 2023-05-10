# %%
import json
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import random
import seaborn as sns
# from sklearn import preprocessing

with open('Batches.js') as file:
    data_json = json.load(file)

    # старый файл
    # data = pd.DataFrame(data_json['Batches'])
    # print(data.head(5))

    # новые файлы
    data = pd.DataFrame(data_json)
# %%
data.columns  # колонки информации
# %%
data['TotalMass'].count()
# %%
# Построение удельного потребления энергии
data['EnergyConsumed'].hist()
# %%
x_dots_num = len(data['EnergyConsumed'].unique())
plt.plot([n for n in range(x_dots_num-2)],
         data['EnergyConsumed'][:-2])
plt.xlabel('Количество произведенного продукта')
plt.ylabel('Удельное потребление энергии')
#  графики позволят сразу увидеть, если удельное потребление нелинейно, то где то утечка. 
# %%
data.columns.values
# %%
#  Построение графика степени смешения
product_num = 0
# Исправить, не хранить шаг моделирования
time_max = data['DegreeMixingGraph'][product_num][-1][0]
mixing_degree = [data['DegreeMixingGraph'][product_num][ind][1] for ind in range(time_max)]  #  первый индекс продукт
plt.plot([n for n in range(time_max)], mixing_degree)
plt.xlabel('Время, с')
plt.ylabel('Степень смешения')
# тут нечего комментировать
# %%
# Исследование способа представления насыпной плотности
# data['Dencity'].hist()
expriment_points = 1000
ideal_num = 1000
synthesized_data = np.array([random.gauss(mu=5.6, sigma=0.2) for _ in range(expriment_points)])
# synthesized_data = pd.Series(synthesized_data)

ideal_data = np.array([random.gauss(mu=5.6, sigma=0.1) for _ in range(ideal_num)])
# ideal_data = pd.Series(ideal_data)
# %%
colors = ['#E69F00', '#56B4E9']
plt.hist([synthesized_data, ideal_data],
            bins=20,
            color=colors,
            label=['Типа реальные', 'Идеальное распределение'],
            density=True)

plt.legend()
plt.xlabel('Допустимая плотность')
plt.ylabel('Количество таблеток')
plt.title('Способ представления информации 1')
# %%
# далее гладкие распределения
# synthesized_data = preprocessing.normalize([synthesized_data])
# ideal_data = preprocessing.normalize([ideal_data])
data_for_density = pd.DataFrame({'Synth': synthesized_data.reshape(-1, ),
                                    'Ideal': ideal_data.reshape(-1, )})
sns.displot(data=data_for_density,
            kind='kde',
            color=colors,
            )
plt.xlabel('Допустимая плотность')
plt.ylabel('Количество таблеток')
# %%
#  Еще вариант представления
# synth_data_scaled = synthesized_data - synthesized_data.mean()
# plt.hist(synth_data_scaled, color='#E69F00')
# plt.vlines(x= [-0.2, 0.2], ymin=0, ymax=250, colors='black')

plt.hist(synthesized_data, color='#E69F00')
plt.vlines(x=[5.4, 5.8], ymin=0, ymax=270, colors='black')
plt.xlabel('Плотность')
plt.ylabel('Количество таблеток')

# %%
synth_data_scaled = synthesized_data - synthesized_data.mean()
plt.plot([n for n in range(len(synth_data_scaled))], synthesized_data)
plt.hlines(y=[5.4, 5.8], xmin=0, xmax=expriment_points,
           linestyles='dashed',
           linewidths=3,
           colors='black')
plt.xlabel('Плотность')
plt.ylabel('Количество таблеток')
# %%
sns.boxplot(ideal_data)
plt.plot(synthesized_data[10:30],
         [0 for _ in range(20)],
         color='red',
         marker='o',
         linestyle='',
         linewidth=2,
         markersize=12)
# %%
plt.plot([n for n in range(len(data['FillCoef']))], data['FillCoef'])
# идея в том, чтобы строить только то, что вышло за диапазоны

# %%
mix_degree = data['FinalDegreeMixing']
print(mix_degree)
plt.plot([n for n in range(len(mix_degree))],
         mix_degree,
         label='Степень смешения')
plt.hlines(0.25,
           mix_degree.min(),
           len(mix_degree),
           colors='red',
           label='Нижняя граница степени смешения')
plt.hlines(0.35,
           mix_degree.min(),
           len(mix_degree),
           colors='red',
           label='Верхняя граница степени смешения')
# и еще можно
bad_mix_degree = {ind: n for ind, n in enumerate(mix_degree) if n < 0.25 or n > 0.35}
plt.plot(bad_mix_degree.keys(), bad_mix_degree.values(), 'ro')
# %%
bar_width = 0.25
mix_degree = data['FinalDegreeMixing']
start_mix_degree = data['StartDegreeMixing']
points = [n for n in range(len(mix_degree))]
points2 = [n+bar_width for n in points]
fig = plt.subplots(figsize =(12, 8))
plt.bar(points, height=mix_degree, width=bar_width, label='StartDegreeMixing')
plt.bar(points2, height=mix_degree, width=bar_width, label='FinalDegreeMixing')
plt.xlabel('Product num', fontweight ='bold', fontsize = 15)
plt.ylabel('MixingDegree', fontweight ='bold', fontsize = 15)
# %%
# Отрисовка рисков


def make_groups(risk):
    risk_range = {bound: 0 for bound in range(0, 100, 10)}
    previous = 0
    for risk in risk_data:
        for key in risk_range.keys():
            if risk <= key and risk >= previous:
                risk_range[key] += 1
            previous = key
    risk_range_without_0 = risk_range.copy()
    for key, value in risk_range.items():
        if value == 0:
            risk_range_without_0.pop(key)
    return risk_range_without_0
                 

risk_data = data['RiskAssessment']
risk_range = make_groups(risk_data)
fig = plt.subplots(figsize =(12, 8))
plt.pie(x=risk_range.values(),
        labels=[f'Группа риска: {ris}' for ris in risk_range.keys()],
        labeldistance=0.25,
        rotatelabels=True,
        autopct='%1.1f%%',
        pctdistance=1.2,
        textprops={'fontsize': 12})
plt.rcParams['axes.facecolor'] = 'white'
plt.legend(title='Оценки проведения процесса усреднения', fontsize=12)
# %%
# Для циклограммы нужны моменты запуска усреднителя?
time_end = data['TimeEndFabrication']
time_work = data['TimeFabrication']
time_avg = data['TimesAverage']
time_end = pd.concat([pd.Series({0: 0}), time_end], ignore_index=True)
time_work = pd.concat([pd.Series({0: 0}), time_work], ignore_index=True)

plt.plot(time_end, 'g-o')
plt.xlabel('Номер продукта')
plt.ylabel('Время выпуска от начала')

# plt.plot(time_avg, )
# %%
# задержка между производством продукции
last = 0 
time_wait = []
for ind, value in time_end.items():
    time_wait.append(value - last)
    last = value
time_wait = pd.Series(time_wait)
plt.plot(time_wait, 'g-o', label='Простой')
plt.hlines(1000, 0, len(time_wait), colors='r', label='Предельный простой')
plt.xlabel('Номер продукта')
plt.ylabel('Время простоя')
plt.legend()
# %%
