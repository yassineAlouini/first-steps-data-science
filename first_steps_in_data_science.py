
# coding: utf-8

#  First steps in data science with Python 

# # Installation

# For new comers, I recommend using the Anacaonda distribution. You can download it from [here](https://www.continuum.io/downloads)

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

# This is a very important concept when doing data science

# # Example

# ## Import pacakges

# In[17]:

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

# In[9]:

sf_slaries_df = pd.read_csv('data/Salaries.csv')


# ## Data exploration

# In[11]:

sf_slaries_df.head()


# In[12]:

sf_slaries_df.tail()


# In[13]:

sf_slaries_df.columns


# In[14]:

sf_slaries_df.dtypes


# In[15]:

sf_slaries_df.describe()


# In[18]:

msno.matrix(sf_slaries_df)


# ## Some analysis

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
