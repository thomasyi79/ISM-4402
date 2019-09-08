#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
Location = "Downloads/wholesaleTrade.csv"
df = pd.read_csv(Location, names=['Areaname','STCOU'])
df.columns = ['Areaname','STCOU']


# In[ ]:




