#!/usr/bin/python
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
import pandas as pd
import numpy as np
import re
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import matplotlib.pyplot as plt
import seaborn as sns

binary = FirefoxBinary('/usr/bin/firefox-beta-bin')
driver = webdriver.Firefox(firefox_binary=binary)
driver.get("https://www.fifaindex.com/de/players/fifa19_1/")
#driver = webdriver.Chrome('C:\\Users\\Franz Bewerunge\\Desktop\\Ubiqum\\Study Data\\chromedriver.exe')
#driver.get("https://www.fifaindex.com/players/fifa08_1/")

players = pd.DataFrame()
limiter = True
while limiter:
    try:
        data_raw = pd.DataFrame()
        for j in range(1, 31):
            team = driver.find_elements_by_class_name('team')
            nationality = driver.find_elements_by_class_name('nation')

            for i in range(3, 7):
                data_chunk = driver.find_element_by_xpath('/html/body/main/div/div[2]/div[2]/div[2]/table/tbody/tr['+str(j)+']/td['+str(i)+']').text
                data_raw.loc[j,i] = data_chunk
            data_raw.loc[j, 8] = team[j-1].get_attribute('title')
            data_raw.loc[j, 9] = nationality[j-1].get_attribute('title')
        players = players.append(data_raw)


        #press on button to go to next page
        clicker = driver.find_element_by_link_text('Nächste Seite').send_keys(Keys.ENTER)
    except:
        limiter = False

