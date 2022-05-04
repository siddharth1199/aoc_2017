"""
i create a pandas series for each of the 10 criteria.  Using the Sue# as an index, I can then merge each individual series together to form a 500 x 10 dataframe.
From there, I can simply filter out the Sue's that don't match my criteria
"""

import pandas as pd
df = pd.read_csv("input.txt", sep = ":|,", names = ['Sue', 'Detail_1', 'Detail_1_val', 'Detail_2', 'Detail_2_val','Detail_3', 'Detail_3_val'])
df = df.set_index('Sue')



"""
Sue    Detail_1      Detail_1_val  Detail_2   Detail_2_val  Detail_3   Detail_3_val
Sue 1  goldfish      9            cars        0             samoyeds   9
Sue 2  perfumes      5            trees       8             goldfish   8
Sue 3  pomeranians   2            akitas      1             trees      5
Sue 4  goldfish      10           akitas      2             perfumes   9
Sue 5  cars          5            perfumes    6             akitas     9
"""

detail_list = [' children', ' cats', ' samoyeds', ' pomeranians', ' akitas', ' vizslas', ' goldfish', ' trees', ' cars', ' perfumes']


children_1 = pd.Series(df.Detail_1_val[df.Detail_1 == ' children'])
children_2 = pd.Series(df.Detail_2_val[df.Detail_2 == ' children'])
children_3 = pd.Series(df.Detail_3_val[df.Detail_3 == ' children'])
children = pd.concat([children_1, children_2, children_3])

cats_1 = pd.Series(df.Detail_1_val[df.Detail_1 == '  cats'])
cats_2 = pd.Series(df.Detail_2_val[df.Detail_2 == '  cats'])
cats_3 = pd.Series(df.Detail_3_val[df.Detail_3 == '  cats'])
cats = pd.concat([cats_1, cats_2, cats_3])

samoyeds_1 = pd.Series(df.Detail_1_val[df.Detail_1 == ' samoyeds'])
samoyeds_2 = pd.Series(df.Detail_2_val[df.Detail_2 == ' samoyeds'])
samoyeds_3 = pd.Series(df.Detail_3_val[df.Detail_3 == ' samoyeds'])
samoyeds = pd.concat([samoyeds_1, samoyeds_2, samoyeds_3])

pomeranians_1 = pd.Series(df.Detail_1_val[df.Detail_1 == ' pomeranians'])
pomeranians_2 = pd.Series(df.Detail_2_val[df.Detail_2 == ' pomeranians'])
pomeranians_3 = pd.Series(df.Detail_3_val[df.Detail_3 == ' pomeranians'])
pomeranians = pd.concat([pomeranians_1, pomeranians_2, pomeranians_3])

akitas_1 = pd.Series(df.Detail_1_val[df.Detail_1 == ' akitas'])
akitas_2 = pd.Series(df.Detail_2_val[df.Detail_2 == ' akitas'])
akitas_3 = pd.Series(df.Detail_3_val[df.Detail_3 == ' akitas'])
akitas = pd.concat([akitas_1, akitas_2, akitas_3])

vizslas_1 = pd.Series(df.Detail_1_val[df.Detail_1 == ' vizslas'])
vizslas_2 = pd.Series(df.Detail_2_val[df.Detail_2 == ' vizslas'])
vizslas_3 = pd.Series(df.Detail_3_val[df.Detail_3 == ' vizslas'])
vizslas = pd.concat([vizslas_1, vizslas_2, vizslas_3])

goldfish_1 = pd.Series(df.Detail_1_val[df.Detail_1 == ' goldfish'])
goldfish_2 = pd.Series(df.Detail_2_val[df.Detail_2 == ' goldfish'])
goldfish_3 = pd.Series(df.Detail_3_val[df.Detail_3 == ' goldfish'])
goldfish = pd.concat([goldfish_1, goldfish_2, goldfish_3])

trees_1 = pd.Series(df.Detail_1_val[df.Detail_1 == ' trees'])
trees_2 = pd.Series(df.Detail_2_val[df.Detail_2 == ' trees'])
trees_3 = pd.Series(df.Detail_3_val[df.Detail_3 == ' trees'])
trees = pd.concat([trees_1, trees_2, trees_3])

cars_1 = pd.Series(df.Detail_1_val[df.Detail_1 == ' cars'])
cars_2 = pd.Series(df.Detail_2_val[df.Detail_2 == ' cars'])
cars_3 = pd.Series(df.Detail_3_val[df.Detail_3 == ' cars'])
cars = pd.concat([cars_1, cars_2, cars_3])

perfumes_1 = pd.Series(df.Detail_1_val[df.Detail_1 == ' perfumes'])
perfumes_2 = pd.Series(df.Detail_2_val[df.Detail_2 == ' perfumes'])
perfumes_3 = pd.Series(df.Detail_3_val[df.Detail_3 == ' perfumes'])
perfumes = pd.concat([perfumes_1, perfumes_2, perfumes_3])

final = pd.DataFrame(pd.concat([children, cats, samoyeds, pomeranians, akitas, vizslas, goldfish, trees, cars, perfumes], axis = 1))



criteria = pd.Series( data = {'children': 3,
'cats': 7,
'samoyeds':2,
'pomeranians': 3,
'akitas': 0,
'vizslas': 0,
'goldfish': 5,
'trees': 3,
'cars': 2,
'perfumes': 1})

final_filtered = final

for i in range(0,10):
    final_filtered = final_filtered[(final_filtered[i] == criteria[i]) | (final_filtered[i].isnull())]


print(final_filtered.index)

criteria = pd.DataFrame( data = {'details': ['children', 'cats', 'samoyeds', 'pomeranians', 'akitas', 'vizslas', 'goldfish', 'trees', 'cars', 'perfumes'],
                                 'criteria': [3,7,2,3,0,0,5,3,2,1],
                                 'Assignment': ['Equal', 'Greater', 'Equal', 'Less', 'Equal', 'Equal', 'Less', 'Greater', 'Equal', 'Equal']})

for i in range(0,10):
    if criteria.iloc[i,2] == 'Equal':
        final = final[(final[i] == criteria.iloc[i,1]) | (final[i].isnull())]
    elif criteria.iloc[i,2] == 'Less':
        final = final[(final[i] < criteria.iloc[i,1]) | (final[i].isnull())]
    elif criteria.iloc[i,2] == 'Greater':
        final = final[(final[i] > criteria.iloc[i,1]) | (final[i].isnull())]

print(final.index)
