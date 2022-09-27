# -*- coding: utf-8 -*-
"""
Created on Sun Jan 17 12:56:03 2021

@author: JiM
"""
# plot blood pressure
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
df=pd.read_csv('blood_pressure2.csv')
df2=pd.read_csv('bp_old_machine.csv')
datet=[]
for k in range(len(df)):
    datet.append(pd.to_datetime(df['date'][k]+' '+str(df['time'][k]),format='%m/%d/%Y %H%M'))
df['datet']=datet
df=df.set_index('datet')
df=df.drop(['date','time','pulse'],axis=1)
datet=[]
for k in range(len(df2)):
    datet.append(pd.to_datetime(df2['date'][k]+' '+str(df2['time'][k]),format='%m/%d/%Y %H%M'))
df2['datet']=datet
df2=df2.set_index('datet')
df2=df2.drop(['date','time'],axis=1)
df2=df2.dropna()
df.rename(columns={'systolic':'raw_s'},inplace=True)
df.rename(columns={'diastolic':'raw_d'},inplace=True)
plt.rcParams["figure.figsize"] = [12,9]
fig, ax = plt.subplots(1, 1)
df.plot(ax=ax)
for j in range(len(df)):
    if isinstance(df.notes.values[j],str):
        ax.text(df.index.values[j],90,df.notes.values[j],horizontalalignment='center',rotation=90)
dfw=df.resample('W').mean()
dfw.rename(columns={'raw_s':'weekly_s'},inplace=True)
dfw.rename(columns={'raw_d':'weekly_d'},inplace=True)

plt.plot([df.index[0],df.index[-1]],[150,150],color='k')
ax.plot(df2,label='old machine')
dfw.plot(ax=ax).legend(loc='best')
plt.text(df.index[-1],150,'150')
plt.text(df.index[-1],80,'80')
plt.plot([df.index[0],df.index[-1]],[80,80],color='k')
plt.show()
ax.set_title('Manning: medication vs exercise?')
fig.savefig('manning_blood_pressure.png')