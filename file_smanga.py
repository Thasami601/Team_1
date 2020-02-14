#imports pandas and numpy libraries
import pandas as pd
import numpy as np 


### START FUNCTION
def extract_municipality_hashtags(df):
    '''
    Finds the municipality and hashtags of from tweets.
    
    Parameters
    ----------
    df: dataframe containing tweets and dates of those tweets
    
    External Requirements
    ---------------------
    mun_dict: A dictionary that contains handles and corresponding municipalities

    Returns
    -------
    df: modified dataframe with municipality and hashtags 
    columns corresponding to every tweet 
    '''
    mun_list = []
    hash_list = []

    #Iterates though df.
    for index, row in df.iterrows():
        tweet = row["Tweets"].split()
        hashtags = []

        #Municipality is initial set to NaN.
        municipality = np.nan
        for word in tweet:
            if word[0]=='#':
                #Append hashtags to hash_list.
                hashtags.append(word.lower()) 
            elif word[0] =='@':
                if word in mun_dict.keys():
                    #Append municipalities to mun_list.
                    municipality = mun_dict[word]

        #Assigns Nan to hashtags if none are found.
        if len(hashtags)==0:
            hashtags = np.nan
        hash_list.append(hashtags)
        mun_list.append(municipality)

    #Adds 'municipality' and 'hashtags' columns to df.
    df['municipality'] = mun_list
    df['hashtags'] = hash_list
    
    return df
### END FUNCTION

#imports pandas and numpy libraries
import pandas as pd
import numpy as np 

### START FUNCTION
def number_of_tweets_per_day(df):
    '''
    Counts the number of tweets per day
    
    Parameters
    ----------
    df: dataframe containing tweets and dates of those tweets
    
    Returns
    -------
    new_df: dataframe with dates of tweets and number of tweets 
    on that day
    
    '''
    dates = []
    
    for index, row in df.iterrows():
        dates.append(row['Date'].split(' ')[0])

    dates_count = []
    count = []

    #Appends unique dates to dates_count.
    for i in dates:
        if i in dates_count:
            continue
        else:
            count.append(dates.count(i))
            dates_count.append(i)
 
    
    #Creates new dataframe.
    new_df = pd.DataFrame()

    #Adds 'Date' and 'Tweets' columns to new_df.
    new_df['Date'] = pd.to_datetime(dates_count[::-1])
    new_df['Tweets'] = count[::-1]
    
    return new_df.set_index('Date')
### END FUNCTION

#imports pandas and numpy libraries
import pandas as pd
import numpy as np

### START FUNCTION
def word_splitter(df):
    '''
    Splits given tweets and adds them another column in given dataframe
    
    Parameters
    ----------
    df: dataframe containing tweets and dates of those tweets
    
    Returns
    --------
    df: modified dataframe with 'Split Tweets' added column
    '''
    #Split tweets in df and append them to a new list.
    split_tweets = []
    for index, row in df.iterrows():
        tweet = (row['Tweets'].split(' '))
        split_tweets.append([i.lower() for i in tweet])
    
    #Add 'Split Tweets' column in df
    df['Split Tweets'] = split_tweets
    
    return df

### END FUNCTION

#imports pandas and numpy libraries
import pandas as pd
import numpy as np

### START FUNCTION
def stop_words_remover(df):
    '''
    Splits given tweets and removes 'stopwords' from them
    
    Parameters
    ----------
    df: dataframe containing tweets and dates of those tweets

    External Requirements
    ------------
    stop_words_dict: A dictionary that contains stop words
    
    Returns
    --------
    df: modified dataframe with 'Without Stop Words' added column
    '''
    #splits and appends tweets without stopwords to a list
    split_tweets = []
    for index,row in df.iterrows():
        tweet = row['Tweets'].split(" ")
        split_tweets.append([i.lower() for i in tweet if i.lower() not in stop_words_dict['stopwords']])
    #Add 'Without Stop Words' column to df
    df['Without Stop Words'] = split_tweets
    return df

### END FUNCTION