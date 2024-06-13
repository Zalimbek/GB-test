""" В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего из 
1 столбца. Ваша задача перевести его в one hot вид. Сможете ли вы это сделать без get_dummies?
"""
# С get_dummies
# import random
# import pandas as pd
# lst = ['robot'] * 10
# lst += ['human'] * 10
# random.shuffle(lst)
# data = pd.DataFrame({'whoAmI':lst})
# print(data)
# print(pd.get_dummies(data))
# data.head()

#Без get_dummies
import random
import pandas as pd
import numpy as np
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
print(data)
unique_vals = data['whoAmI'].unique()
one_hot_df = pd.DataFrame(0, index=data.index, columns=unique_vals)
for val in unique_vals:
    one_hot_df.loc[data['whoAmI']==val, val] = 1

print(one_hot_df)

