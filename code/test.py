import pandas as pd
import numpy as np
import matplotlib as mpl

df = pd.DataFrame()

df['BTC'] = [100, 120, 131, 121, 133, 22.67, 33.99]
df['ETH'] = [400.81, 420, 434, 424, 433, 22.67, 33.99]

df.style.format({
    "BTC": "${:,..2f}"
})


print(df)
