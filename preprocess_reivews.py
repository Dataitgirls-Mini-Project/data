import pandas as pd
import csv
import re

raw_data = pd.read_csv('reviews_final.csv')

text = ''
review = []
for each_line in raw_data['review_original']:
    review.append(each_line)

def clean_str(text):

    pattern = '([ㄱ-ㅎㅏ-ㅣ]+)'  # 한글 자음, 모음 제거
    text = re.sub(pattern=pattern, repl='', string=text)

    pattern = '[^\w\s]'         # 특수기호제거
    text = re.sub(pattern=pattern, repl='', string=text)
    return ' '.join(text.split())  

review_=[]
for i in review: 
    a = clean_str(i)
    review_.append(a)  #불용어제거한 review 저장

print(review_)

review_df = pd.DataFrame(review_, columns = ['review_cleaned'])
review_df.to_csv('review_final_cleaned.csv', encoding='utf-8-sig')