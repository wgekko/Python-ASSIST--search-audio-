#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  5 21:20:43 2022

@author: walter
"""

import subprocess
import os
import requests
from bs4 import BeautifulSoup
from get_answer import Fetcher


class Commander:
    
    def __init__(self):
        self.confirm = ["yes", "affirmative", "si", "sure", "do it", "yeah", "confirm"]
        self.cancel = ["no", "negative", "negative soldier", "don't", "wait", "cancel"]
    
    def discover(self, text):
        if "what" in text and "your name" in text:
            if "my" in text:
                self.respond("you haven told me your name yet ")
              
            else: 
                self.respond("My name is python commander ... Hoy are you ??")
                
        else:
            
            f = Fetcher("https://wwww.google.com/search?q="+ text)
            answer = f.lookup()
            self.respond(answer)
            
#        if "launch" or "open" in text:
#            # se busca dar  la instruccio de abrir por ejemplo diciendo "opening firefox"
#            app = text.split("  ", 1) [-1]
#            self.respond("Opening" + app)
#            
#            os.system("open -a "+ app + " app")
   
    def respond(self, response):
        print(response)
        subprocess.call("say " + response, shell = True)
        