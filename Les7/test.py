from matplotlib import pyplot as plt
# %matplotlib inline
import seaborn as sns
import pandas as pd
import numpy as np
# from sklearn.datasets import load_boston
from sklearn.preprocessing import Normalizer, StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_colwidth', None)
pd.set_option('display.expand_frame_repr', False)

#boston_data = load_boston()
data_url = "http://lib.stat.cmu.edu/datasets/boston"
raw_df = pd.read_csv(data_url, sep="\s+", skiprows=22, header=None, engine='python')
data1 = np.hstack([raw_df.values[::2, :], raw_df.values[1::2, :2]])
target = raw_df.values[1::2, 2]
col = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT']
boston = pd.DataFrame(data1, columns=col)

# print(boston.head())
# print(boston)

x = boston
y = target
x_corr = x.copy()
x_corr['MEDV'] = y
correlation_matrix = x_corr.corr().round(2)
plt.subplots(figsize=(10, 7))
sns.heatmap(data=correlation_matrix, annot=True)

features = [['LSTAT', 'RM'], ['LSTAT', 'RM', 'PTRATIO'], ['LSTAT', 'RM', 'PTRATIO', 'TAX'], ['DIS', 'AGE'],
            ['DIS', 'RAD']]

"""##Оцениваем результат"""

metrics = pd.DataFrame(columns=['Features', 'MAE train', 'MAE test', 'MSE train', 'MSE test', 'R2 train', 'R2 test'])


for future in features:
    x_future_test = x.loc[:, future]
    x_train, x_test, y_train, y_test = train_test_split(x_future_test, y, test_size=0.2, random_state=5)

    transformer = Normalizer().fit(x_train.loc[:, x_train.columns])
    x_train = pd.DataFrame(transformer.transform(x_train.loc[:, x_train.columns]), index=x_train.index,
                           columns=x_train.columns)
    x_test = pd.DataFrame(transformer.transform(x_test.loc[:, x_test.columns]), index=x_test.index,
                          columns=x_test.columns)

    regr = LinearRegression()
    regr.fit(x_train, y_train)
    pred_train = regr.predict(x_train)
    pred_test = regr.predict(x_test)

    metrics = metrics.append({'Features': future,
                              'MAE train': mean_absolute_error(y_train, pred_train),
                              'MAE test': mean_absolute_error(y_test, pred_test),
                              'MSE train': mean_squared_error(y_train, pred_train),
                              'MSE test': mean_squared_error(y_test, pred_test),
                              'R2 train': r2_score(y_train, pred_train),
                              'R2 test': r2_score(y_test, pred_test)}, ignore_index=True)

print(metrics)