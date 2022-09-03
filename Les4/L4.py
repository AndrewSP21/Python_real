# Импортируем нужные библиотеки
import pandas as pd
import requests, zipfile, io #работает с архивами
import matplotlib.pyplot as plt #работает с графиками и диаграммами
import seaborn as sns #работает с графиками и диаграммами
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_colwidth', None)
pd.set_option('display.expand_frame_repr', False)
'''Считываем файл'''
rw = requests.get('https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv')
ww = requests.get('https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-white.csv')
'''Формируем датафрейм'''
winered = pd.read_csv(io.BytesIO(rw.content), header=0, sep=';')
winewhite = pd.read_csv(io.BytesIO(ww.content), header=0, sep=';')


'''Добавляем столбец good'''
winered['good'] = winered['quality'].apply(lambda x: 1 if x > 5 else 0)
winewhite['good'] = winewhite['quality'].apply(lambda x: 1 if x > 5 else 0)
winered['good_q'] = winered['quality'].apply(lambda x: 'Good' if x > 5 else 'Bad')
winewhite['good_q'] = winewhite['quality'].apply(lambda x: 'Good' if x > 5 else 'Bad')

#
# data1 = winered['good_q'].value_counts()
# plt.figure(figsize = (10,7))
# plt.pie(data1, autopct='%1.1f%%')
# plt.title('Оценки качества Красного вина')
# plt.legend(data1.index)
# plt.show()
# plt.close()
#
# data2 = winewhite['good_q'].value_counts()
# plt.figure(figsize = (10,7))
# plt.pie(data2, autopct='%1.1f%%')
# plt.title('Оценки качества Белого вина')
# plt.legend(data2.index)
# plt.show()
# plt.close()

# print(data1.head())
# print(data2.head())


# Строим боксплот зависимость качества Белого вина от уровня алкоголя 
def boxplot_quality(wine, value, df):
    qhigh = df[value].loc[df['good'] == 1]
    qlower_middle = df[value].loc[df['good'] == 0]
    plt.figure(figsize=(10, 7))
    plt.boxplot([qhigh, qlower_middle])  # , winered_high, winered_lower_middle])
    plt.title(wine + ', показатель: ' + value)
    plt.xlabel('Качество')
    plt.ylabel('Показатель: ' + value)
    plt.xticks([1, 2], ['Высокое', 'Ниже среднего'])
    # plt.savefig('boxplot_quality_' + wine + '_' + value +'.png')
    plt.show()
    plt.close()

# boxplot_quality('Белое вино', 'alcohol', winewhite)
# for el in winewhite.columns:
#     if el not in ('quality', 'good'):
#         boxplot_quality('Белое вино', el, winewhite)
#
# for el in winered.columns:
#     if el not in ('quality', 'good'):
#         boxplot_quality('Красное вино', el, winered)


'''
# Строим корреляционную матрицу
correlation = winewhite.corr()
plt.figure(figsize = (10,7))
sns.heatmap(correlation, cmap = 'Blues', annot = True)
plt.title('Корреляционаая матрица')
plt.savefig('Corr_matrix.png')
'''
print(winered.head())
# wrfa = winered['fixed acidity'].value_counts()
# wrva = winered['volatile acidity'].value_counts()
# wrca = winered['citric acid'].value_counts()
# wrrs = winered['residual sugar'].value_counts()
# wrch = winered['chlorides'].value_counts()
# wrfsd = winered['free sulfur dioxide'].value_counts()
# wrtsd = winered['total sulfur dioxide'].value_counts()
# wrde = winered['density'].value_counts()
# wrph = winered['pH'].value_counts()
# wrsu = winered['sulphates'].value_counts()
# wral = winered['alcohol'].value_counts()
#
data = winered[['fixed acidity','volatile acidity','citric acid', 'residual sugar', 'chlorides','free sulfur dioxide', 'total sulfur dioxide','density', 'pH', 'sulphates' ]]
sns.pairplot(data)
plt.show()
# print(wrfa)
# print(wrva)
# print(wrca)
# print(wrrs)
# print(wrch)
# print(wrfsd)
# print(wrtsd)
# print(wrde)
# print(wrph)
# print(wrsu)
# print(wral)

def hist_quality(wine, value, df):
    plt.figure(figsize = (10,7))
    plt.hist(df[value].loc[df['good'] == 1], alpha = 0.3, label = 'good') #, bins = 20)
    plt.hist(df[value].loc[df['good'] == 0], alpha = 0.3, label = 'bad') #, bins = 20)
    plt.title(wine + ', показатель: ' + value)
    plt.xlabel('Интервал показателя')
    plt.ylabel('Количество')
    plt.legend()
    plt.savefig('hist_quality_' + wine + '_' + value + '.png')
    plt.close()

#
# hist_quality('Белое вино', 'volatile acidity', winewhite)
# hist_quality('Красное вино', 'volatile acidity', winered)
# hist_quality('Белое вино', 'citric acid', winewhite)
# hist_quality('Красное вино', 'citric acid', winered)


# for el in winewhite.columns:
#     if el not in ('quality', 'good'):
#         hist_quality('Белое вино', el, winewhite)
#
# for el in winered.columns:
#     if el not in ('quality', 'good'):
#         hist_quality('Красное вино', el, winered)
#
# sns.jointplot(y=winered['residual sugar'], x=winered['good'], data=winered, kind='reg')
# plt.show()

data = winered[['quality' ]]
sns.pairplot(data)
plt.show()