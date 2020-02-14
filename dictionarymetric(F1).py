### Function to calculate mean, median, variance, standard deviation, min, max
def dictionary_of_metrics(items):
    """this function will use eskom data in gauteng amd calculate key statistical 
    mean, median, var, std, min and max from the dataset"""   
            # using numpy library to calculate mean, median, var and std
    for item in items:
        """ ---
        this function uses the dictionary method as the output format,
        the key are the components of information extracted
        the values are the calculations based on the data corresponding to the the key
        --- """
        return {'mean': round(np.mean(items), 2),  'median': round(np.median(items), 2), 'var': round(np.var(items, ddof = 1), 2), 
                'std': round(np.std(items, ddof = 1), 2),'min': round(min(items), 2),'max': round(max(items), 2)}
        """the function returns the name of the calculation and the value corresponding, 
        ----
        mean = sum(n)/n
        median = middle number in data set
        var = squared deviation of a random variable from its mean
        std dev = squared variance
        max = highest value in dataset
        min = lowest value in dataset
        ---
        each value is rounded to the 2nd decimal
        Standrd deviation and variance use an additional parameter, called ddof is set to 1.
        This function has utilised the numpy library to caluclate mean, median, var, std""" 
### END FUNCTION 
