import numpy as np
import pandas as pd

#Question 1
start_dt = pd.to_datetime('2017-06-05')
stocks = pd.DataFrame(data=None, 
                      index=start_dt + pd.to_timedelta(np.arange(5), 'D'))
print(stocks)