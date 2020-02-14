dates = twitter_df['Date'].to_list()
def date_parser(dates):
    # your code here
    ent = []  
    for i in dates:
        x =  i.split(" ")[0]
        ent.append(x)
    return ent
   