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
df.rename(columns={'col1': 'col1a', 'col2': 'col2a'}, inplace=True)

df.sort_values(['col1', 'col2', 'col3'], ascending=[True, True, True], inplace=True)

pd.merge(df1, df2, left_on='col1', right_on='col2', how='left')

df.pivot_table(index=['col1', 'col2'], columns=['col3', 'col4'], 
                     aggfunc={'col3': 'count', 'col4': sum})
```
