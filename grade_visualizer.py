import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('students.csv')

plt.bar(df['Name'], df['Math_Grade'], color='blue')
plt.title('Math Grades')
plt.xlabel('Student')
plt.ylabel('Grade')
plt.savefig('math_grades.png')
plt.clf()

plt.pie(df['Math_Grade'], labels=df['Name'], autopct='1.2f%%')
plt.title('Math Grades Distribution')
plt.savefig('math_grades_pie.png')