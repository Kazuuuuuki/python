import json

# def get_counts(sequence):
#     counts = {}
#     for x in sequence:
#         if x in counts:
#             counts[x] += 1
#         else:
#             counts[x] = 1
#
#     return counts

from collections import defaultdict
from collections import Counter

from pandas import DataFrame, Series
import pandas as pd; import numpy as np

def get_counts(sequence):
    counts = defaultdict(int)
    for x in sequence:
        counts[x] += 1
    return counts

def top_counts(count_dict, n=10):
    value_key_pairs = [(count, tz) for tz, count in count_dict.items()]
    value_key_pairs.sort()
    return value_key_pairs[-n:]

path = 'pydata-book/ch02/usagov_bitly_data2012-03-16-1331923249.txt'
records = [json.loads(line) for line in open(path)]

time_zones = [rec['tz'] for rec in records if 'tz' in rec]
counts = Counter(time_zones)
# print(counts.most_common(10))

frame = DataFrame(records)

clean_tz = frame['tz'].fillna('Missing')
clean_tz[clean_tz == ''] = 'Unknown'
tz_counts = frame['tz'].value_counts()

results = Series([x.split()[0] for x in frame.a.dropna()])
# print(results.value_counts()[:8])

cframe = frame[frame.a.notnull()]
# print(cframe['a'].str.contains('Windows'))
operating_system = np.where(cframe['a'].str.contains('Windows'), 'Windows', 'Not Windows')
# print(operating_system[:5])
by_tz_os = cframe.groupby(['tz', operating_system])
agg_counts = by_tz_os.size().unstack().fillna(0)
indexer = agg_counts.sum(1).argsort()
count_subset = agg_counts.take(indexer)[-10:]
print(count_subset)
count_subset.plot(kind='barh', stacked=True)

normed_subset = count_subset.div(count_subset.sub(1), axis=0)
normed_subset.plot(kind='barh', stacked=True)
# print(indexer[:10])
# print(frame['tz'][:10])
# print(tz_counts[:10])

# tz_counts[:10].plot(kind='barh', rot=0)


