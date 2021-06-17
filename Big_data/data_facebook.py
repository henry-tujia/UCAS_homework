import data_get
import pandas as pd

df_ = pd.read_csv('twitter_combined.txt', sep=' ', header=None)
df_.columns = ['column1', 'column2']

ids = df_['column1'].tolist()
ids_ = df_['column2'].tolist()

all_id = set(ids_ + ids)
is_list = list(all_id)
is_list.sort()
voca = dict(zip(is_list, range(len(all_id))))

df1 = df_['column1'].apply(lambda x:voca.get(x))

df2 = df_['column2'].apply(lambda x:voca.get(x))

df = pd.concat([df1,df2],axis=1)

martix = data_get.creat_martix(df)

# a = martix.toarray()
u, s, vt = data_get.svd(martix, k=10)
data_get.save(u.real, 'TW_U')
data_get.save(vt.real, 'TW_V')

print('ok')
