#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


US_CPI=pd.read_csv('/Users/erinliang/Desktop/599/US_CPI.csv')
##display(US_CPI)

#stack years and months
US_CPI = pd.melt(US_CPI, id_vars=['YEAR'], var_name=['Month'])
US_CPI['date'] = pd.to_datetime(US_CPI['YEAR'].astype(str) + '-' + US_CPI['Month'].astype(str))
US_CPI = US_CPI.sort_values(by=['date']).drop(columns=['Month', 'YEAR']).reset_index(drop=['index'])
US_CPI = US_CPI.rename(columns={'value': 'US_CPI'})
##display(US_CPI)


# In[3]:


indices=pd.read_csv('/Users/erinliang/Desktop/599/599_data.csv')

#merge US CPI data and Indices return data into one dataframe
data = pd.concat([US_CPI, indices], axis = 1)

#drop column 
data = data.drop('Date', 1)
##display(data)


# In[4]:


#isolate inflation periods 
data = data[data.US_CPI > 0.035]
##pd.set_option('display.max_rows',700)
display(data)


# In[ ]:




