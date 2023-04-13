import pandas as pd
LAYER_PARAMS = ["m_Pu", "Mass", "dencity", "V", "C_Pu"]


def xlsx_read(file_name):
    data = pd.read_excel(file_name, sheet_name='OK')
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
        layers_info["layers"][row-2]["m_Pu"] = round(data.iloc[row, 0], 3)
        layers_info["layers"][row-2]["Mass"] = round(data.iloc[row, 1], 3)
        layers_info["layers"][row-2]["dencity"] = round(data.iloc[row, 2], 3)
        layers_info["layers"][row-2]["V"] = round(data.iloc[row, 3], 3)
        layers_info["layers"][row-2]["C_Pu"] = round(data.iloc[row, 4], 3)
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


layers_info, model_params = xlsx_read('super.xlsx')
print(model_params, layers_info["layers"][0])