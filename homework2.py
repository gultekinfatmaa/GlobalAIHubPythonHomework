#!/usr/bin/env python
# coding: utf-8

# In[1]:


users=input("user name:")


# In[3]:


users_lastname=input("user lastname:")


# In[4]:


users_age=int(input("user age: "))


# In[8]:


users_birth=int(input("user date of birth: "))


# In[17]:


print("user name:"+users+"\nuser lastname:"+users_lastname+"\nuser age:"+str(users_age)+"\nuser data of birth:"+str(users_birth))
if(users_age<18):
    print("You can't go out because it's too dangerous")
else:
    print("You can go out to te street")

