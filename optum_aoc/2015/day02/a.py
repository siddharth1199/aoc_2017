import numpy as np
import pandas as pd

#Day 2

#part i

df = pd.read_csv("input.txt", sep="x", header=None, names=['Length', "Width", "Height"])

df.head()

a =df.values
b = a[np.arange(len(df))[:,None],np.argpartition(a,np.arange(3),axis=1)[:,:3]]

new_df = pd.DataFrame(b)

new_df.head()
new_df.columns = ['Shortest', 'Second_Shortest', 'Third_Shortest']

new_df["Sq_ft"] = 2*(new_df.Second_Shortest * new_df.Shortest) + 2*(new_df.Shortest * new_df.Third_Shortest) + 2*(new_df.Third_Shortest*new_df.Second_Shortest) + new_df.Shortest*new_df.Second_Shortest

print(new_df.Sq_ft.sum())

#Day 2

#part ii

df = pd.read_csv("input.txt", sep="x", header=None, names=['Length', "Width", "Height"])

df.head()

a =df.values
b = a[np.arange(len(df))[:,None],np.argpartition(a,np.arange(3),axis=1)[:,:3]]

new_df = pd.DataFrame(b)

new_df.head()
new_df.columns = ['Shortest', 'Second_Shortest', 'Third_Shortest']

new_df["cubic_ft"] = new_df.Second_Shortest*new_df.Shortest*new_df.Third_Shortest

new_df["perimeter"] = 2*(new_df.Shortest + new_df.Second_Shortest)

new_df["total_Ribbon"] = new_df.cubic_ft + new_df.perimeter

print(new_df.total_Ribbon.sum())
