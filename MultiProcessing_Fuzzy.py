# Synchronous Processing
import pandas as pd
df1=pd.read_csv(r'C:\Users\Menda Jawahar\Downloads\endole_data_uk.csv')

from fuzzywuzzy import fuzz

class multipoolexecutor:
    def __init__(self,df):
        self.df=df
    def fuzzratio(self):
        l=[]
        for i in range(len(self)):
            l.append(fuzz.ratio(self['name'][i],self['URL'][i]))
        return l

import datetime

t1=datetime.datetime.now()
multipoolexecutor.fuzzratio(df1)
t2=datetime.datetime.now()
print(t2-t1)

# Time taken 0:01:14.714166

# Multi Processing

from concurrent.futures import ProcessPoolExecutor

def fuzzratio(data):
    l=[]
    for i in range(len(data)):
        l.append(fuzz.ratio(data['name'][i],data['URL'][i]))
    return l

t1=datetime.datetime.now()
with ProcessPoolExecutor(max_workers=8) as executor:
    future = executor.map(fuzzratio,df1)
t2=datetime.datetime.now()
print(t2-t1)

# Time taken 0:00:00.208451