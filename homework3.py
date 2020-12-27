#!/usr/bin/env python
# coding: utf-8

# In[24]:


#homework3
import time
import random


# In[25]:


name=input("What is your name? ")
print("Hello "+name," Good Luck! ")


# In[26]:


print("Start guessing..")


# In[38]:


words = ['rainbow', 'computer', 'science', 'programming', 
         'python', 'mathematics', 'player', 'condition', 
         'reverse', 'water', 'board', 'geeks'] 
word=random.choice(words)

turns=len(word)+1


# In[40]:


guesses = []
while turns>0:
    failed=0
    for char in word:
        if char in guesses:
            print(char)
        else:
            print("_")
            failed+=1
    if failed==0:
        print("You win!")
        print("The word is:",word)
        break
    guess=input("Guess a charakter:")
    guasses.append(guess)
    if guess not in word:
        turns-=1
        print("wrong!")
        print("You have",+turns,"more guesses")
        if turns ==0:
            print("You Lose")


# In[ ]:




