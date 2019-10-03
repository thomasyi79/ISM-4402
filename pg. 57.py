#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd

names = ['Bob','Jessica','Mary','John','Mel']
grades = [76,95,77,78,99]
bsdegrees = [1,1,0,0,1]
msdegrees = [2,1,0,0,0]
phddegrees = [0,1,0,0,0]


# In[6]:


GradeList = zip(names,grades,bsdegrees,msdegrees,phddegrees)
df = pd.DataFrame(data = GradeList, columns=['Names','Grades','BS','MS','PhD'])
df


# In[7]:


df.count()


# In[8]:


df.std()


# In[9]:


df.min()


# In[10]:


df.max()


# In[11]:


df.quantile(.25)


# In[12]:


df.quantile(.5)


# In[14]:


df.quantile(.75)

