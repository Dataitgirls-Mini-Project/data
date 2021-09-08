#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
get_ipython().run_line_magic('config', "InlineBackend.figure_format = 'retina'")


# ### 폰트 설정

# In[2]:


import matplotlib.font_manager as fm

font_list = fm.findSystemFonts(fontpaths = None, fontext = 'ttf')

font_list[:]


# In[3]:


##설정 파일 위치
print (mpl.matplotlib_fname())


# In[4]:


print ('버전: ', mpl.__version__)
print ('설치 위치: ', mpl.__file__)
print ('설정 위치: ', mpl.get_configdir())
print ('캐시 위치: ', mpl.get_cachedir())


# In[5]:


font_list = fm.findSystemFonts(fontpaths=None, fontext='ttf')

# ttf 폰트 전체갯수
print(len(font_list)) 


# In[6]:


font_list[:10] 


# In[7]:


[(f.name, f.fname) for f in fm.fontManager.ttflist if 'Nanum' in f.name]


# In[8]:


path ='C:\\Windows\\Fonts\\나눔고딕.ttf'
fontprop = fm.FontProperties(fname=path, size=12)


# ### - 가설: '도움이 돼요'를 받은 리뷰는 전체 리뷰의 절반 이하일 것이다.
# 
# ### [결과물] 파이 차트 (시각화)
# 

# In[9]:


import pandas as pd
df = pd.read_csv('reviews_preprocessed.csv')
df.head()


# In[10]:


df["help"].value_counts()


# In[11]:


df.loc[(df.help != "0"), 'help'] = "1"


# In[12]:


df["help"].value_counts()


# In[13]:


t = df["help"].value_counts()


# In[14]:


x = t.index
y = t.values


# In[15]:


x


# In[16]:


y


# In[17]:


print(x)
print(y)


# In[18]:


plt.bar(x, y)
plt.title('도움이 돼요 유무별 리뷰 수', fontproperties=fontprop)
plt.xlabel('도움이 돼요 수', fontproperties=fontprop)
plt.ylabel('리뷰 수', fontproperties=fontprop)
plt.xticks(x, ["O개", "1개 이상"], fontproperties=fontprop)
plt.show()


# In[19]:


from matplotlib import font_manager, rc

font_name = font_manager.FontProperties(fname='C:\\Windows\\Fonts\\나눔고딕.ttf').get_name()
rc('font', family=font_name) #폰트 정하기(글자 깨짐 방지)
plt.figure(figsize=(7,7))
plt.title('도움이 돼요 유무별 리뷰수 비율', fontproperties=fontprop,
       fontsize = 13)
plt.pie(y, labels=["없음", "1개 이상"], autopct='%.1f%%', colors = ['#09ADDB','#C4B288'])
plt.legend(['없음', '1개 이상'], loc = 'lower right')
colors = ['red','yellow','purple','goldenrod','lightcoral']
plt.show()


# ### 가설4. '도움이 돼요' 를 받은 리뷰가 받지 않은 리뷰에 비해 평균 길이가 길 것이다.
# 
# ### [결과물] 막대 그래프 (시각화)

# In[20]:


def get_len(a) :
    return len(a)

df["len_review_cleaned"] = df["review_cleaned"].apply(get_len)


# In[21]:


df.head()


# In[22]:


df2 = pd.pivot_table(df, index = ['help'], values='len_review_cleaned', aggfunc = 'mean')
df2.head()


# In[23]:


print(df2.index)
print(df2['len_review_cleaned'].values)
x = df2.index
y = df2['len_review_cleaned'].values


# In[24]:


plt.bar(x, y, color = '#09ADDB')
plt.title('도움이 돼요 유무별 평균 리뷰 길이', fontproperties=fontprop)
plt.xlabel('도움이 돼요 수', fontproperties=fontprop)
plt.ylabel('평균 리뷰 길이', fontproperties=fontprop)
plt.xticks(x, ["O개", "1개 이상"], fontproperties=fontprop)
plt.show()


# ### 가설 5. 도움이돼요 1개 이상 리뷰 분석 

# In[25]:


import pandas as pd
help = pd.read_csv('reviews_preprocessed.csv')
help.head()


# In[26]:


help["help"].value_counts()


# In[27]:


help["help"].value_counts().index


# In[28]:


help["help"].unique()


# In[29]:


def help_clean (a):
    if "," in a:
        return a.replace(",","")
    return a
help["help"] = help["help"].apply(help_clean)


# In[30]:


help = help.astype({'help':'int'})


# In[31]:


# 이 리뷰 다시 확인해보기
help[help["help"] == 2128]


# In[32]:


help[help["user_name"] == "이한솔토마토"]


# In[33]:


help["help"].sum()


# In[34]:


help2 = help[help["help"] > 0]


# In[35]:


m = help2["help"].value_counts()
m


# In[36]:


x = m.index


# In[37]:


y = m.values


# In[38]:


print(x)
print(y)


# In[39]:


def help_pre(a):
    if a <= 5 :
        return "1개~5개"
    elif a> 5 and a <= 10:
        return "5~10개"
    else :
        return "10개 이상"
help2["help_pre"] = help2["help"].apply(help_pre)


# In[40]:


m = help2["help_pre"].value_counts()


# In[41]:


x = ['1개~5개','5~10개', '10개 이상']


# In[42]:


y = [1070,   58,   70]


# In[43]:


from matplotlib import font_manager, rc

font_name = font_manager.FontProperties(fname='C:\\Windows\\Fonts\\나눔고딕.ttf').get_name()
rc('font', family=font_name) #폰트 정하기(글자 깨짐 방지)
plt.figure(figsize=(7,7))
plt.title('도움이 돼요 수별 리뷰수 비율', fontproperties=fontprop,
       fontsize = 13)
plt.pie(y, labels=['1개~5개','5~10개', '10개 이상'], autopct='%.1f%%', colors = ['#09ADDB','#C4B288','#CFD0CD'])
plt.legend(['1개~5개','5~10개', '10개 이상'], loc = 'lower right')
plt.show()


# In[44]:


# 도움이 돼요 100개 이상 받은 리뷰들은 어떠어떠한(긍정 or 부정) 리뷰인지? - 10개


# In[45]:


df = help["help"].value_counts()
df = df.sort_index()
df = pd.to_numeric(df.index)
display(df)
bins = [-1,0,20,40,60,80,2128]
labels = ['0개','1~20','21-40','41-60','61~80','81개 이상']
cat = pd.cut(df.values,bins,labels=labels)
display(cat)


# In[46]:


len(help[help["help"] >= 100])


# In[47]:


help[help["help"] >= 100]


# #### 도움이 돼요 상위 10개 리뷰는 모두 리뷰 평점이 5.0! 즉 긍정적인 리뷰로 분류가 되었지만, 가장 많이 도움이돼요를 받은 리뷰의 실제 내용은 부정적인 리뷰였음을 확인했다.

# In[51]:


help_top_10 = help[help["help"] >= 100][['total_star','review_cleaned','help']]


# In[ ]:




