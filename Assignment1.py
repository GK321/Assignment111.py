import pandas as pd
import numpy as np

df = pd.DataFrame ({'ship mode': ['Same Day', 'First class', 'Standard class', 'Other'],
                    'sales': [100, 200, 300, 400],
                    'profit': [10, 20, 30, 40]})

df['surcharge'] = np.where(df['ship mode' ] == 'Same Day', 0.2,
                          np.where(df['ship mode'] == 'First Class', 0.1,
                                  np.where(dff[ 'ship mode'] == 'Standard class',0.05, 0)))

df['total cost'] = (df['sales'] - df['profit' ]) * (1 + df[' surcharge'])

print (df)