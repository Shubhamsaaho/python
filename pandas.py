import pandas as pd
data = { "Name": ["Shubham", "Aman", "yogesh", "Rahul", "mani", "Karan", "shivansh", "Ravi", "abhinav", "amit"],"English": [85, 78, 92, 88, 76, 80, 89, 77, 90, 84],
"Math":    [90, 75, 88, 92, 69, 85, 91, 73, 86, 82],
    "Science": [88, 79, 95, 90, 72, 86, 93, 78, 89, 85],
    "History": [76, 74, 80, 83, 70, 79, 82, 75, 81, 78],
    "Computer": [95, 88, 96, 94, 85, 89, 97, 87, 93, 90],
}
df = pd.DataFrame(data)
df["Total"] = df[["English", "Math", "Science", "History", "Computer"]].sum(axis=1)

print("Marksheet:\n")
print(df)