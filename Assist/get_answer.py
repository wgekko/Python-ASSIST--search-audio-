#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  5 22:02:19 2022

@author: walter
"""

import time
from selenium import webdriver
from selenium.webdirver.common.by import By
from selenium.webdirver.support.ui import WebDriveWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from bs4 import BeautifulSoup
from urllib.parse import urlparse
import sys


class Fetcher:
    def __init__(self, url):
        self.driver = webdriver.PhantomJS()
        self.driver.wait = WebDriverWait(self.driver, 5)
        self.url = url
        print(self.url)
        # self.lookup()
        
    def lookup(self):
        self.driver.get(self.url)
        try:
            ip = self.drive.wait.until(EC.presence_of_element_located(
                    (By.CLASS_NAME, "gsfi")
            ))
        
        except: 
            print("Failed Bro")
            
        soup = BeautifulSoup(self.driver.page_source, "html.parser" )
        answer = soup.find_all(class_="-sPg")
        #print(answer.get_text())
        with open("test.html", "w+") as f:
            f.write(soup)
            #f.close()
        
        if not answer:            
            answer = soup.find_all(class_="_m3b")
            
        if not answer:
            answer = "I don't Know..."
        
        self.driver.quit() 
        
        return answer[0].get_text()
       
        