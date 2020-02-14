### START FUNCTION
def dictionary_of_metrics(items):
    # your code here
    for item in items:
        
        return {'mean': round(np.mean(items), 2),  'median': round(np.median(items), 2), 'var': round(np.var(items, ddof = 1), 2), 
            'std': round(np.std(items, ddof = 1), 2),'min': round(min(items), 2),'max': round(max(items), 2)}



### END FUNCTION 
