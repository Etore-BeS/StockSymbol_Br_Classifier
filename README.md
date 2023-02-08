# StockSymbol_Br_Classifier
Classifier of Brazilian Stocks for StockSymbol lib. This function categorize the types of stock and their fractional status to speed up the filtering process. 

## Installation
Just move the file 'classify.py' to the directory where you're using the lib StockSymbol. 

## Usage
```python
# Import the libs necessary
from classify import class_data
from stocksymbol import StockSymbol
import pandas as pd


# Acess the StockSymbol API e get the Dataframe of brazilian stocks
api_key = 'INSERT YOUR API KEY'
ss = StockSymbol(api_key)
df = pd.DataFrame(ss.get_symbol_list(market='BR'))

# Returns a DataFrame with the type of stock and a boolean about their fractional status
df = class_data(df)
```

## Contributing

Pull requests are welcome.

## License

[MIT](https://choosealicense.com/licenses/mit/)
