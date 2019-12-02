#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
Location = "datasets/axisdata.csv"
df = pd.read_csv(Location)
df.head()


# In[11]:


df['Cars Sold'].mean()


# In[12]:


df['Cars Sold'].max()


# In[13]:


df['Cars Sold'].min()


# In[7]:


pd.pivot_table(df, values=['Cars Sold'], index=['Gender'])


# In[19]:


df[df['Cars Sold']>3]['Hours Worked'].mean()


# In[15]:


df['Years Experience'].mean()


# In[16]:


df[df['Cars Sold']>3]['Years Experience'].mean()


# In[4]:


pd.pivot_table(df, values=['Cars Sold'], index=['SalesTraining'])


# In[5]:


pd.pivot_table(df, values=['Years Experience'], index=['Gender'])


# In[7]:


pd.pivot_table(df, values=['Hours Worked'], index=['Gender'])

