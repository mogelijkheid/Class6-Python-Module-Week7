#!/usr/bin/env python
# coding: utf-8

# In[8]:


import json,csv

def json_maker(csvFP,jsonFP):
    
    data={}
    
    with open (csvFP) as csvf:
        csvReader = csv.DictReader(csvf)
        
        for lines in csvReader:
            key=lines['Company']
            data[key]=lines
            
    #print(data)
    with open (jsonFP,'w') as jsonf:
        json.dump(data,jsonf,indent = 4)

json_maker('data.csv','data.json')

                


# In[ ]:




