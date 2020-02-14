def date_parser(dates):
    
    """Date Parser - changes dates to date format 'yyyy-mm-dd'  
        
        Parameters
        ----------
        dates: list
                list of datetime strings in the format 'yyyy-mm-dd hh:mm:ss'
        
        Returns
        -------
        A list of only the date in 'yyyy-mm-dd' format.
    """  
    # your code here
    
    data_format = []                 #Empty list.
    for i in dates:                  #Iterate over elements of dates.
        x =  i.split(" ")[0]         #Split the strings in dates to get rid of the times.
        data_format.append(x)        #append splitted strings to the empty list 'data_format'
                                      
        
     
    return data_format               #Return the new list 'data_format'.
