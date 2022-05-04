import numpy as np
import pandas as pd

# Day 3

# part i

Day_3 = open("input.txt", "r")
Day_3_data = Day_3.read()

Day3_string = str(Day_3_data)
len(Day_3_data)

#Day_3_data
split_strings = []
n  = 1
for index in range(0, len(Day_3_data), n):
    split_strings.append(Day_3_data[index : index + n])
print(split_strings)

Day_3_df = pd.DataFrame(split_strings)
Day_3_df.columns = ["Character"]
Day_3_df.head()

Day_3_df.loc[Day_3_df['Character'] == '>', 'X_value'] = 1
Day_3_df.loc[Day_3_df['Character'] == '<', 'X_value'] = -1
Day_3_df.loc[Day_3_df['Character'] == '^', 'X_value'] = 0
Day_3_df.loc[Day_3_df['Character'] == 'v', 'X_value'] = 0
Day_3_df.loc[Day_3_df['Character'] == '>', 'Y_value'] = 0
Day_3_df.loc[Day_3_df['Character'] == '<', 'Y_value'] = 0
Day_3_df.loc[Day_3_df['Character'] == '^', 'Y_value'] = 1
Day_3_df.loc[Day_3_df['Character'] == 'v', 'Y_value'] = -1

Day_3_df["X_Cum_Sum"] = Day_3_df["X_value"].cumsum()
Day_3_df["Y_Cum_Sum"] = Day_3_df["Y_value"].cumsum()

a = np.char.array(Day_3_df['X_Cum_Sum'].values)
b = np.char.array(Day_3_df['Y_Cum_Sum'].values)
Day_3_df['Coordinates'] = (a + b', - ' + b).astype(str)

print(Day_3_df.shape)
Day_3_df_dedup = Day_3_df.drop_duplicates(subset=['Coordinates'])
print(Day_3_df_dedup.shape)

# Part 2
Day_3_df["santa"] = Day_3_df.index.values % 2

robo_santa = Day_3_df[Day_3_df.santa == 0]
real_santa = Day_3_df[Day_3_df.santa == 1]

robo_santa["X_Cum_Sum"] = robo_santa["X_value"].cumsum()
robo_santa["Y_Cum_Sum"] = robo_santa["Y_value"].cumsum()

real_santa["X_Cum_Sum"] = real_santa["X_value"].cumsum()
real_santa["Y_Cum_Sum"] = real_santa["Y_value"].cumsum()

a = np.char.array(robo_santa['X_Cum_Sum'].values)
b = np.char.array(robo_santa['Y_Cum_Sum'].values)
robo_santa['Coordinates'] = (a + b', - ' + b).astype(str)

a = np.char.array(real_santa['X_Cum_Sum'].values)
b = np.char.array(real_santa['Y_Cum_Sum'].values)
real_santa['Coordinates'] = (a + b', - ' + b).astype(str)

Day_3_df_2 = pd.concat([robo_santa, real_santa])
Day_3_df_2_dedup = Day_3_df_2.drop_duplicates(subset=['Coordinates'])
print(Day_3_df_2_dedup.shape)
