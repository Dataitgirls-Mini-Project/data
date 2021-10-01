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

# 부정적인 리뷰만 불러오기
df = df[df['sentiment'] == 0]

# 말뭉치
neg_corpus = ' '.join(df['review_cleaned'].tolist())
neg_corpus

okt=Okt() 

#품사 별로 나눠주기 
neg_pos = okt.pos(neg_corpus, stem = True)

# 명사
noun_list = []

for item in neg_pos:
    
    w = item[0] #단어
    c = item[1] #품사
    
    if c == 'Noun' and len(w) > 1:
        noun_list.append(w)

# noun_list
# len(noun_list)

count_noun = Counter(noun_list)
noun_most= count_noun.most_common()
# noun_most

noun_stop_words = ['의자','생각','쿠션','부분','아주','커서','다른','처음','보고','그냥','별로','조금','진짜','다시']

#불용어 제거한 리스트

noun_most_list = []

for sent in noun_list:
    if sent not in noun_stop_words:
        noun_most_list.append(sent)

count_noun_most = Counter(noun_most_list)
cnmc = count_noun_most.most_common()
# cnmc

cnmc[0] = ('배송', 51)
del cnmc[9]
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
                      mask = mask 
                     )
cloud = wordcloud.generate_from_frequencies(dic_cnmc)                      
plt.figure(figsize = (40 , 35))  
plt.imshow(cloud, interpolation="bilinear")
plt.axis('off')
# plt.show()
plt.savefig('부정리뷰_명사_워드클라우드_1.png')

# 막대 그래프 글자 깨짐 해결
from matplotlib import font_manager, rc
import platform

if platform.system() == 'Windows':
# 윈도우인 경우
    font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
    rc('font', family=font_name)

x = np.arange(15)
items = ['의자', '생각', '부분','배송','조립','쿠션','사용','가격','구매','허리','제품','교환','엉덩이','택배','냄새']
values = [65, 47, 40, 34, 31, 25, 24, 22, 21, 18, 18, 18, 17, 17, 17]

plt.bar(x, values, color='y')
plt.bar(x, values, color='skyblue')
plt.xticks(x, items)
plt.figure(figsize = (40 , 38))  
plt.show()

y = np.arange(10)

items = ['냄새', '엉덩이', '교환', '제품', '허리', '구매', '가격', '사용' ,'조립','배송']
values = [17, 17, 18, 18, 18, 21, 22, 24, 31, 51]

plt.barh(y, values , color = 'skyblue')
plt.yticks(y, items)
plt.title('부정적인 리뷰에서 빈출 명사 top10', fontsize = 13)
plt.xlabel('빈출수', fontsize = 12)
#plt.show()

plt.savefig('부정리뷰_명사_top10 막대그래프.png', dpi=300)


# 형용사
adj_list = []

for item in neg_pos:
    
    w = item[0] #단어
    c = item[1] #품사
    
    if c == 'Adjective' and len(w) > 1:
        adj_list.append(w)

adj_list

len(adj_list)

count_adj = Counter(adj_list)
adj_most= count_adj.most_common()
adj_most

adj_stop_words = ['많다','어떻다','야하다','조금','같다','있다','없다','아니다','이다','그렇다','이렇다']

#불용어 제거한 리스트

adj_most_list = []

for sent in adj_list:
    if sent not in adj_stop_words:
        adj_most_list.append(sent)

count_adj_most = Counter(adj_most_list)
camc = count_adj_most.most_common()
#camc

camc[3] = ('예쁘다', 24)
del camc[15]
camc[1] = ('편하다', 57)
del camc[9]
# camc
camc = camc[:51]

dic_camc = dict(camc)

mask_image = Image.open('C:/Users/user/Areumpy/Mini Project/house_1.png')
mask = np.array(mask_image)

dic_camc_ = dic_camc
dic_camc_save = pd.DataFrame(dic_camc_, index = [0])
dic_camc_save.to_csv("dic_camc_210828.csv", mode = 'w', encoding = 'utf-8-sig')

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
plt.savefig('부정리뷰_형용사_워드클라우드.png')


y = np.arange(10)
items = ['안좋다','힘들다','짧다','아프다','괜찮다','안되다','불편하다','예쁘다','좋다', '편하다']
values = [8, 9, 11, 11, 14, 17,  22, 24, 55, 57]

plt.barh(y, values, color = 'skyblue')
plt.yticks(y, items)


plt.title('부정적인 리뷰에서 빈출 형용사 top10', fontsize = 13)
plt.xlabel('빈출수', fontsize = 12)
#plt.show()

plt.savefig('부정리뷰_형용사_top10 막대그래프.png', dpi=300)





