import glob
import pandas as pd

reviews = pd.concat(map(pd.read_csv, glob.glob('./data/*.csv')), ignore_index=True)
reviews.drop(reviews.filter(regex="Unnamed"),axis=1, inplace=True)

def rating_to_label(rating):
    if rating > 3:
        return 1
    elif rating <= 3:
        return 0
    else:
        return 'null'

reviews['sentiment'] = reviews['total_star'].apply(lambda x: rating_to_label(x))

reviews.to_csv('./data/reviews.csv', encoding='utf-8-sig')