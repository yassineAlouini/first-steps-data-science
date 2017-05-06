
# coding: utf-8

#  First steps in data science with Python 

# # Installation

# For new comers, I recommend using the Anacaonda distribution. You can download it from [here](https://www.continuum.io/downloads).
# 
# If you are familiar with Python, create a `conda` environment and install the need libraries (using the `environment.yml` file): 
# 
# `conda env create -f environment.yml`
# 
# Then, activate the environement using: 
# 
# `conda activate worshop`

# # The Python data science ecosystem

# ## Jupyter notebook

# [Jupyter](https://jupyter.org/) notebook is the code environment we will be using today. <br>
# Previously known as ipython notebook, it is an interactive environment that makes prototyping easier for data scientists.

# ## Pandas

# [Pandas](http://pandas.pydata.org/) is the primary toolbox used for collecting and cleaning datasets from various data sources. <br>
# Most of the concepts that we are exploring today can be found in the following great [cheatsheet](https://github.com/pandas-dev/pandas/blob/master/doc/cheatsheet/Pandas_Cheat_Sheet.pdf)

# ## Matplotlib

# [Matplotlib](http://matplotlib.org/) is the standard and de facto Python library for creating visualizations.

# ## Numerical and statistical (numpy, scipy, statsmodels)

# Alongside the above tools, Python offers a set of numerical and statistical packages to perform data analysis. 
# The most famous ones are: 
# 
# * [numpy](http://www.numpy.org/): Base N-dimensional array package
# * [scipy](https://www.scipy.org/scipylib/index.html): Fundamental library for scientific computing
# * [statsmodels](http://www.statsmodels.org/stable/): Statistical computations and models for Python

# Keep in mind that most of the capabilites of the above package are integrated within the Pandas library.

# # Tidy data

# This is a very important concept when doing data science. To demonstrate how important it is, let's start by creating a messy one and tidying it.

# In[9]:

import pandas as pd
messy_df = pd.DataFrame({'2016': [1000, 2000, 3000], 
                         '2017': [1200, 1300, 4000], 
                         'company': ['slack', 'twitter', 'twitch']})


# Here, we have created a fictional dataset that contains earnings for years 2016 and 2017

# In[10]:

messy_df


# You might ask, what is the problem with this dataset? <br>
# There are two main ones:
# 
# * The coloumns 2016 and 2017 contain the same type of variable (earnings)
# * The columns 2016 and 2017 contain an information about the year 

# Now that we have a "messy" dataset, let's clean it.

# In[24]:

tidy_df = pd.melt(messy_df, id_vars=['company'],value_name='earnings', var_name='year')


# In[25]:

tidy_df


# That's much better! <br>

# In summary, a tidy dataset has the following properties: 
#     
# * Each column represents only one **variable**
# * Each row represents an **observation**

# # Example

# ## Import pacakges

# In[28]:

get_ipython().magic('matplotlib inline')
import pandas as pd
import numpy as np
import matplotlib.pylab as plt
import missingno as msno


# ## Loading data

# [Kaggle](https://www.kaggle.com/) offers many free datasets with lots of metadata, descriptions, kernels, discussions and so on. <br>
# Today, we will be working with the San Francisco Salaries dataset. You can download it from [here](https://www.kaggle.com/kaggle/sf-salaries) (you need a Kaggle account) or get it from the workshop [repository](https://github.com/yassineAlouini/first-steps-data-science/blob/master/data/Salaries.csv).

# The dataset we will be working with is a CSV file. Fortunately for us, Pandas has a handy method `.read_csv`.
# Let's try it out!

# In[29]:

sf_slaries_df = pd.read_csv('data/Salaries.csv')


# ## Data exploration

# In[30]:

sf_slaries_df.head()


# In[31]:

sf_slaries_df.tail()


# In[32]:

sf_slaries_df.columns


# In[33]:

sf_slaries_df.dtypes


# In[34]:

sf_slaries_df.describe()


# In[35]:

msno.matrix(sf_slaries_df)


# ## Some analysis

# ### What are the different job titles? How many?

# In[42]:

sf_slaries_df.JobTitle.value_counts()


# In[44]:

sf_slaries_df.JobTitle.nunique()


# ## Higher and lowest salaries per year? Which jobs?

# In[62]:

sf_slaries_df.groupby('Year').TotalPay.agg(['min', 'max'])


# In[67]:

lowest_idx = sf_slaries_df.groupby('Year').apply(lambda df: df.TotalPay.argmin())


# In[74]:

sf_slaries_df.loc[lowest_idx, ['Year', 'JobTitle']]


# In[71]:

highest_idx = sf_slaries_df.groupby('Year').apply(lambda df: df.TotalPay.argmax())


# In[73]:

sf_slaries_df.loc[highest_idx, ['Year', 'JobTitle']]


# # To wrap up

# In todays's workshop, you have learned: 
# 
# * About the Python data science ecosystem (some of its parts at least)
# * The concept of a tidy dataset
# * How to load a dataset using Pandas
# * How to explore a dataset
# * How to make simple plots
# 
# I hope this was insightful! <br>
# See you at a next workshop hopefully.

# # References/ To go beyond

# I hope you have enjoyed this workshop. To continue learning, I recommend the following:
#     
# * A blog post on how to become a data scientist: https://www.dataquest.io/blog/how-to-become-a-data-scientist/ 
# * Consider trying [dataquest](https://www.dataquest.io) and/or [datacamp](https://www.datacamp.com/) if you want to learn more about data science using Python. Notice that they both offer some free content but most of it is available for a monthly subscription
# * [Quora](https://www.quora.com/): one of the best places to ask and answer questions about data science (and any other subject more generally)
# * [Kaggle](https://www.kaggle.com/): this is a great place to hone your data science skills through producing and reading different kernels (these are their internal variation of notebooks)
# * More generally follow great data scientists. Some that I really enjoy reading their work (in no particular order): 
#     * [Wes Mckinney](http://wesmckinney.com/): original creator of Pandas.
#     * [Tom Augspurger](https://tomaugspurger.github.io/): core contributor of Pandas. Has written the [modern Pandas](https://tomaugspurger.github.io/modern-1.html) blog posts series (a most read).
#     * [Jake VanderPlas](http://staff.washington.edu/jakevdp/): a data scientist in academia (as he defines himself).
