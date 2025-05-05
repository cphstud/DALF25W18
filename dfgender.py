# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 11:13:23 2024

@author: thor
"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

#comlength = function(cell){}
def comlength(cell):
    retval=len(cell)
    return retval


def computegender(row):
    retval=""
    if row['Drengenavn_x']=="Ja":
        retval="M"
    elif row['Pigenavn']=="Ja":
        retval="F"
    else:
        retval="U"
    return retval

# import data

df=pd.read_csv("data/home.csv", encoding="iso-8859-1")

df.info()
df.describe()

# FE: length of reviews
df['length']=df['content'].apply(len)
df['length']=df['content'].apply(lambda x: len(x))
df['length']=df['content'].apply(comlength)

# plot distribution
sns.distplot(df['length'])
sns.boxplot(df['length'])

# subsetting
dfsub=df[(df['length'] > 100) & (df['length'] < 1000)]
dfsub=df.query('length > 100 & length < 1000')

# FE: fornavn
df['Navn']=df['name'].str.split()
df['Navn']=df['Navn'].apply(lambda x: x[0])
df['Navn']=df['Navn'].str.title()

# FE: gender ud fra liste med drenge og pigenavne

dfd=pd.read_excel("data/drenge.xlsx")
dfp=pd.read_excel("data/piger.xlsx")

dfdd=pd.merge(df, dfd,on="Navn",how="left")
dfdp=pd.merge(dfdd, dfp,on="Navn",how="left")
dfdd.drop(columns='Pigenavn', inplace=True)
dfdp.drop(columns='Drengenavn_y', inplace=True)

dfdp['gender']=dfdp.apply(computegender,axis=1)
dfdp['gender'].value_counts
sns.countplot(data=dfdp,x='gender')


# Sentida sentiment score
from sentida import Sentida
dfdp['sscore']=df['content'].apply(lambda x: Sentida().sentida(x,output="mean", normal=False) )

# plot
sns.distplot(dfdp['sscore'])
dfdp['sscore'].describe()

# score fordelt på køn
# FE: categorivariabel fra sscore
bins=['low','medium','high','very high']
intervals=[-2,0,1,1.5,6]
dfdp['scorecat']=pd.cut(dfdp['sscore'],labels=bins,bins=intervals, include_lowest=True)
sns.countplot(dfdp, x='scorecat')
sns.barplot(data=dfdp,x='gender',y='length', hue='scorecat')

### NLP ###
import nltk
# hele datasættet mhp wordcount - mest positive og mest negative
# byggende på aarup.csv
# samle alle reviews

dftotal = df['content'].str.cat() 
dftotalwords = nltk.word_tokenize(dftotal,language='danish')
dftotalwordsSub = [w for w in dftotalwords if len(w) > 4]
dftfd=nltk.FreqDist(dftotalwords)
dftfd=nltk.FreqDist(dftotalwordsSub)
dftfd.plot(10)

# remove danish stopwords
stdk=nltk.corpus.stopwords.words('danish')
stdk.append('vores')
dtt=dftotalwordsSub
dttst=[w for w in dtt if w not in stdk]
fd=nltk.FreqDist(dttst)
fd.plot(10)
dffreq = pd.DataFrame(list(fd.items()), columns=['Word', 'Frequency'])
 # join med aarups-sentiment 

afin=pd.read_csv("data/aarup.csv", encoding="iso-8859-1")
afin.rename(columns = {'stem':'Word'}, inplace=True)
dftotalstem=pd.merge(dffreq,afin,on='Word', how="inner")

# stem words
from nltk.stem.snowball import SnowballStemmer
stemmer = SnowballStemmer("danish")
dftotalstem['sw']=dftotalstem['Word'].apply(lambda x: stemmer.stem(x))

# plot 10 mest negative og 10 mest positive

dfpos=dftotalstem.sort_values('score', ascending=False).iloc[0:10]
dfneg=dftotalstem.sort_values('score', ascending=True).iloc[0:10]
dfneg=dfneg.sort_values('score', ascending=False)
ttt=pd.concat([dfpos,dfneg], axis=0)
ax=sns.barplot(ttt,y='Word',x='score')
ax.set_xticklabels(ax.get_xticklabels(), rotation=90)
plt.show()


























