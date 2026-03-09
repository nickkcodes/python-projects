import pandas as pd

df = pd.read_csv('students.csv')
top = df[df['Math_Grade'] == df['Math_Grade'].max()]
lowest = df[df['Math_Grade'] == df['Math_Grade'].min()]
failing = df[df['Math_Grade'] < 80]
print(df)
print()
print(f'Top student:\n {top}')
print()
print(f'Lowest student:\n {lowest}')
print()
print(f'Math average: {df["Math_Grade"].mean():.2f}')
print(f'Science average: {df["Science_Grade"].mean():.2f}')
print()
print(f'Failing students:\n {failing}')
