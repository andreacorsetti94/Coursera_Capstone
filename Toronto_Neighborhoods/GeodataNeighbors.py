#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from WikipediaScraper import scrape_toronto_neighbors_from_wikipedia


# ## After having imported the WikipediaScraper module, we obtain the neighbors dataframe stored in Wikipedia

# In[2]:


wiki_neighbors_df = scrape_toronto_neighbors_from_wikipedia()


# In[3]:


wiki_neighbors_df.head()


# ## Now we import the latitude and longitude of each Neighborhood from a csv file

# In[4]:


geo_df = pd.read_csv("http://cocl.us/Geospatial_data")


# In[5]:


geo_df.head()


# ## Now we have to merge the two dataframes by the Postal code column

# In[9]:


final_df = pd.merge(wiki_neighbors_df, geo_df, left_on='Postal code', right_on='Postal Code')


# In[10]:


final_df.head()


# ## Drop the redundant column 'Postal Code'

# In[18]:


final_df.drop('Postal Code', axis=1, inplace = True)


# In[19]:


final_df.head()


# ## Now I create a function that groups these methods in order to be invoked by another .py module

# In[20]:


def obtain_and_merge_geo_data():
    wiki_neighbors_df = scrape_toronto_neighbors_from_wikipedia()
    geo_df = pd.read_csv("http://cocl.us/Geospatial_data")
    final_df = pd.merge(wiki_neighbors_df, geo_df, left_on='Postal code', right_on='Postal Code')
    final_df.drop('Postal Code', axis=1, inplace = True)
    return final_df


# In[21]:


obtain_and_merge_geo_data().head()

