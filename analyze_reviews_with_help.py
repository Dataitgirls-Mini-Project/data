import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
import matplotlib.font_manager as fm

font_list = fm.findSystemFonts(fontpaths = None, fontext = 'ttf')
font_list[:]
##설정 파일 위치
print (mpl.matplotlib_fname())

print ('버전: ', mpl.__version__)
print ('설치 위치: ', mpl.__file__)
print ('설정 위치: ', mpl.get_configdir())
print ('캐시 위치: ', mpl.get_cachedir())

font_list = fm.findSystemFonts(fontpaths=None, fontext='ttf')
font_list[:10] 
[(f.name, f.fname) for f in fm.fontManager.ttflist if 'Nanum' in f.name]

path ='C:\\Windows\\Fonts\\나눔고딕.ttf'
fontprop = fm.FontProperties(fname=path, size=12)


# ### - 가설: '도움이 돼요'를 받은 리뷰는 전체 리뷰의 절반 이하일 것이다.
# ### [결과물] 파이 차트 (시각화)

import pandas as pd
df = pd.read_csv('reviews_preprocessed.csv')
df.head()
df["help"].value_counts()

df.loc[(df.help != "0"), 'help'] = "1"
df["help"].value_counts()

t = df["help"].value_counts()
x = t.index
y = t.values

# print(x)
# print(y)

plt.bar(x, y)
plt.title('도움이 돼요 유무별 리뷰 수', fontproperties=fontprop)
plt.xlabel('도움이 돼요 수', fontproperties=fontprop)
plt.ylabel('리뷰 수', fontproperties=fontprop)
plt.xticks(x, ["O개", "1개 이상"], fontproperties=fontprop)
plt.show()

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
# ### [결과물] 막대 그래프 (시각화)
def get_len(a) :
    return len(a)

df["len_review_cleaned"] = df["review_cleaned"].apply(get_len)
# df.head()

df2 = pd.pivot_table(df, index = ['help'], values='len_review_cleaned', aggfunc = 'mean')
# df2.head()

print(df2.index)
print(df2['len_review_cleaned'].values)
x = df2.index
y = df2['len_review_cleaned'].values

plt.bar(x, y, color = '#09ADDB')
plt.title('도움이 돼요 유무별 평균 리뷰 길이', fontproperties=fontprop)
plt.xlabel('도움이 돼요 수', fontproperties=fontprop)
plt.ylabel('평균 리뷰 길이', fontproperties=fontprop)
plt.xticks(x, ["O개", "1개 이상"], fontproperties=fontprop)
plt.show()

import pandas as pd
help = pd.read_csv('reviews_preprocessed.csv')
help.head()
help["help"].value_counts()
help["help"].value_counts().index
help["help"].unique()

def help_clean (a):
    if "," in a:
        return a.replace(",","")
    return a
help["help"] = help["help"].apply(help_clean)

help = help.astype({'help':'int'})
help["help"].sum()
help2 = help[help["help"] > 0]

m = help2["help"].value_counts()
# m

x = m.index
y = m.values

print(x)
print(y)

def help_pre(a):
    if a <= 5 :
        return "1개~5개"
    elif a> 5 and a <= 10:
        return "5~10개"
    else :
        return "10개 이상"
help2["help_pre"] = help2["help"].apply(help_pre)

m = help2["help_pre"].value_counts()
x = ['1개~5개','5~10개', '10개 이상']
y = [1070,   58,   70]


font_name = font_manager.FontProperties(fname='C:\\Windows\\Fonts\\나눔고딕.ttf').get_name()
rc('font', family=font_name) #폰트 정하기(글자 깨짐 방지)
plt.figure(figsize=(7,7))
plt.title('도움이 돼요 수별 리뷰수 비율', fontproperties=fontprop,
       fontsize = 13)
plt.pie(y, labels=['1개~5개','5~10개', '10개 이상'], autopct='%.1f%%', colors = ['#09ADDB','#C4B288','#CFD0CD'])
plt.legend(['1개~5개','5~10개', '10개 이상'], loc = 'lower right')
plt.show()

# 도움이 돼요 100개 이상 받은 리뷰들이 긍정 혹은 부정 리뷰인지? - 10개
df = help["help"].value_counts()
df = df.sort_index()
df = pd.to_numeric(df.index)
display(df)
bins = [-1,0,20,40,60,80,2128]
labels = ['0개','1~20','21-40','41-60','61~80','81개 이상']
cat = pd.cut(df.values,bins,labels=labels)
display(cat)

len(help[help["help"] >= 100])
help[help["help"] >= 100]


# #### 도움이 돼요 상위 10개 리뷰는 모두 리뷰 평점이 5.0! 즉 긍정적인 리뷰로 분류가 되었지만, 가장 많이 도움이돼요를 받은 리뷰의 실제 내용은 부정적인 리뷰였음을 확인했다.
help_top_10 = help[help["help"] >= 100][['total_star','review_cleaned','help']]




