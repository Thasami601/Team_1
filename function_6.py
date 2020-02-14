
def word_splitter(df):
    ''''split tweets in the dataframe and append them to a new list, then make them lower case. merge the the new list into the dataframe column'''
    split_tweets = []
    for index, row in df.iterrows():
        a = (row['Tweets'].split(' '))
        split_tweets.append([i.lower() for i in a])
    
    #Add to new column in df
    new_df = df.copy(deep=True)
    new_df['Split Tweets'] = split_tweets
    return new_df

