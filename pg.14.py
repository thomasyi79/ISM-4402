#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from sqlalchemy import create_engine

# Connect to sqlite db
db_file = r'datasets/salesdata.db'
engine = create_engine(r"sqlite:///{}".format(db_file))

sql = "select name from sqlite_master where type = 'table';"

sales_data_df = pd.read_sql(sql, engine)
sales_data_df.head()


# In[2]:


sql = "select * from scores;"
scores_df = pd.read_sql(sql, engine)
scores_df.head()


# In[ ]:




