#!/usr/bin/env python
# coding: utf-8

# In[91]:


#Import Libraries
from bs4 import BeautifulSoup
from scrapy.crawler import CrawlerProcess
import requests
import scrapy


# In[25]:


#Read file
with open(r"C:\Users\pdoah\OneDrive\Desktop\aolhamilton.com_programs_.html", 'r') as html_file:
    content = html_file.read()
soup = BeautifulSoup(content, 'lxml')

#create class
class Edkosmos(scrapy.Spider):
    name = "edkosmos"
    
    def start_requests( self ):
        url = content
        yield scrapy.request( url = url, callback = self.parse_front)
        


# In[88]:


#Program Categories
categories = soup.find_all('ul', class_="nav nav-pills text-center w-auto m-auto")
for category in categories:
    Program_categories=category.text
    print(Program_categories)       


# In[90]:


tags = soup.find_all('div', class_="course-content")
for tag in tags:
        Prog_name = tag.h2.text
        Prog_duration = tag.span.text
        Prog_description = tag.p.text
        
        print(Prog_name)
        print(Prog_duration)
        print(Prog_description)


# In[69]:





# In[61]:


tags = soup.find_all('ul', class_="nav nav-pills text-center w-auto m-auto")
for tag in tags:
    Program_category = tag.text
    print(Program_category)


# In[60]:


features = soup.find_all('div', class_="course-content")
for feature in features:
    details=feature.text
    print(details)


# In[ ]:




