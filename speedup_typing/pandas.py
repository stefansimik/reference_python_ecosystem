import pandas as pd

df, df1, df2 = pd.DataFrame(), pd.DataFrame(), pd.DataFrame()

# ----------------------------------------
# PANDAS
# ----------------------------------------

df.apply(lambda row: row['col'], axis=1)

df.drop(columns=['c1', 'c2'], inplace=True)

pd.merge(df1, df2, left_on='a', right_on='b', how='left')
pd.merge(df1, df2, left_on=['a1', 'b1'], right_on=['a2', 'b2'], how='left')

df.pivot_table(index=['c1', 'c2'], columns=['c3', 'c4'], aggfunc={'c3': 'count', 'c4': sum})

df.rename(columns={'c1': 'c2', 'c3': 'c4', 'c5': 'c6'}, inplace=True)

df.reset_index(inplace=True)

df.sort_values(['c1', 'c2', 'c3'], ascending=[True, True, True], inplace=True)
