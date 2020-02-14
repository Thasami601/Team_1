def five_num_summary(items):
    # your code here
    a = 'max median min q1 q3'.split()
    b = [round(np.max(items),2),round(np.median(items),2),round(np.min(items),2),round(np.quantile(items,0.25),2),round(np.quantile(items, 0.75),2)]
   
    return dict( list(zip(a,b)))