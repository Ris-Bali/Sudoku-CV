#!/usr/bin/env python
# coding: utf-8

# In[2]:


import cv2 as cv
import numpy as np


# In[3]:


img = cv.imread('Sudokuog.jpg',1)
#cv.imshow("Sudoku",img)
#cv.waitKey(0)
#cv.destroyAllWindows()


# In[4]:


image = img.copy()


# In[5]:


image = cv.cvtColor(image,cv.COLOR_BGR2RGB)
gray = cv.cvtColor(image,cv.COLOR_RGB2GRAY)
thresh= cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_MEAN_C,            cv.THRESH_BINARY_INV,39,10)
#thresh1 = cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,\cv.THRESH_BINARY_INV,11,2)
#cv.imshow('Threshold1',thresh)
#cv.waitKey(0)
#cv.destroyAllWindows()


# In[6]:


contours,hierarchy = cv.findContours(thresh,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE)
max_area = 0
contour=contours[0]
for i in contours :
    if cv.contourArea(i)>max_area :
        contour=i
        max_area = cv.contourArea(i)


# In[10]:


blank_image = np.zeros(img.shape,dtype=np.uint8)
new_img = cv.drawContours(blank_image,[contour],-1,(255,255,255),2)
cv.imshow("new",new_img)
#cv.waitKey(0)
#cv.destroyAllWindows()


# In[12]:


edges = cv.Canny(new_img,40,150,apertureSize=3)
lines = cv.HoughLines(edges,1,np.pi/180,100)

