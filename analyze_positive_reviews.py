import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re
import urllib.request
import nltk
import konlpy
from PyKomoran import *
from konlpy.tag import Okt
from collections import Counter
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 
from wordcloud import WordCloud
from wordcloud import ImageColorGenerator
from PIL import Image



df = pd.read_csv('reviews_preprocessed.csv')

# 긍정적인 리뷰만 불러오기
df = df[df['sentiment'] == 1]

# 말뭉치
pos_corpus = ' '.join(df['review_cleaned'].tolist())
pos_corpus

okt=Okt() 

#품사 별로 나눠주기 
posi_pos = okt.pos(pos_corpus, stem = True)

# 명사
noun_list = []

for item in posi_pos:
    
    w = item[0] #단어
    c = item[1] #품사

    if c == 'Noun' and len(w) > 1:
        noun_list.append(w)

# noun_list
# len(noun_list)

count_noun = Counter(noun_list)
noun_most= count_noun.most_common()
# noun_most
# len(noun_most)

noun_stop_words = ['쿠션','부분','의자','우리','저희','저기','이제','대신','오늘','신하','무엇','약간','바로','생각','진짜','정말','하나','조금','아주','완전','보고','그냥','여기','정도','살짝','일단','계속','매우','다른','지금','색도','듭니','제일']

#불용어 제거한 리스트
noun_most_list = []

for sent in noun_list:
    if sent not in noun_stop_words:
        noun_most_list.append(sent)

count_noun_most = Counter(noun_most_list)
cnmc = count_noun_most.most_common()
# cnmc

cnmc.insert(6,('리뷰', 443))
del cnmc[20]
del cnmc[32]
cnmc[12] = ('가성비',327)
# cnmc

cut_cnmc = cnmc[:51]
dic_cnmc = dict(cut_cnmc)

mask_image = Image.open('C:/Users/user/Areumpy/Mini Project/house_1.png')
mask = np.array(mask_image)


dic_cnmc_ = dic_cnmc
dic_cnmc_save = pd.DataFrame(dic_cnmc_, index = [0])
dic_cnmc_save.to_csv("dic_cnmc_210828.csv", mode = 'w', encoding = 'utf-8-sig')

wordcloud = WordCloud(font_path='C:/Windows/Fonts/잘풀리는오늘 Medium.ttf',
                      background_color = 'white', 
                      colormap = "cool",
                      # colormap = "viridis", 
                      mask = mask 
                      #height = mask.shape[0],
                      #width = mask.shape[1] 
                     )
cloud = wordcloud.generate_from_frequencies(dic_cnmc)                      
plt.figure(figsize = (40 , 35))  
plt.imshow(cloud, interpolation="bilinear")
plt.axis('off')
# plt.show()
plt.savefig('긍정리뷰_명사_워드클라우드.png')


# In[28]:


# 막대 그래프 글자 깨짐 해결

from matplotlib import font_manager, rc
import platform

if platform.system() == 'Windows':
# 윈도우인 경우
    font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
    rc('font', family=font_name)


# In[45]:


y = np.arange(10)

items = ['느낌', '조절', '받침', '리뷰','디자인', '구매','사용','가격', '배송', '조립']
values = [396, 409,432,443, 524, 710, 710, 832, 1194, 1546]

plt.barh(y, values, color = 'skyblue')
plt.yticks(y, items)

plt.title('긍정적인 리뷰에서 빈출 명사 top10', fontsize = 13)
plt.xlabel('빈출수', fontsize = 12)

#plt.show()

plt.savefig('긍정리뷰_명사_top10 막대그래프.png', dpi=300)


# # 형용사

# In[5]:


okt=Okt() 

#품사 별로 나눠주기 
posi_pos = okt.pos(pos_corpus, stem = True)

adj_list = []

for item in posi_pos:
    
    w = item[0] #단어
    c = item[1] #품사

    if c == 'Adjective' and len(w) > 1:
        adj_list.append(w)

# adj_list
# len(adj_list)

count_adj = Counter(adj_list)
adj_most= count_adj.most_common()
adj_most
adj_stop_words = ['있다','같다','이다','없다','아니다','그렇다','야하다','어떻다'] 
adj_most_list = []

for sent in adj_list:
    if sent not in adj_stop_words:
        adj_most_list.append(sent)

count_adj_most = Counter(adj_most_list)
camc = count_adj_most.most_common()
# camc

camc.insert(0,('편하다', 5314))
camc.insert(2,('예쁘다', 1582))
camc.insert(7,('빠르다', 676))
del camc[1]
del camc[3]
del camc[6]
del camc[16]
# camc

cut_camc = camc[:51]
dic_camc = dict(cut_camc)

mask_image = Image.open('C:/Users/user/Areumpy/Mini Project/house_1.png')
mask = np.array(mask_image)

dic_camc_ = dic_camc
dic_camc_save = pd.DataFrame(dic_camc_, index = [0])
dic_camc_save.to_csv("dic_camc__pos210828.csv", mode = 'w', encoding = 'utf-8-sig')

wordcloud = WordCloud(font_path='C:/Windows/Fonts/잘풀리는오늘 Medium.ttf',
                      background_color = 'white', 
                      colormap = "cool", 
                      mask = mask 
                     )

cloud = wordcloud.generate_from_frequencies(dic_camc)                      
plt.figure(figsize = (40 , 35))  
plt.imshow(cloud, interpolation="bilinear")
plt.axis('off')
# plt.show()
plt.savefig('긍정리뷰_형용사_워드클라우드.png')

y = np.arange(10)

items = ['안락하다','괜찮다', '좋아하다', '푹신하다', '만족하다', '튼튼하다', '빠르다','예쁘다', '좋다','편하다']
values = [286, 312, 332, 494, 547, 642, 676, 1582, 4536, 5314]
plt.barh(y, values, color = 'skyblue')
plt.yticks(y, items)

plt.title('긍정적인 리뷰에서 빈출 형용사 top10', fontsize = 13)
plt.xlabel('빈출수', fontsize = 12)

#plt.show()

plt.savefig('긍정리뷰_형용사_top10 막대그래프.png', dpi=300)




