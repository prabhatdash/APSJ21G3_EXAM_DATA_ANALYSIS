import pandas as pd

df=pd.read_csv('dataset.csv',engine="python")
math=list(df.math_score)
writing=list(df.writing_score)
reading=list(df.reading_score)

avgf=[]
avgm=[]
sum=[]
val=df[df['gender']=='male']
scr=val['math_score']
print(val['gender'].count())
print(scr.sum())
# for (i,j,k) in zip(math,writing,reading):
#         avg=(i+j+k)/3
#         for m in gender:
#             if m==True:
#                 avgm=avgm.append(avg)
#             else:
#                 avgf=avgf.append(avg)





