#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 11:33:18 2017

@author: soumak
@author: jzimmerman13
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

emotion = 3
def get_uniscore(wordtable,wordstring):
    wordemotion = np.array(wordtable[['word','score']],dtype=str)
    wordemotionstring = wordemotion[:,0]
    if(np.alen(wordemotion[wordemotionstring[:] == wordstring])>0):
        scorearray = wordemotion[wordemotionstring[:] == wordstring]
        return float(scorearray[0,1])
    else:
        return 0.0

def get_positive_uniscore(wordtable,wordstring):
    wordemotion = np.array(wordtable[['word','positive']],dtype=str)
    wordemotionstring = wordemotion[:,0]
    if(np.alen(wordemotion[wordemotionstring[:] == wordstring])>0):
        scorearray = wordemotion[wordemotionstring[:] == wordstring]
        return float(scorearray[0,1])
    else:
        return 0.0

def get_negative_uniscore(wordtable,wordstring):
    wordemotion = np.array(wordtable[['word','negative']],dtype=str)
    wordemotionstring = wordemotion[:,0]
    if(np.alen(wordemotion[wordemotionstring[:] == wordstring])>0):
        scorearray = wordemotion[wordemotionstring[:] == wordstring]
        return float(scorearray[0,1])
    else:
        return 0.0

def get_biscore(wordtable,wordstring1,wordstring2):
    wordemotion = np.array(wordtable[['word1','word2','score']],dtype=str)
    wordemotionstring = wordemoti:on[:,0]
    if(np.alen(wordemotion[wordemotionstring[:] == wordstring])>0):
        scorearray = wordemotion[wordemotionstring[:] == wordstring]
        return float(scorearray[0,1])
    else:
        return 0.0

def get_positive_biscore(wordtable,wordstring):
    wordemotion = np.array(wordtable[['word','positive']],dtype=str)
    wordemotionstring = wordemotion[:,0]
    if(np.alen(wordemotion[wordemotionstring[:] == wordstring])>0):
        scorearray = wordemotion[wordemotionstring[:] == wordstring]
        return float(scorearray[0,1])
    else:
        return 0.0

def get_negative_biscore(wordtable,wordstring):
    wordemotion = np.array(wordtable[['word','negative']],dtype=str)
    wordemotionstring = wordemotion[:,0]
    if(np.alen(wordemotion[wordemotionstring[:] == wordstring])>0):
        scorearray = wordemotion[wordemotionstring[:] == wordstring]
        return float(scorearray[0,1])
    else:
        return 0.0



def check_emotion(emotiontable,emotion,wordstring):
    try:
        return emotiontable.loc[wordstring,emotion]
    except:
        return 0

features = ['id','sentence','intensity']
unigram_wordtable=pd.read_table('./NRC-Sentiment-Emotion-Lexicons/Lexicons/NRC-Hashtag-Sentiment-Lexicon-v1.0/HS-unigrams.txt',header=None)
unigram_wordtable.columns = ['word','score','positive','negative']
bigram_wordtable=pd.read_table('./NRC-Sentiment-Emotion-Lexicons/Lexicons/NRC-Hashtag-Sentiment-Lexicon-v1.0/HS-bigrams.txt',header=None)
bigram_wordtable.columns = ['word1','score','positive','negative']
bigram_wordtable[['word1','word2']]=bigram_wordtable['word1'].str.split(' ',expand=True)

emotiontext = ''
emotionscores = './scoreddata/'

if emotion == 0:
    processeddataset = pd.read_csv('./processeddata/angertrainset.txt',names = features, sep='\t')
    emotiontext = 'anger'
    emotionscores += emotiontext+'emotionscores.txt'
elif emotion == 1:
    processeddataset = pd.read_csv('./processeddata/feartrainset.txt',names = features, sep='\t')
    emotiontext = 'fear'
    emotionscores += emotiontext+'emotionscores.txt'
elif emotion == 2:
    processeddataset = pd.read_csv('./processeddata/joytrainset.txt',names = features, sep='\t')
    emotiontext = 'joy'
    emotionscores += emotiontext+'emotionscores.txt'
elif emotion == 3:
    processeddataset = pd.read_csv('./processeddata/sadnesstrainset.txt',names = features, sep='\t')
    emotiontext = 'sadness'
    emotionscores += emotiontext+'emotionscores.txt'
else:
    processeddataset = pd.read_csv('./processeddata/valencetrainset.txt',names = features, sep='\t')

angerFeatureFrame = pd.DataFrame()
i = 0
for row in processeddataset['sentence']:
    row = row.replace('[','')
    row = row.replace(']','')
    row = row.replace('\'','')
    row = row.replace(' ','')
    score = 0.0
    for text in row.split(','):
        score = score + get_score(wordtable, emotiontext, text)
    h = pd.Series([str(processeddataset['id'][i]),str(score),str(processeddataset['intensity'][i])])
    angerFeatureFrame = angerFeatureFrame.append(h,ignore_index = True)
    i = i + 1

angerFeatureFrame.to_csv(emotionscores,header=['id','score','intensity'], index = False, sep='\t')
