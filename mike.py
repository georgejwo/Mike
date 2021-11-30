# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 16:29:05 2021

@author: chocp
"""
import os
import matplotlib.pyplot as plt
import seaborn as sns
import tkinter as tk
import eikon as ek
import numpy as np
import pandas as pd
import blpapi
import pdblp
import configparser as cp
import cufflinks as cf
import bt
import talib as ta
#from scipy.stats import norm#for PDF and CDF
cfg=cp.ConfigParser()
cfg.read('eikon.cfg')
ek.set_app_key(cfg['eikon']['app_key'])
StartDate='2015-01-01'
EndDate='2021-10-31'
Interval='weekly'
rics_list = ['EUR=','BTC=','.HSI']
col_list = ['CLOSE','HIGH','LOW']
result = []    
def pearson_r(x,y):
    """Pearson's coefficient of correlation rho"""
    
    corcof = np.corrcoef(x, y)
    return corcof[0,1]

def extractor(rics, columns, start, end, interval):
    return ek.get_timeseries([rics], fields=columns,start_date=start,  end_date=end,interval=interval)

def pct_chg(rics, columns, start, end, interval):
    return extractor(rics, columns, start, end, interval).pct_change().dropna().to_numpy()

aa = pct_chg('EUR=','CLOSE','2015-01-01','2021-11-23','daily')
#btc=ek.get_timeseries(['BTC='], fields='*',start_date='2018-04-01',  end_date='2021-11-23',interval='daily')
for i in rics_list:
    for j in col_list:
        result.append(pct_chg(i,j,StartDate,EndDate,Interval))
print(type(result))
for i in result:
    
    print(i)
    print("*"*50)
print(len(result))

import plotly.express as px

df = px.data.gapminder().query("country=='Canada'")
fig = px.line(df, x="year", y="lifeExp", title='Life expectancy in Canada')
fig.show()