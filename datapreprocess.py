import pandas as pd
import numpy as np
import scipy.stats as stats
import pylab

#读取数据
df=pd.read_csv('horse-colic.data.txt',sep=' ')
attrname=['surgery','Age','Hospital_Number','rectal_temperature','pulse','respiratory_rate','temperature_of_extremities','peripheral_pulse','mucous_membranes','capillary_refill_time','pain','peristalsis','abdominal_distension','nasogastric_tube','nasogastric_reflux','nasogastric_reflux_PH','rectal_examination','abdomen','packed_cell_volume','total_protein','abdominocentesis_appearance','abdomcentesis_total_protein','outcome','surgical_lesion','#1_lesion','#2_lesion','#3_lesion','cp_data']
labelattr=[1,2,3,7,8,9,10,11,12,13,14,15,17,18,21,23,24,25,26,27,28]
valueattr=[4,5,6,16,19,20,22]

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


for attrid in valueattr:
    print(attrname[attrid - 1])
    series=df[attrname[attrid - 1]]
    series=series[series != '?'].apply(pd.to_numeric, errors='coerce')
    series.hist()

for attrid in valueattr:
    print(attrname[attrid - 1])
    series=df[attrname[attrid - 1]]
    series=series[series != '?'].apply(pd.to_numeric, errors='coerce')
    _=stats.probplot(series, dist="norm", plot=pylab)


for attrid in valueattr:
    print(attrname[attrid - 1])
    series=df[attrname[attrid - 1]]
    series=series[series != '?'].apply(pd.to_numeric, errors='coerce')
    _=pd.DataFrame(series).boxplot()
    
