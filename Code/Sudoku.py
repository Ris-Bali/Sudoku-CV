#!/usr/bin/env python
# coding: utf-8

# In[14]:


import numpy as np


# In[15]:


skeleton = np.zeros((9,9),dtype=np.int64)             


# In[16]:


print(skeleton)


# In[17]:


skeleton[0,1]=1
skeleton[0,2]=9
skeleton[0,3]=3
skeleton[0,5]=6
skeleton[0,6]=8
skeleton[0,8]=5
skeleton[1,4]=8
skeleton[1,5]=2
skeleton[2,6]=4
skeleton[2,7]=9
skeleton[3,1]=3
skeleton[3,2]=4
skeleton[3,6]=1
skeleton[4,0]=1
skeleton[4,2]=5
skeleton[5,1]=9
skeleton[5,3]=4
skeleton[5,4]=3
skeleton[5,7]=6
skeleton[6,0]=3
skeleton[6,1]=6
skeleton[6,2]=1
skeleton[6,4]=5
skeleton[7,4]=1
skeleton[7,6]=3
skeleton[8,0]=4
skeleton[8,3]=2
skeleton[8,8]=9


# In[18]:


skeleton


# In[19]:


def return_empty(board):
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j]==0:
                return (i,j) 
    return None  


# In[20]:


#Function to check validity of the number (wiill return False if number exists in box,row or column and True othervise)
#Inputs are number entered to fill blank , the board,the position in which number is entered)
def check(num,board,pos):
    #Check the row
    for i in range(len(board)):
        if board[pos[0]][i] ==num and i!=pos[1] :
            return False
    for j in range(len(board)):
        if board[j][pos[1]]==num and j!=pos[0] :
            return False
    box_hori=pos[1]//3
    box_ver=pos[0]//3
    for i in range (box_ver*3,box_ver*3+3) :
        for j in range(box_hori*3,box_hori*3+3):
            if board[i][j]==num and pos!=(i,j):
                return False
    return True        
        


# In[ ]:





# In[25]:


#Recursive Algorithm to solve the sudoku consider some numbers that do not work and then backtrack only then will this algorithm make sense to u 

def Algo(board):
    find = return_empty(board)
    if not find :
        return True 
    else :
        row,column = find[0],find[1]
    for i in range(1,10):
        if check(i,board,(row,column)):
            board[row][column]=i
            if Algo(board):
                return True
        board[row][column]=0
    return False   
        
        
    


# In[26]:



def structure(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")


# In[27]:


structure(skeleton)


# In[28]:


Algo(skeleton)


# In[29]:


structure(skeleton)


# In[ ]:




