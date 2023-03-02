#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
from datetime import datetime
from datetime import date
import seaborn as sns 
import matplotlib.pyplot as plt


# # Sheet 1: Transactions

# In[2]:


# Read data from sheet
df_transactions=pd.read_excel("C:/Users/RUCHITA/Documents/Downloads/KPMG_Python.xlsx", sheet_name ="Transactions")


# In[3]:


print(df_transactions.head())


# In[8]:


df_transactions.info()


# #### Using only required columns

# In[9]:


#Using only the required columns
df_transactions = df_transactions.iloc[:, 0:13]
df_transactions.info()


# In[10]:


df_transactions.info()


# ### Casting columns: 

# In[11]:


# Casting product_first_sold_date to date format.
df_transactions["product_first_sold_date"] = pd.to_datetime(df_transactions["product_first_sold_date"])

# Casting online_orde to str format.
df_transactions["online_order"]=df_transactions["online_order"].astype(str)


# In[12]:


df_transactions.info()


# #### Checking for null values

# 
# Few columns have the data type object, either because they contain values of different types or contain empty values (NaN).
# 
# It appears that few column contains some empty values since the Non-Null count for every column is lower than the total number of rows (20000). We'll need to deal with empty values and manually adjust the data type for each column on a case-by-case basis.
# 

# In[13]:


# Checking for null values
df_transactions.isnull().sum()


# In[14]:


# Finding percentage of missing data


# #### Checking for duplicate values

# In[15]:


# Checking for duplicate values
df_transactions[df_transactions.duplicated()].sum()


# #### check for uniqueness of each column

# In[16]:


#check for uniqueness of each column
df_transactions.nunique()


# #### Displaying value_counts for the columns

# In[17]:


# Brand Column values
df_transactions['brand'].value_counts()


# In[18]:


# profuct_line Column values
df_transactions['product_line'].value_counts()


# In[19]:


# product_class Column values
df_transactions['product_class'].value_counts()


# In[20]:


# product_size Column values
df_transactions['product_size'].value_counts()


# #### Let's now view some basic statistics about numeric columns.
# 

# In[21]:


df_transactions.describe()


# # Sheet 2: CustomerDemographic

# In[22]:


df_custDemo=pd.read_excel("C:/Users/RUCHITA/Documents/Downloads/KPMG_Python.xlsx", sheet_name ="CustomerDemographic")


# In[23]:


df_custDemo.info()


# In[24]:


df_custDemo.columns


# In[302]:


df_custDemo.head(5)


# #### Using only the required columns

# In[25]:


#Using only the required columns
# Discard Default column as it contains random data
a1=df_custDemo.iloc[:, 0:10]
b1=df_custDemo.iloc[:, 11:]
frames1 =[a1,b1]
df_custDemo= pd.concat(frames1, axis=1)
df_custDemo.info()


# In[26]:


df_custDemo["DOB"] = pd.to_datetime(df_custDemo["DOB"])

df_custDemo["age"] = df_custDemo["DOB"].apply(lambda x: (pd.datetime.now().year - x.year))
df_custDemo.sort_values(by='age', ascending=False).head(10)


# In[27]:


df_custDemo = df_custDemo[df_custDemo['age'] < 100]
df_custDemo.sort_values('age', ascending = False)


# #### Checking for null values

# In[28]:


# Checking for null values
df_custDemo.isnull().sum()


# #### Checking for duplicate values

# In[29]:


# Checking for duplicate values
df_custDemo[df_custDemo.duplicated()].sum()


# In[30]:


#check for uniqueness of each column
df_custDemo.nunique()


# #### Displaying value_counts for the columns

# In[31]:


# Brand Column values
df_custDemo['gender'].value_counts()


# In[32]:


# Replacing F and Femal with Female
df_custDemo['gender'] = df_custDemo['gender'].replace(['Femal', 'F'],'Female')
df_custDemo['gender'] = df_custDemo['gender'].replace(['M'],'Male')
df_custDemo['gender'] = df_custDemo['gender'].replace(['U'],'Undefined')
df_custDemo['gender'].value_counts()


# In[33]:


# job_industry_category Column values
df_custDemo['job_industry_category'].value_counts()


# In[34]:


# wealth_segment Column values
df_custDemo['wealth_segment'].value_counts()


# In[35]:


# deceased_indicator Column values
df_custDemo['deceased_indicator'].value_counts()


# In[36]:


# owns_car  Column values
df_custDemo['owns_car'].value_counts()


# #### Let's now view some basic statistics about numeric columns.
# 

# In[37]:


df_custDemo.describe()


# # Sheet 3: CustomerAddress

# In[38]:


df_custAddr=pd.read_excel("C:/Users/RUCHITA/Documents/Downloads/KPMG_Python.xlsx", sheet_name ="CustomerAddress")


# In[39]:


df_custAddr.columns


# In[40]:


df_custAddr.info()


# In[41]:


df_custAddr.columns


# In[42]:


df_custAddr.head(5)


# #### Checking for null values

# In[43]:


# Checking for null values
df_custAddr.isnull().sum()


# #### Checking for duplicate values

# In[44]:


# Checking for duplicate values
df_custAddr[df_custAddr.duplicated()].sum()


# #### check for uniqueness of each column

# In[45]:


#check for uniqueness of each column
df_custAddr.nunique()


# #### Displaying value_counts for the columns

# In[46]:


# state Column values
df_custAddr['state'].value_counts()


# In[47]:


# Replacing strings New south wales with NSW
df_custAddr['state'] = df_custAddr['state'].replace(['New South Wales'],'NSW')

# Replacing strings Victoria with VIC
df_custAddr['state'] = df_custAddr['state'].replace(['Victoria'],'VIC')

df_custAddr['state'].value_counts()


# In[48]:


# country Column values
df_custAddr['country'].value_counts()


# In[49]:


# Checking uniqness against the modifications made.
df_custAddr.nunique()


# #### Let's now view some basic statistics about numeric columns.
# 

# In[50]:


df_custAddr.describe()


# #### Find Columns Shared By Two Data Frames|

# In[51]:


#df_transactions.columns & df_custDemo.columns & df_custAddr.columns
df_transactions.columns.intersection(df_custDemo.columns)


# In[52]:


df_transactions.columns.intersection(df_custAddr.columns)


# In[53]:


df_custDemo.columns.intersection(df_custAddr.columns)


# #### Count Matching Values Between Columns

# In[54]:


# print("transactions:", df_transactions['customer_id'].value_counts().sum())
# print("custDemo", df_custDemo['customer_id'].value_counts().sum())
# print("custAddr", df_custAddr['customer_id'].value_counts().sum())

print("transactions:", df_transactions['customer_id'].nunique())
print("custDemo", df_custDemo['customer_id'].nunique())
print("custAddr", df_custAddr['customer_id'].nunique())



# In[55]:


t_u= df_transactions['customer_id'].unique()
print("unique transactions", t_u)

cd_u= df_custDemo['customer_id'].unique()
print("unique Customer Demo", cd_u)

ca_u= df_custAddr['customer_id'].unique()
print("unique Customer Addr", ca_u)


# In[56]:


def non_match_elements(list_a, list_b):
    non_match = []
    for i in list_a:
        if i not in list_b:
            non_match.append(i)
    return non_match
       
non_match = non_match_elements(t_u, cd_u)
print("t_u not in cd_u: \n", non_match)

non_match = non_match_elements(t_u, ca_u)
print("\n \n t_u not in ca_u: ", non_match)

non_match = non_match_elements(cd_u, ca_u)
print("\n \n cd_u not in ca_u: ", non_match)


# In[57]:


def non_match_elements(list_a, list_b, list_c):
    non_match = []
    for i in list_a:
        if i not in list_b: 
            if i not in list_c:
                non_match.append(i)
    return non_match
       
non_match = non_match_elements(t_u, cd_u, ca_u)
print("\n No records found in customer demo and customer address table : \n", non_match)


# In[ ]:





# In[58]:


df_transactions['customer_id'].isin(df_custAddr['customer_id']).value_counts()


# In[59]:


df_custDemo['customer_id'].isin(df_custAddr['customer_id']).value_counts()


# #### Display Matching Values Between Columns

# In[ ]:





# # Extra Sheet: NewCustomerList

# In[ ]:





# In[72]:


df_custList=pd.read_excel("C:/Users/RUCHITA/Documents/Downloads/KPMG_Python.xlsx", sheet_name ="NewCustomerList")


# In[73]:


df_custList.info()


# In[74]:


df_custList.columns


# In[133]:


#Using only the required columns
# Removing unnamed columns
b=df_custList.iloc[:,21:]
a=df_custList.iloc[:,0:16]
frames = [a,b]
df_custListM= pd.concat(frames, axis=1)
df_custListM.info()


# In[ ]:




