# -*- coding: utf-8 -*-
"""
Created on Tue Nov  9 14:18:06 2021

@author: R252202
"""

import numpy as np
import cv2
from PIL import ImageGrab
import os
import shutil
import pyautogui as pya
from time import sleep


def getScreenshot():
    img = ImageGrab.grab() #x, y, w, h
    img_np = np.array(img)
    return convertToGrey(img_np)

def convertToGrey(img):
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  

def findImageLocation09(scr, img):
    #GET WIDTH AND HEIGHT OF IMG
    w, h = img.shape[::-1]
    
    #MAGIC
    res = cv2.matchTemplate(scr, img, cv2.TM_CCOEFF_NORMED)
    threshold = 0.9
    loc = np.where(res >= threshold)
    co_x_y = ()
    
    for pt in zip(*loc[::-1]):
        cv2.rectangle(scr, pt, (pt[0] + w, pt[1] +h), (0, 0, 255), 2)
        co_x_y = pt
        
    return co_x_y, w, h

def click(loc, w ,h):
    pya.click(loc[0]+w/2, loc[1]+h/2)


def search():
    #LOAD IMAGE TO SERCH
    img_fav = cv2.imread("g:\\test.PNG")
    img_fav = convertToGrey(img_fav) #CONVERT IT TO GREYSCALE
    
    #GET SCR OF SCREEN
    scr = getScreenshot()
    
    #FIND LOCATION OF IMG
    location, w, h = findImageLocation09(scr, img_fav)
    
    #CLICK IT
    click(location, w, h)
    
sleep(0.5)
pya.press("enter")



