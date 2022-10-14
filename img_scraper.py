import requests
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
import time
import urllib.request
import pandas as pd
driver = webdriver.Chrome('E:\\chromedriver\\chromedriver_win32 (1)\\chromedriver.exe')
master_list=[]
url="https://www.pexels.com/search/4k%20wallpaper/"
driver.get(url)
for i in range(10):
   driver.find_element_by_tag_name('body').send_keys(Keys.END)
   time.sleep(3)
html=driver.page_source
soup=BeautifulSoup(html,"html.parser")
content=soup.find_all("div",{"class":"ButtonGroup_buttons__kI2YT"})
i=1
for c in content:
    data_dict={}
    data_dict['image_link']=c.find("a",{"class":"ButtonGroup_buttonOverrides__NuhSe Button_button__L4pRn Button_white__snM9f MediaCard_hideWhenNotHovered__eYqDp ButtonGroup_downloadButton__M_vvd"})["href"]
    master_list.append(data_dict)
pexel_df=pd.DataFrame(master_list)
pexel_df.to_excel('pexel.xlsx',index=False)
i=1
for r in master_list:
    for value in r.values():
        image=requests.get(value)
        image_title=str(i)+".jpeg"
        with open(image_title,'wb') as file:
            file.write(image.content)
        i=i+1