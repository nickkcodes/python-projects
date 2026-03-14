import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('sales.csv')

#Revenue
df['Revenue'] = df['Price'] * df['Quantity_Sold']

#Revenue by category
category_revenue = df.groupby('Category')['Revenue'].sum()

#Bar Chart
plt.bar(df['Product'], df['Price'] * df['Quantity_Sold'])
plt.title('Total Revenue Per Product' )
plt.xlabel('Products')
plt.ylabel('Total Revenue')
plt.savefig('bar_chart.png')
plt.clf()

#Pie Chart
plt.pie(category_revenue, labels=category_revenue.index, autopct='%1.2f%%')
plt.title('Category Revenue Distribution')
plt.savefig('pie_chart.png')
plt.clf()

#Line Chart
plt.plot(df['Product'], df['Revenue'], marker='o')
plt.title('Revenue')
plt.xlabel('Products')
plt.ylabel('Revenue')
plt.savefig('line_chart.png')
plt.clf()
