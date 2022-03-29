import pandas as pd
import re 

def top_tweets_retweeted(data):
    list_top = []
    for d in data:
        sub_top = d.sort_values(by='retweetCount', ascending=False).head(10)
        list_top.append(sub_top)
    pd_top = pd.concat(list_top, axis=0)
    top = pd_top.sort_values(by='retweetCount', ascending=False).head(10)
    return top

def top_users(data):
    list_top = []
    for d in data:
        df_user = pd.DataFrame(d['user'].tolist()).fillna(0)['id'].value_counts().head(10)
        list_top.append(df_user)
    pd_top = pd.concat(list_top, axis=0)
    top = pd_top.groupby('id').value_counts().head(10)
    return top

def top_days_tweets(data):
    list_top = []
    for d in data:
        sub_top = d.groupby('date').value_counts().head(10)
        list_top.append(sub_top)
    pd_top = pd.concat(list_top, axis=0)
    top = pd_top.groupby('date').value_counts().head(10)
    return top

def top_hashtags(data):
    pass
    
data = pd.read_json('farmers-protest-tweets.json', lines=True, chunksize = 20000)
# top_tweets_retweeted(data)
# top_users(data)
# top_days_tweets(data)
# top_hashtags()