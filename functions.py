import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
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

def avg_male_female():
    male = df[df['gender'] == 'male']
    math_male = male['math_score']
    reading_male = male['reading_score']
    writing_male = male['writing_score']
    m = (male['gender'].count())
    m_m = math_male.sum()
    w_m = writing_male.sum()
    r_m = reading_male.sum()
    avg_m = ((m_m + w_m + r_m) / 3) / m
    print("THE AVERAGE SCORE OF MALE STUDENTS   : ", avg_m)
    female = df[df['gender'] == 'female']
    math_female = female['math_score']
    reading_female = female['reading_score']
    writing_female = female['writing_score']
    fm = (female['gender'].count())
    m_fm = math_male.sum()
    w_fm = writing_female.sum()
    r_fm = reading_female.sum()
    avg_fm = ((m_fm + w_fm + r_fm) / 3) / fm
    print("THE AVERAGE SCORE OF FEMALE STUDENTS : ", avg_fm)
def highestlowestscore():
    math = list(df.math_score)
    writing = list(df.writing_score)
    reading = list(df.reading_score)
    sum = []
    for (i, j, k) in zip(math, writing, reading):
        sum_ = (i + j + k)
        sum.append(sum_)
    print("THE HIGHEST SCORE BY A STUDENT IS :- ", max(sum), "\nTHE LOWEST SCORE BY A STUDENT IS  :- ", min(sum))


def tabularavgscores():
    male = df[df['gender'] == 'male']
    math_male = male['math_score']
    reading_male = male['reading_score']
    writing_male = male['writing_score']
    m = (male['gender'].count())
    m_m = math_male.sum()
    w_m = writing_male.sum()
    r_m = reading_male.sum()
    avg_m_m = m_m / m
    avg_r_m = r_m / m
    avg_w_m = w_m / m
    avg_m = ((m_m + w_m + r_m) / 3) / m

    female = df[df['gender'] == 'female']
    math_female = female['math_score']
    reading_female = female['reading_score']
    writing_female = female['writing_score']
    fm = (female['gender'].count())
    m_fm = math_male.sum()
    w_fm = writing_female.sum()
    r_fm = reading_female.sum()
    avg_m_fm = m_fm / fm
    avg_r_fm = r_fm / fm
    avg_w_fm = w_fm / fm
    avg_fm = ((m_fm + w_fm + r_fm) / 3) / fm
    avg_dict = {"AVERAGE MATH SCORE": [avg_m_m, avg_m_fm], "AVERAGE READING SCORE": [avg_r_m, avg_r_fm],
                'AVERAGE WRITING SCORE': [avg_w_m, avg_w_fm]}

    avg_df = pd.DataFrame(avg_dict, index=['MALE', 'FEMALE'])
    print(
        'THE TABULAR DISPLAY OF THE AVERAGE SCORES IN DIFFERENT SUBJECTS BY MALE AND FEMALE STUDENTS IS GIVEN BELOW:-\n')
    print(avg_df)
