#!/usr/bin/env python
# coding: utf-8

# In[5]:


import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd 
import os
print(os.listdir("../workspace"))


# In[14]:


data = pd.read_csv('../workspace/diabetes.csv')
data.info()


# In[15]:


data.describe()


# In[16]:


data.columns


# In[17]:


data.isnull().sum()


# In[18]:


print(data.Outcome.value_counts())
labels = '0', '1',
sizes = [500, 268]
colors = ['palegoldenrod','lightgrey']
explode = (0, 0)
fig1, ax1 = plt.subplots(figsize =(10,10))
ax1.pie(sizes,colors = colors ,explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')
plt.title("Outcome")
plt.show()


# In[19]:


data_columns = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin',
       'BMI', 'DiabetesPedigreeFunction', 'Age']
for each in data_columns:
    fig1, ax1 = plt.subplots(figsize =(10,10))
    plt.hist(data[each], bins=80,color = "cadetblue")
    plt.xlabel(each)
    plt.ylabel("Frequency")
    plt.grid()
    plt.show()


# In[20]:


df = pd.DataFrame(data,columns=data_columns)
f, ax = plt.subplots(figsize =(15,11))
corrMatrix = df.corr()
sns.heatmap(corrMatrix, annot=True)
plt.show()


# In[21]:


g = sns.jointplot(
    data=data,
    x="Glucose", y="Insulin", 
    kind="kde",
)
plt.show() 


# In[22]:


fig1, ax1 = plt.subplots(figsize =(10,10))
plt.scatter(data.index , data.Glucose,label =  "Glucose",alpha = 0.5,color = "orangered")
plt.scatter(data.index , data.Insulin,label =  "Insulin",alpha = 0.5,color = "darkblue")
plt.legend(loc ="best")
plt.xlabel("index")
plt.ylabel("Value")
plt.grid()
plt.show()


# In[23]:


g = sns.catplot(
    data=data, kind="bar",
    x="Outcome", y="Glucose",
    ci="sd", palette="dark", alpha=.6, height=6,
)
g.despine(left=True)
g.set_axis_labels("Outcome", "Glucose")
plt.grid()
plt.show()


# In[24]:


g = sns.catplot(
    data=data, kind="bar",
    x="Outcome", y="Insulin",
    ci="sd", palette="dark", alpha=.6, height=6,
)
g.despine(left=True)
g.set_axis_labels("Outcome", "Insluin")
plt.grid()
plt.show()


# In[25]:


sns.violinplot(data=data, x="Outcome", y="Glucose",
               split=True, inner="quart", linewidth=1,)
sns.despine(left=True)
plt.show()


# In[26]:


sns.violinplot(data=data, x="Outcome", y="Insulin",
               split=True, inner="quart", linewidth=1,)
sns.despine(left=True)
plt.show()


# In[ ]:




