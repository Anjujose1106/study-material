import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data = pd.read_csv('https://tinyurl.com/ChrisCoDV/Products/DailySales.csv', index_col=0)
pd.plotting.register_matplotlib_converters()
data.index = pd.to_datetime(data.index)

sample_rate = 'M'  # weekly
averaged_data = data.resample(sample_rate).mean()
period = 7
rolling_average = data.rolling(window=period).mean()

selected = ['B', 'C', 'I', 'K', 'N', 'Q', 'R', 'U', 'V', 'Y']
print(data[selected].head())

plt.figure(figsize=(8, 8))
plt.plot(averaged_data[selected], linewidth=0.5)
plt.gca().set_prop_cycle(None)
for name in selected:
    x = np.arange(len(data[name]))
    z = np.polyfit(x, data[name], 1)
    trend = np.poly1d(z)
    plt.plot(data.index, trend(x), linestyle='--')
# plt.ylim(ymin=0)
plt.xlabel('Date', fontsize=18)
plt.ylabel('Units sold', fontsize=18)
plt.title('Very Low Volume Monthly Average\n with Linear Trendlines', fontsize=20)
plt.legend(selected, loc=2)
plt.show()
