import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset('titanic')
print(df.shape)
print(df.isnull().sum())
sns.countplot(x='survived', data=df)
plt.savefig('survival.png')
print("EDA Done")