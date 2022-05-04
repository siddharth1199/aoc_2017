import pandas as pd

# import time
# tic = time.time()
Day_5 = open("input.txt", "r")
data = Day_5.read()
day_5_list = (data.split("\n"))


# count if the same character is repeated
def double_char(s):
    i = 0
    char_counter = 0
    while (i < len(s) - 1):

        if s[i] == s[i + 1]:
            char_counter = 1
            i += 1
        i += 1
    return char_counter


# count the number of vowels
def vowel_counter(s):
    i = 0
    vowel_counter = 0
    while (i < len(s)):

        if s[i] == "a" or s[i] == "e" or s[i] == "i" or s[i] == "o" or s[i] == "u":
            vowel_counter += 1

        i += 1
    return (vowel_counter)


# look for specific text
text_list = ["ab", "cd", "pq", "xy"]
rows = []
for i in day_5_list:
    rows.append([i, double_char(i), vowel_counter(i), any(ele in i for ele in text_list)])

day_5_df = pd.DataFrame(rows, columns=["Text", "Double_Char", "Vowel_Count", "Text_String"])

day_5_df.loc[(day_5_df["Double_Char"] > 0) & (day_5_df["Vowel_Count"] > 2) & (
            day_5_df["Text_String"] == False), "Nice_Words"] = 1

print(day_5_df.Nice_Words.sum())
# toc = time.time()
# print("For loop time:" + str(1000*(toc-tic))+" ms")
# typical run time is ~23 ms
