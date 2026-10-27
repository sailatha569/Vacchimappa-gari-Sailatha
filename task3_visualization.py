import pandas as pd
import matplotlib.pyplot as plt

data = {'Month':['Jan','Feb','Mar','Apr','May'], 'Sales':[12000,15000,13000,18000,20000]}
df = pd.DataFrame(data)
plt.bar(df['Month'], df['Sales'])
plt.title('Monthly Sales')
plt.savefig('sales.png')
print("Visualization Done")