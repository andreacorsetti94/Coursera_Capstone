#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# ## Read Postal Codes Table from Wikipidia Website's html

# In[4]:


df_list = pd.read_html("https://en.wikipedia.org/wiki/List_of_postal_codes_of_Canada:_M")
df = df_list[0] #[0] since it's the first <table> of the page
df.head()


# ## Dropping the rows where 'Borough' is not assigned

# In[33]:


df.drop(df[df["Borough"] == "Not assigned"].index, inplace = True)


# ## Replacing the separator of the column 'Neighborhoods' from '/' to ','

# In[34]:


df['Neighborhood'] = df['Neighborhood'].str.replace(' /', ',', regex=True)


# ## I define a function that is going to be used by the notebooks that will import this module

# In[37]:


def scrape_toronto_neighbors_from_wikipedia():
    df_list = pd.read_html("https://en.wikipedia.org/wiki/List_of_postal_codes_of_Canada:_M")
    df = df_list[0]
    df.drop(df[df["Borough"] == "Not assigned"].index, inplace = True)
    df['Neighborhood'] = df['Neighborhood'].str.replace(' /', ',', regex=True)
    return df


# In[39]:


df = scrape_toronto_neighbors_from_wikipedia()


# In[40]:


df.head()


# In[41]:


df.shape

