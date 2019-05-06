#!/usr/bin/env python
# coding: utf-8

# In[36]:


import pandas as pd
from splinter import Browser
import requests
from bs4 import BeautifulSoup 
#from selenium import webdriver


# In[37]:


executable_path = {'executable_path': 'chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=False)


# In[38]:


url = "https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&c"
browser.visit(url)


# In[39]:


response = requests.get(url)
soup = BeautifulSoup(response.text,'html.parser')


# In[76]:


#find title

executable_path = {'executable_path': 'chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=False)
url = "https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&c"
browser.visit(url)
soup = BeautifulSoup(browser.html,'html.parser')


n_title= soup.find("div", class_="content_title").text.replace("\n", "")

print(n_title)


# In[52]:


#find paragraph text
executable_path = {'executable_path': 'chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=False)
url = "https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&c"
soup = BeautifulSoup(response.text,'html.parser')
news_par=soup.find("div", class_="rollover_description_inner").text
print(news_par)


# In[ ]:


#jpl mars space images

executable_path = {"executable_path": "chromedriver.exe"}
browser = Browser("chrome", **executable_path, headless=False)
url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
soup = BeautifulSoup(browser.html,'html.parser')
featured_image = soup.find("a", class_="fancybox-nav fancybox-prev")["javascript-href"]
featured_image_url = "https://www.jpl.nasa.gov"+ featured_image
print(featured_image_url)


# In[63]:


##mars weather
executable_path = {"executable_path": "chromedriver.exe"}
browser = Browser("chrome", **executable_path, headless=False)
url = "https://twitter.com/marswxreport?lang=en" 
browser.visit(url)
soup = BeautifulSoup(browser.html,'html.parser')
    
    
tw_text=soup.find("div",class_="js-tweet-text-container").find("p").text
mars_weather="".join(tw_text.split("pic")[0].split("InSight")[1].split("\n"))
print(mars_weather)                     


# In[70]:


##mars facts
executable_path = {"executable_path": "chromedriver.exe"}
browser = Browser("chrome", **executable_path, headless=False)
url = "https://space-facts.com/mars/" 
browser.visit(url)
soup = BeautifulSoup(browser.html,'html.parser')

mars_df=pd.read_html(url)[0]
mars_df=mars_df.rename(columns={1 :''})
mars_df=mars_df.set_index(0)
mars_html=mars_df.to_html(classes='table table-striped')
print(mars_html)


# In[ ]:


##mars hempispheres
executable_path = {"executable_path": "chromedriver.exe"}
browser = Browser("chrome", **executable_path, headless=False)
url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars" 
browser.visit(url)
soup = BeautifulSoup(browser.html,'html.parser')


hemi_img_urls=[]

for hemi in links:
    links= soup.find_all("div", class_="description")[x]
    h_name=links.find("h3").text
    h_img=links.find("a")["href"]
    h_img_url=f""https://astrogeology.usgs.gov/" + h_img

executable_path = {"executable_path": "chromedriver.exe"}
browser = Browser("chrome", **executable_path, headless=False)
soup = BeautifulSoup(browser.html,'html.parser')

h_res_img=soup.find("img", class_="wide-image")["src"]
h_res_img_url=f""https://astrogeology.usgs.gov" + h_res_img

h_dict={"title", h_name,"img_url":h_res_img_url}
hemi_img_urls.append(h_dict)

print(hemi_img_urls)

