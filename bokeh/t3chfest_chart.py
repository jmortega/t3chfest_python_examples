import pandas as pd

import json

from bokeh.charts import *

import numpy as np

df = pd.read_csv('t3chfest.csv')

count_c=0
count_java=0
count_python=0
count_javascript=0

for index in df.values.tolist():
    if 'C++' in index[1]:
        count_c = count_c +1
    if 'Java' in index[1]:
        count_java = count_java +1
    if 'Python' in index[1]:
        count_python = count_python +1
    if 'Script' in index[1] or 'Javascript' in index[1]:
        count_javascript = count_javascript +1  
 

dataFrame= pd.DataFrame({'Languages':['Java','Python','C++','JavaScript'],
                         'Count':[count_java,count_python,count_c,count_javascript]})


bar_chart= Bar(dataFrame,label='Languages',values='Count',group='Languages',
               legend='top_right')

output_file(filename="t3chfest_chart.html")

show(bar_chart)



