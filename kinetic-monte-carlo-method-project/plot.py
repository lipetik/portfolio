import pandas as pd 
import matplotlib.pyplot as plt

df = pd.read_csv("teste.csv")
print(df.head())
print(df.k)
# k_array = df["k"].to_numpy()
# n0_array = df['n=0'].to_numpy()

# plt.plot(k_array, n0_array)
# df['k'].apply(lambda r: r.real)


# plt.plot(df['k'], df['n=0'])
# plt.plot(df['k'], df['n=1'])
# plt.plot(df['k'], df['n=2'])
# plt.plot(df['k'], df['n=3'])
# plt.show()


