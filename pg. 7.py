#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
Location = "Downloads/floridaTotalPop.csv"
df = pd.read_csv(Location, names=['Name','POP100.2000'])
df.columns = ['Name','POP100.2000']


# In[ ]:




