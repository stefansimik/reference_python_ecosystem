# Python

```python
my_list = ['a', 'b', 'c', 'd']

my_dict1 = {'key1': 'val1', 'key2': 'val2', 'key3': 'val3', 'key4': 'val4'}

my_dict2 = {'key1': 'val1',
            'key2': 'val2',
            'key3': 'val3',
            'key4': 'val4'}
```


# Pandas

```python
dfp = df.pivot_table(index='col1', columns='col2', aggfunc={'col1': 'count', 'col2': sum})
dfp = df.pivot_table(index=['col1', 'col2'], columns=['col3', 'col4'], aggfunc={'col1': 'count', 'col2': sum})

dfm = pd.merge(df1, df2, left_on='col1', right_on='col2', how='left')

df.rename(columns={'col1': 'col1a', 'col2': 'col2a'})
df.rename(columns={'col1': 'col1a', 'col2': 'col2a'}, inplace=True)

df.sort_values(['col1', 'col2', 'col3'])
df.sort_values(['col1', 'col2', 'col3'], inplace=True)
```
