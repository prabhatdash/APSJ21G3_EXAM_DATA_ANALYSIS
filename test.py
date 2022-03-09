from turtle import width
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
df=pd.read_csv('dataset.csv',engine="python")
# math=list(df.math_score)
# writing=list(df.writing_score)
# reading=list(df.reading_score)
#
# avgf=[]
# avgm=[]
# sum=[]
# male=df[df['gender']=='male']
# math_male=male['math_score']
# reading_male=male['reading_score']
# writing_male=male['writing_score']
# m=(male['gender'].count())
# m_m=math_male.sum()
# w_m=writing_male.sum()
# r_m=reading_male.sum()
# avg_m_m=m_m/m
# avg_r_m=r_m/m
# avg_w_m=w_m/m
# avg_m=((m_m+w_m+r_m)/3)/m
#
# female=df[df['gender']=='female']
# math_female=female['math_score']
# reading_female=female['reading_score']
# writing_female=female['writing_score']
# fm=(female['gender'].count())
# m_fm=math_male.sum()
# w_fm=writing_female.sum()
# r_fm=reading_female.sum()
# avg_m_fm = m_fm/fm
# avg_r_fm = r_fm/fm
# avg_w_fm = w_fm/fm
# avg_fm=((m_fm+w_fm+r_fm)/3)/fm
# avg_dict={"AVERAGE MATH SCORE":[avg_m_m,avg_m_fm],"AVERAGE READING SCORE":[avg_r_m,avg_r_fm],'AVERAGE WRITING SCORE':[avg_w_m,avg_w_fm]}
#
# avg_df=pd.DataFrame(avg_dict,index=['MALE','FEMALE'])
# print('THE TABULAR DISPLAY OF THE AVERAGE SCORES IN DIFFERENT SUBJECTS BY MALE AND FEMALE STUDENTS IS GIVEN BELOW:-\n')
# print(avg_df)




# for (i,j,k) in zip(math,writing,reading):
#         avg=(i+j+k)/3
#         for m in gender:
#             if m==True:
#                 avgm=avgm.append(avg)
#             else:
#                 avgf=avgf.append(avg)

# math = list(df.math_score)
# writing = list(df.writing_score)
# reading = list(df.reading_score)
# sum = []
# for (i, j, k) in zip(math, writing, reading):
#     sum_ = (i + j + k)
#     sum.append(sum_)
# print("THE HIGHEST SCORE BY A STUDENT IS :- ",max(sum),"\nTHE LOWEST SCORE BY A STUDENT IS  :- ",min(sum))

gen=list(df.gender)
mathscore=list(df.math_score)
readscore=list(df.reading_score)
writingscore=list(df.writing_score)
c1=0
c2=0
for i in gen:
    if(i=="male"):
        c1=c1+1 #c1 is the count of males
    else:
        c2=c2+1 #c2 is the count of females
mm1=df[df['gender']=='male'].math_score.max() #male highest math marks
mm2=df[df['gender']=='female'].math_score.max() #female highest math marks      
mr1=df[df['gender']=='male'].reading_score.max() #male highest read marks
mr2=df[df['gender']=='female'].reading_score.max() #female highest read marks
mw1=df[df['gender']=='male'].writing_score.max() #male highest writing marks
mw2=df[df['gender']=='female'].writing_score.max() #female highest writing marks
s1=sum(mathscore)/(len(mathscore))
s2=sum(readscore)/(len(readscore))
s3=sum(writingscore)/len(writingscore)
plt.bar(["Maths","Reading","Writing"],[s1,s2,s3],color=['b','g','r'],width=0.50)
plt.title("Average marks across all subjects")
plt.show()