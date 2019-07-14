# Python

```python
my_list = ['a', 'b', 'c', 'd']

my_dict1 = {'k1': 'v1', 'k2': 'v2', 'k3': 'v3'}

my_dict2 = {'k1': 'v1',
            'k2': 'v2',
            'k3': 'v3'}
```


# Pandas

```python
df.rename(columns={'c1': 'c2', 'c3': 'c4', 'c5': 'c6'}, inplace=True)

df.sort_values(['c1', 'c2', 'c3'], ascending=[True, True, True], inplace=True)

pd.merge(df1, df2, left_on='a', right_on='b', how='left')

df.pivot_table(index=['c1', 'c2'], columns=['c3', 'c4'], aggfunc={'c3': 'count', 'c4': sum})

df.apply(lambda row: row['col'], axis=1)
```
