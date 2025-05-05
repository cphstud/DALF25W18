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

def spacydf(document):
    data = []
    for token in doc:
        data.append({
            'text': token.text,
            'lemma': token.lemma_,
            'pos': token.pos_,
            'is_stop': token.is_stop
        })
    return pd.DataFrame(data)

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
#dfdd.drop(columns='Pigenavn', inplace=True)
dfdp.drop(columns='Drengenavn_y', inplace=True)

dfdp['gender']=dfdp.apply(computegender,axis=1)
dfdp['gender'].value_counts()
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
sns.barplot(data=dfdp,x='gender',y='length', hue='scorecat')

### NLP ###
import nltk
# hele datasættet mhp wordcount - mest positive og mest negative
# byggende på aarup.csv
# samle alle reviews

# Complete text
dftotal = df['content'].str.cat() 


dftotalwords = nltk.word_tokenize(dftotal,language='danish')
dftotalwordsSub = [w for w in dftotalwords if len(w) > 4]
#dftfd=nltk.FreqDist(dftotalwords)
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
#ax.set_xticklabels(ax.get_xticklabels(), rotation=90)
#plt.show()

# 
import spacy

nlp = spacy.load("da_core_news_sm")

# skateboard
testtext=dfdp.query('length == 500')
testtext=dfdp.loc[1200,'content']
doc=nlp(testtext)
len(doc)
testdf=spacydf(doc)

totaltext= ' '.join(dftotal)
totaldoc=nlp(dftotal)

totalnouns=[w.text for w in totaldoc if w.pos_ == "NOUN"]
fdt=nltk.FreqDist(totalnouns)
fdt.plot(20)

# get this as a dataframe
dffreqtotal = pd.DataFrame(list(fdt.items()), columns=['Word', 'Frequency'])

# bigrams
# clean the total corpus
import re
reviewtokens=nltk.word_tokenize(dftotal)
reviewtokenslow=[w.lower() for w in reviewtokens]
reviewtokenslowsub=[w for w in reviewtokenslow if len(w)>1]
reviewtokenslowsub2=[re.sub('[^-9A-ZÆØÅa-zæøå ]', '' , w) for w in reviewtokenslowsub ]
reviewtokenslow=reviewtokenslowsub2
bigr=list(nltk.bigrams(reviewtokenslow))
tigr=list(nltk.trigrams(reviewtokenslow))

# liste af KPI-navneord.
homekpi=dffreqtotal.sort_values('Frequency', ascending=False)
homekpiTop=homekpi.iloc[0:10]
homekpilist=list(homekpiTop['Word'])
homekpilist.append("forløb")

# finde bigrams hvor kpi forekommer
#fb = [b for b in bigr if b[0] in homekpilist or b[1] in homekpilist]
fbln = [b for b in bigr if b[1] in homekpilist]

# finde tillægsord i listen af KPI-relevante nouns og koble til AFINN
sw=list(afin['Word'])

## THIS IS LIST WITH IMPORTANT TUPLES
fblna = [b for b in fbln if b[0] in sw]

# test trigrams
tfb = [b for b in tigr if b[0] in homekpilist or b[1] in homekpilist or b[2] in homekpilist]

# alternativ med dataframes og merge da list-traversal tager tid
swdf=afin
swdf.rename(columns={'Word':'w1'}, inplace=True)
dfbig=pd.DataFrame(bigr,columns=['w1','w2'])
dfbigafin=pd.merge(dfbig,swdf,on='w1',how='left')

# counting bigrams
from collections import Counter
cts=Counter(fblna)

# count manually
biguniqu=dfbig.groupby(['w1','w2']).size().reset_index(name='Frequency')

len(cts.items())
dfcts=pd.DataFrame(cts.items(), columns=['Bigram','Value']) 
dfcts['w1']=dfcts['Bigram'].apply(lambda x: x[0])    
dfcts['w2']=dfcts['Bigram'].apply(lambda x: x[1])           
         


# ud af dette skal vi finde adjektiver
dfctssentiment=pd.merge(dfcts,afin,on='w2', how="left")


















