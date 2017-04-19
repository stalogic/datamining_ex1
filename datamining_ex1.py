# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 18:04:52 2017

@author: Jiang
"""

def count_plot(df):
    
    #分析标签属性的出现频数
    for attrid in labelattr:
        print(df[attrname[attrid-1]].value_counts())
        print()
        
    #数值属性的最小值，1/4分位数，中位数，均值，3/4分位数，最大值
    for attrid in valueattr:
        print(attrname[attrid - 1])
        series=df[attrname[attrid - 1]].apply(pd.to_numeric, errors='coerce')
        series=series[series.notnull()]
        print('min:',series.min())
        print('1/4 quantile:',series.quantile(0.25))
        print('mean:',series.mean())
        print('median:',series.median())
        print('3/4 quantile:',series.quantile(0.75))
        print('max:',series.max())
        print()
   
    #直方图
    for attrid in valueattr:
    #    print(attrname[attrid - 1])
        series=df[attrname[attrid - 1]]
        series=series.apply(pd.to_numeric, errors='coerce')
        fig=series.hist().get_figure()
        fig.savefig('./pngs/hist_'+attrname[attrid -1]+'.png')
        fig.clear()
    
    #qq图
    for attrid in valueattr:
        print(attrname[attrid - 1])
        series=df[attrname[attrid - 1]]
        series=series.apply(pd.to_numeric, errors='coerce')
        stats.probplot(series, dist="norm", plot=plt)
        fig=plt.gcf()
        fig.savefig('./pngs/qqplot_'+attrname[attrid -1]+'.png')
        fig.clear()
        
        
        
    #盒图    
    for attrid in valueattr:
        series=df[attrname[attrid - 1]]
        series=series.apply(pd.to_numeric, errors='coerce')
        fig=pd.DataFrame(series).boxplot().get_figure()
        fig.savefig('./pngs/boxplot_'+attrname[attrid -1]+'.png')
        fig.clear()


import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt

#读取数据
df=pd.read_csv('horse-colic.data_backup.txt',sep=' ')
df=df.drop(df.columns[[28]], axis=1)
df=df.apply(pd.to_numeric,errors='coerce')
attrname=['surgery','Age','Hospital_Number','rectal_temperature','pulse',
'respiratory_rate','temperature_of_extremities','peripheral_pulse',
'mucous_membranes','capillary_refill_time','pain','peristalsis',
'abdominal_distension','nasogastric_tube','nasogastric_reflux',
'nasogastric_reflux_PH','rectal_examination','abdomen','packed_cell_volume',
'total_protein','abdominocentesis_appearance','abdomcentesis_total_protein',
'outcome','surgical_lesion','#1_lesion','#2_lesion','#3_lesion','cp_data']
labelattr=[1,2,3,7,8,9,10,11,12,13,14,15,17,18,21,23,24,25,26,27,28]
valueattr=[4,5,6,16,19,20,22]

count_plot(df)

drop_any_df=df.dropna()


high_frequency_fillna_df=df.fillna(df.mode().iloc[0])


