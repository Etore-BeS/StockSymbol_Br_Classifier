import pandas as pd

#Inserting Column of only number within the ticker called 'symbol_cl'
def split_digit(x):
    split = str(x.split('.')[0])
    num = ''
    for s in [c for c in split][-3:]:
        if s.isdigit():
            num += s
        else: pass
    return num

#Inserting a boolean Column checking if it is a fractional stock called 'fractional'
def is_frac(x):
    if list(x)[-4] == 'F':
        return True
    else: return False



def class_data(df):
    
   
    #Dictionary of the types of stock listed in Brazilian Market
    stock_type = {'1' : 'Subscription Right - Commom Share', '2': 'Subscription Right - Preferred Share', '3' : 'Common Share', '4' : 'Preferred Share', 
                '5': 'Preferred Share - Class A', '6': 'Preferred Share - Class B', '7': 'Preferred Share - Class C', '8': 'Preferred Share - Class d',
                '9': 'Subscription Receipt - Common Share', '10': 'Subscription Receipt - Preferred Share', '11': 'Units/ETF', '31': 'BDR Receipt',
                '32': 'BDR - Level 2', '33': 'BDR - Level 3', '34': 'BDR', '35': 'BDR'} 

    cl_series = pd.Series(df['symbol']).apply(split_digit)
    df['symbol_cl'] = cl_series

    #Inserting Column of Types of Stock called 'type'
    type_series = pd.Series(df['symbol_cl']).map(stock_type)
    df['type'] = type_series
    df = df.drop(columns='symbol_cl')

    

    frac_series = pd.Series(df['symbol']).apply(is_frac)
    df['fractional'] = frac_series

    return df
