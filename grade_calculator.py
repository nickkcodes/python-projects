math = int(input("Math score: "))
science = int(input("Science score: "))
english = int(input("English score: "))

average = (math + science + english) / 3

print(f"\nAverage: {average:.2f}")

if average >= 90:
    print("Grade: Excellent")
elif average >= 75:
    print("Grade: Good")
else:
    print("Grade: Needs Improvement")
