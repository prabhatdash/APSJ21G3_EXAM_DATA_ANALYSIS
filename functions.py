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
    print(df["reading score"].max(), "  -Highest reading score")
    print(df["writing score"].max(), "  -Highest writing score")
