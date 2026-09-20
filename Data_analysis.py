import pandas as pd

# Read the student data
df = pd.read_csv("student_data.csv")

# Calculate total and average marks
df["Total"] = df[["Python", "Data_Analytics", "AI_ML", "English"]].sum(axis=1)
df["Average"] = df[["Python", "Data_Analytics", "AI_ML", "English"]].mean(axis=1)

# Find the student with the highest total marks
top_student = df.loc[df["Total"].idxmax()]

print("Student Performance Analysis")
print("----------------------------")
print(df)

print("\nHighest Scoring Student")
print("-----------------------")
print(f"Name: {top_student['Name']}")
print(f"Total Marks: {top_student['Total']}")
print(f"Average Marks: {top_student['Average']:.2f}")

print("\nAverage Marks by Subject")
print("------------------------")
print(df[["Python", "Data_Analytics", "AI_ML", "English"]].mean())