# %%
import pandas as pd
import matplotlib as plt
import numpy as np
from sklearn.model_selection import train_test_split
# %%
train = pd.read_csv('./data/train_v2.csv', index_col='id')
test = pd.read_csv('./data/test_v2.csv', index_col='id')
# %%
pd.set_option('display.float_format', '{:.2f}'.format)
print(train.columns)
train.head(4)
# %%
train.shape
# %%
train.info()
# %%
test.info()
# %%
# train.isnull().sum().sort_values(ascending=False).to_frame()

# %%

def find_nulls(df):
    isnull = df.isnull().sum().sort_values(ascending=False).to_frame()
    isnull.columns = ['How_many']
    isnull['Percentage'] = np.around(((isnull / len(df) * 100)[(isnull / len(df) * 100) != 0]), decimals=2)
    print(f"В информации {len(isnull[isnull.How_many>0])} признаков с просуском ")
    return isnull

# %%
# так, ну пропусков в целом не так много 20%
find_nulls(train).head(10)
find_nulls(test).head(10)
# %%
# Заметка. А если похитрее обработать пропуски?
train.dropna(inplace=True)
test.dropna(inplace=True)
# %%
find_nulls(train).head(10)
# %%
train.shape
# %%
# не знаю что это за признаки. Посмотрел, все равно непонятно - уберу
train.select_dtypes(include='object').columns
# %%
# train.iloc[:, 1:770]
train.iloc[:, 0]
# %%
X = train.iloc[:, 1:770]
y = train.iloc[:, 0]
# %%
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=14)
# %%
