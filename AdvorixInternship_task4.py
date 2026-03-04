import pandas as pd
import matplotlib.pyplot as plt

# Load the file from the current directory
df = pd.read_csv('students.csv')

# --- 1. DATA ANALYSIS ---
# Group by 'Course' as shown in your LibreOffice sheet
course_counts = df.groupby('Course').size()
cs_students = df[df['Course'] == 'CS']

# --- 2. DATA VISUALIZATION ---
# This will now work because course_counts is no longer empty
plt.figure(figsize=(8, 4))
course_counts.plot(kind='bar', color='skyblue')
plt.title('Number of Students per Course')
plt.savefig('bar_chart.png') # Saves the file so you can submit it
plt.show()

# --- 3. DATA VISUALIZATION (3 Graphs) ---

# Graph 1: Bar Chart
plt.figure(figsize=(8, 4))
course_counts.plot(kind='bar', color='skyblue')
plt.title('Number of Students per Course')
plt.xlabel('Course Name')
plt.ylabel('Number of Students')
plt.tight_layout()
plt.savefig('bar_chart.png') # Saves the file to your folder
plt.show()

# Graph 2: Pie Chart
plt.figure(figsize=(7, 7))
course_counts.plot(kind='pie', autopct='%1.1f%%', startangle=140)
plt.title('Student Distribution by Course')
plt.ylabel('') # Removes the default 'None' label
plt.savefig('pie_chart.png')
plt.show()

# Graph 3: Horizontal Bar Chart
plt.figure(figsize=(8, 4))
course_counts.plot(kind='barh', color='salmon')
plt.title('Total Student Count by Department')
plt.xlabel('Count')
plt.tight_layout()
plt.savefig('horizontal_bar.png')
plt.show()

print("\nSuccess! 3 graphs have been saved as PNG files.")