import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df=pd.read_csv('dataset.csv',engine="python")
def sexratio():
    m = 0
    f = 0
    male = list(df.gender == "male")
    for i in male:
        if i == True:
            m = m + 1
        else:
            f = f + 1
    ratio = str(m) + ":" + str(f)
    print("The Male to Female ratio is: "+ratio)
def highestmarks():
    print(df["math_score"].max(), "  -Highest math score")
    print(df["reading_score"].max(), "  -Highest reading score")
    print(df["writing_score"].max(), "  -Highest writing score")
def studentspassed():
    math = list(df.math_score)
    writing = list(df.writing_score)
    reading = list(df.reading_score)
    sum = []
    for (i, j, k) in zip(math, writing, reading):
        sum_ = (i + j + k)
        sum.append(sum_)
    c = 0
    for l in sum:
        if l >= 200:
            c = c + 1
        else:
            pass
    print("No. of students passed are :- ", c)

