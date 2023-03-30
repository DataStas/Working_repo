# %%
import json
import pandas as pd
import matplotlib.pyplot as plt

with open('Batches.js') as file:
    data_json = json.load(file)
    # for info in data_json['Batches']:
    #     for 
    #     print(info['TotalMass'])
    # print(data_json['Batches'])
    data = pd.DataFrame(data_json['Batches'])
    print(data.head(5))
    # %% 
    data['EnergyConsumed'].describe()
    # %%
    x_dots_num = len(data['EnergyConsumed'].unique())
    plt.plot([n for n in range(x_dots_num)], data['EnergyConsumed'])
    plt.xlabel('Количество произведенного продукта')
    plt.ylabel('Удельное потребление энергии')
    # %%
    data['TotalMass']
    data['TotalMass'].hist()
    # %%
    time_max = data['DegreeMixingGraph'][0][-1][0] # Исправить, не хранить шаг моделирования
    mixing_degree = [degree for degree in unpack(data['DegreeMixingGraph'][0][:][:])]
    # %%
    mixing_degree
    # %%
    time_moment, mixing_degree = data['DegreeMixingGraph']
    

# %%
