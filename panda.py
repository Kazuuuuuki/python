from pandas import Series, DataFrame
import pandas as pd
import numpy as np

obj = Series([4, 7, -5, 3])
obj2 = Series([4, 7, -5, 3], index=['d', 'b', 'a', 'x'])

# print(obj2[['c', 'd', 'a']])
#
# print(obj2[obj2 > 2])

# print('b' in obj2)

sdata = {'Ohio': 35000, 'Texas': 71000, 'Oregon': 16000, 'Utah':5000}

obj3 = Series(sdata)

data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevasa'],
        'year': [2000, 2001, 2002, 2001, 2002],
        'pop': [1.5, 1.7, 3.6, 2.4, 2.9]}

frame = DataFrame(data)

# print(frame)

frame2 = DataFrame(data, columns=['year', 'state', 'pop', 'debt'],
                    index=['one', 'two', 'three', 'four', 'five'])

# print(frame2.ix['three'])

pop = {'Nevada': {2001: 2.4, 2002: 2.9},
       'Ohio': {2000: 1.5, 2001: 1.7, 2002: 3.6}}

frame3 = DataFrame(pop)

# print(frame3.T)

obj = Series(range(3), index=['a', 'b', 'c'])
index = obj.index

index = pd.Index(np.arange(3))

print(index)

obj2 = Series([1.5, -2.5, 0], index=index)
obj2.index is index