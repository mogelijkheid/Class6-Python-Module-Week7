#!/usr/bin/env python
# coding: utf-8

# In[49]:


import csv

with open('users.csv', 'w', newline='') as file:
    fieldnames = ['firstname', 'surname']
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'firstname': 'jan', 'surname': 'oranje'})
    writer.writerow({'firstname': 'tiny', 'surname': 'gomez'})
    


# In[50]:


def print_names():
    with open('users.csv') as file:
        reader = csv.DictReader(file)
        for i in reader:
            print("{} {}".format(i['firstname'], i['surname']))


# In[57]:


def add_name():
    with open('users.csv', 'a') as file:
        fieldnames = ['firstname','surname']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        first = input("First ")
        last = input("Last ")
        writer = csv.DictWriter(file, fieldnames)
        writer.writerow(dict(firstname=first, surname=last))


# In[ ]:




