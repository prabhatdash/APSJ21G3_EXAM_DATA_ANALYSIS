import pandas as pd
import matplotlib as plt
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
mathscore=list(df.math_scores)
readscore=list(df.reading_scores)
writingscore=list(df.writing_scores)
for i in gen:
    if("male"==i):
        c1=c1+1 #c1 is the count of males
    else:
        c2=c2+1 #c2 is the count of females
x=np.arange(4)
mm1=df[df['gender']=='male'].mathscore.max() #male highest math marks
mm2=df[df['gender']=='female'].mathscore.max() #female highest math marks      
mr1=df[df['gender']=='male'].readscore.max() #male highest read marks
mr2=df[df['gender']=='female'].readscore.max() #female highest read marks
mw1=df[df['gender']=='male'].writingscore.max() #male highest writing marks
mw2=df[df['gender']=='female'].writingscore.max() #female highest writing marks
plt.bar(x,[mm1,mr1,mw1],widht=0.25,color='r',label='Male')
plt.bar(x+0.50,[mm2,mr2,mw2],widht=0.25,color='b',label='Female')
plt.ylabel("Highest Marks")
plt.xlabel("Gender")
plt.legend(loc=2)
plt.title("Highest marks across different genders")




