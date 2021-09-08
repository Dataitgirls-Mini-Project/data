#!/usr/bin/env python
# coding: utf-8

# In[2]:


import os


# In[3]:


os.getcwd()


# In[4]:


import sys
print(sys.version)


# In[5]:


os.chdir("C:/Users/user/Areumpy/Mini Project")
get_ipython().system('pip install JPype1-1.1.2-cp38-cp38-win_amd64.whl')


# In[6]:


get_ipython().system('pip install konlpy')


# In[7]:


import konlpy


# In[11]:


from konlpy.tag import Komoran

komoran = Komoran()
print(komoran.nouns("게시글이 좋았다면 공감을 눌러주세요!!!"))


# In[ ]:




