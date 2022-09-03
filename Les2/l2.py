'''
1. Загрузить, просмотреть, определить количество строк и склеить 3 датасета: marketing_campaign.csv, users.csv и subscribers.csv.
'''

import pandas as pd
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_colwidth', None)
pd.set_option('display.expand_frame_repr', False)

dfm = pd.read_csv('marketing_campaign.csv', header=0, sep=',')
dfs = pd.read_csv('subscribers.csv', header=0, sep=',')
dfu = pd.read_csv('users.csv', header=0, sep=',')


#
# print(f'{dfm.head()} \n {dfs.head()} \n\n {dfu.head()}')
# print(f'Строк в marketing_campaign.csv: {len(dfm.index)} \nСтрок в subscribers.csv: {len(dfs.index)}\nСтрок в '
#       f'users.csv: {len(dfu.index)}')


a = dfm.merge(dfu, left_on=['user_id'], right_on=['user_id'], how='left')
b = a.merge(dfs, left_on=['user_id'], right_on=['user_id'], how='left')
# print(f' {a.info()}')
# print(f' {b.info()}')

'''
2. Определить количество, типы и описательные статистики колонок (столбцов) получившегося датасета.
'''
# print(b.describe())


'''
3. Определить эффективность маркетинговых каналов по привлечению платящих игроков.
'''
paying = b[b['converted'] == 1]
c = paying['marketing_channel'].value_counts()
print(c)

'''
4. Определить самую раннюю дату подписки на сервис.
'''
'''----------------Преобразуем столбец date_subscribed в дату------------'''
# from datetime import datetime
# b['date_subscribed'] = pd.to_datetime(b['date_subscribed'])
# d = b['date_subscribed'].min()
# print(datetime.strftime(d, '%d.%m.%Y'))

'''
5. Определить портрет аудитории удержанных подписчиков (по возрасту и языку).
'''
# b['is_retained'] = b['is_retained'].astype('bool')
# # print(b.head())
# # print(b.info())
# retained = b[b['is_retained'] == True]
# # print(retained.head())
# # f = retained['age_group', 'language_preferred'].value_counts()
# age = retained['age_group'].value_counts(normalize=True)
# lang = retained['language_preferred'].value_counts(normalize=True)
# print(age)
# print(lang)
#
# g = b.groupby(['language_preferred', 'age_group'], as_index=False).count()
# g = g[['language_preferred', 'age_group', 'user_id']]
# g_sort = g.sort_values(by=['language_preferred', 'user_id'], ascending=[True, False])
# print(g_sort)
