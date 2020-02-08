import pandas as pd
import numpy as np
from sklearn.metrics import pairwise_distances_argmin_min

subreddit_clust = pd.read_csv('clustered_subreddits.csv')
subreddit_clust.set_index('index', drop=True, inplace=True) # sets the subreddit names as index.

def convert(input_, df = subreddit_clust):# should convert a list of subredditnames into a df of index input_. 
    return pd.DataFrame([df.loc[data_] for data_ in input_])

def recur_sample(point_, df = subreddit_clust): # random sample of x names from point_ cluster.
    return list(df[df['dbscan']==point_].sample(5).index)

def recommend_util(input_, df = subreddit_clust): # returns 5 recomendations from clusters of given name subreddit.
    temp = convert(input_)['dbscan'] 
    return list([recur_sample(i) for i in temp])

def get_value(prompt, df= subreddit_clust): # gennerates input
    while True:
        try:
            value = str(input(prompt)).lower()
        except ValueError:
            print("Sorry, your entry is not valid.")
            continue
        if value not in list(df.index):
            print("Sorry,could not find a subreddit of your choice.Try again or you can choose from the following subreddits?", random.choices(df.index, k=10))
            continue
        else:
            break
    return value

name_ =[]
name_.append(get_value("Choose 3 subreddits you like and we would make a few recommendations you might like.Your first entry is: "))
name_.append(get_value("Your second entry is: "))
name_.append(get_value("Your third entry is: "))
# list_ = [] # placeholder for the imput. 
# name_ = list(subreddit_clust.sample(5).index)



print('Based on your choices your recommended subreddits are as follows: ',recommend_util(name_))
