import pandas as pd

df = pd.DataFrame({'Animal': ['Falcon', 'Falcon',
                               'Parrot', 'Parrot'],
                    'Max Speed': [380., 370., 24., 26.]})
res = df.groupby("Animal", group_keys=False).ohlc()
print(type(res))
print(res)
print(res.reset_index())


ser = pd.Series([1, 3, 2, 4, 3, 5],
                index=pd.DatetimeIndex(['2023-01-01',
                                        '2023-01-10',
                                        '2023-01-15',
                                        '2023-02-01',
                                        '2023-02-10',
                                        '2023-02-15']))
res = ser.resample('MS').ohlc()
print(res)