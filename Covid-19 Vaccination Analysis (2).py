#!/usr/bin/env python
# coding: utf-8

# # Let’s start by importing the necessary Python libraries and the dataset,

# In[3]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
data = pd.read_csv("C:\country_vaccinations.csv")
data.head()


# # Now let’s explore this data before we start analyzing the vaccines taken by countries, 

# In[4]:


data.describe()


# In[5]:


pd.to_datetime(data.date)
data.country.value_counts()


# In[6]:


data = data[data.country.apply(lambda x: x not in ["England", "Scotland", "Wales", "Northern Ireland"])]
data.country.value_counts()


# # Now let’s explore the vaccines available in this dataset,

# In[7]:


data.vaccines.value_counts()


# # Now I will create a new DataFrame by only selecting the vaccine and the country columns to explore which vaccine is taken by which country,

# In[8]:


df = data[["vaccines", "country"]]
df.head()


# # Now let’s see how many countries are taking each of the vaccines mentioned in this data,

# In[9]:


dict_ = {}
for i in df.vaccines.unique():
  dict_[i] = [df["country"][j] for j in df[df["vaccines"]==i].index]

vaccines = {}
for key, value in dict_.items():
  vaccines[key] = set(value)
for i, j in vaccines.items():
  print(f"{i}:>>{j}")


# # Now let’s visualize this data to have a look at what combination of vaccines every country is using,

# In[10]:


import plotly.express as px
import plotly.offline as py

vaccine_map = px.choropleth(data, locations = 'iso_code', color = 'vaccines')
vaccine_map.update_layout(height=300, margin={"r":0,"t":0,"l":0,"b":0})
vaccine_map.show()


# In[ ]:




