#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
x=pd.read_csv("HRDataset.csv")
x
from datetime import date




# In[2]:


x.isnull().sum()


# In[3]:


#date of termination


# In[4]:


x["DateofTermination"]=x["DateofTermination"].replace(to_replace=np.nan,value=0)


# In[5]:


x


# In[6]:


x.isnull().sum()


# In[7]:


x.loc[:,["ManagerName","Department","ManagerID"]]


# In[8]:


nvalue=x["ManagerID"].isnull()
x


# In[9]:


x.loc[x["ManagerName"]=="Webster Butler"]
x


# In[10]:


x["ManagerID"]=x["ManagerID"].replace(to_replace=np.nan,value=39.0)
x["ManagerID"]


# In[12]:


count_emp=x.groupby("Department")["Department"].count()
x


# In[13]:


#average salary
Avg_salary=x.groupby("Department")["Salary"].mean()
Avg_salary.round(2)


# In[32]:


#based on gender
Sex_Salary=x.groupby(["Department","Sex"],as_index=False).Salary.mean()
Sex_Salary


# In[33]:


#RECRUITMENT SOURCES
RecruitmentSource=x.groupby(["Department","RecruitmentSource"]).size().reset_index(name="counts")
RecruitmentSource


# In[20]:


Employee_Name=input("Enter the name:")


# In[14]:


Start_Year=int(input("Enter the Start year:"))
Start_Month=int(input("Enter the Start Month:"))
Start_Day=int(input("Enter the Start Day"))
Start_date=date(Start_Year,Start_Month,Start_Day)
Start_date


# In[17]:


T_Year = int(input("Enter the terminated year:"))
T_Month = int(input("Enter the terminated Month:"))
T_Days = int(input("Enter the terminated Day:"))
T_date = date(T_Year, T_Month, T_Days)
(T_date)


# In[18]:


business_days=pd.bdate_range(Start_date,T_date)
business_days


# In[21]:


print("Employee name:",Employee_Name,'working_days',len(business_days))


# In[ ]:




