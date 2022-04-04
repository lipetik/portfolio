import pandas as pd
import matplotlib.pyplot as plt 


df = pd.read_csv("text.csv")
print(df.head())

plt.plot(df['x'], df['y'])
plt.show()


