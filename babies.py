import pandas as pd
import numpy as np
names1880 = pd.read_csv('pydata-book/ch02/names/yob1880.txt', names=['name', 'sex', 'births'])
#
# print(names1880.groupby('sex').births.sum())


years = range(1880, 2011)
pieces = []
columns = ['name', 'sex', 'births']

for year in years:
    path = 'pydata-book/ch02/names/yob%d.txt' % year
    frame = pd.read_csv(path, names=columns)

    frame['year'] = year
    pieces.append(frame)

names = pd.concat(pieces, ignore_index=True)

total_births = names.pivot_table('births', index='year', columns='sex', aggfunc=sum)

# print(total_births.tail())
# def add_plop(group):
#     births = group.births.astype(float)
#
#     group['prop'] = births / births.sum()
#     return group
#
# names = names.groupby(['year', 'sex']).apply(func=add_prop)
#
# print(names)
#
# print(np.allclose(names.groupby(['year', 'sex']).prop.sum(), 1))

def get_top1000(group):
    return group.sort_values(by='births', ascending=False)[:1000]

grouped = names.groupby(['year', 'sex'])
top1000 = grouped.apply(get_top1000)