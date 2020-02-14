def five_num_summary(items):
    """ Calculates summary statistics of the given list :
    maximum, minimum, median, quartile 1, quartile 3
    
    Parameters
    ----------
    items: A list of intergers/floats
    
    
    Returns
    -------
    dict: 
        Returns values of the dictionary as the summary staistics rounded
        off to two decimal places and the description
        of the values as keys.
    
    """
    # your code here
    a = 'max median min q1 q3'.split()   #Creates a list with keys for the dictionary
    b = [round(np.max(items),2),round(np.median(items),2),
         round(np.min(items),2),round(np.quantile(items,0.25),2),
         round(np.quantile(items, 0.75),2)]   #Creates a list of values for the dictionary
   
    return dict( list(zip(a,b)))   #returns a dictionary matching the keys and values from the lists