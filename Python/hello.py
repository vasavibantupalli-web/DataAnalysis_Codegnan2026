

# Student performance data
data = {
    "Name": ["Ravi", "Priya", "Arun", "Sita", "Kiran"],
    "Attendance": [85, 92, 70, 95, 80],
    "Maths": [78, 88, 65, 92, 75],
    "Science": [82, 90, 60, 95, 72],
    "English": [75, 85, 70, 90, 78]
}

# Create DataFrame
df = id.DataFrame(data)

# Calculate average marks
df["Average"] = (
    df["Maths"] +
    df["Science"] +
    df["English"]
) / 3

# Calculate performance status
df["Status"] = df["Average"].apply(
    lambda x: "Excellent" if x >= 85
    else "Good" if x >= 70
    else "Needs Improvement"
)

# Display student data
print("\n===== STUDENT PERFORMANCE ANALYTICS =====\n")
print(df.to_string(index=False))

# Class average
class_average = df["Average"].mean()

print("\nClass Average: take 2 hour per day")
