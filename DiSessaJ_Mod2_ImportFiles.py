#!/usr/bin/env python
# coding: utf-8

# # Module 2 Assignnment
# 
# ALY6140_Module2_ImportFiles
# 
# Copyright (c) January 20, 2023
# 
# Licensed
# 
# Written by John DiSessa
#     
# 

# In[1]:


#Import necessary libraries
import pandas as pd
import numpy as np
import os
import json


# In[21]:


os.chdir(r'C:\Users\johnd\Desktop\Northeastern\IntroPython')


# In[17]:


#Import CSV

#Trying to use an absolute path but all options I tried failed

#csv_file = '''C:\\Users\\johnd\\Desktop\\Northeastern\\IntroPython\\Neural_data.csv'''
#df_from_csv = pd.read_csv(csv_file)
#df_from_csv.info()

#df = pd.read_csv(""C:\\Users\\johnd\\Desktop\\Neural_data.csv"")

#def readCSV(fileName):
#    """
#    Read data from a CSV file
#    : param fileName: CSV file name
#    : return a CSV dataframe
#    """
#    data_frame = pd.read_csv(fileName)
#    return data_frame

#readCSV("Neural_dataset.csv")

os.getcwd()


# In[3]:


# Import CSV #

def import_csv (csv_file):
    df_from_csv = pd.read_csv(csv_file)
    df_from_csv.info()
    result = df_from_csv
    return result
    
import_csv('Neural_data.csv')


# In[5]:


#Import TXT

def import_txt(txt_file):

    results = []
    with open(txt_file) as f:
        line = f.readline()
        while line:
            results.append(line.strip().split(" "))
            line = f.readline()
    f.close()
    df_from_txtfile = pd.DataFrame(results)
    df_from_txtfile.info()
    result = df_from_txtfile
    return result

import_txt('network_data.txt')


# In[13]:


#Import JSON
#keeping as JSON object


f = open ('nested_data.json', "r")
  
# Reading from file
data = json.loads(f.read())
data[0]


# In[10]:


#Import JSON
#Turning into Data Frame

def import_json(json_file):
    df_json = pd.read_json(json_file)
    df_json.info()
    result = df_json.head()
    return result

import_json('nested_data.json')


# In[12]:


#Import XLSX

def import_excel(excel_file):
    df_from_excel = pd.read_excel(excel_file, index_col = 0, header = 2, usecols = "C:R",sheet_name="Sheet000") #sheet_name can be specified too
    df_from_excel.info()
    result = df_from_excel.head()
    return result


import_excel('Excel_report.xlsx')


# In[4]:





# In[ ]:




