import pandas as pd

df = pd.read_csv('sales.csv')
df['Total_Revenue'] = df['Price'] * df['Quantity_Sold']
highest_total_revenue = df[df['Total_Revenue'] == df['Total_Revenue'].max()]
electronics_products = df[df['Category'] == 'Electronics']
average_products = f'Average price: {df['Price'].mean():.2f}'
df.to_csv('sales_analysis.csv', index=False)

print(df)
print()
print(highest_total_revenue)
print()
print(electronics_products)
print()
print(average_products)
print()
print('Saved! ')