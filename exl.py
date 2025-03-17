from openpyxl import Workbook

# Create a new workbook and select the active sheet
wb = Workbook()
sheet = wb.active



# Set column headers
sheet.append(["S/No", "Roll No", "Student Name", "Parent No"])

# Add sample student data
students = [
    (1,"101", "RAJESH", "9876543210"),
    # (2, "102", "KUMAR B", "9876543211"),
    # (3, "103", "PRIYA C", "9876543212"),
    # (4, "104", "RAJESH", "9876543213"),
    # (5, "105", "MOHAN", "9876543214"),
    # (6, "106", "RAM", "9025213207")

    
]

# Insert student records
for student in students:
    sheet.append(student)

# Save the file
wb.save("data.xlsx")
print("✅ data.xlsx created successfully!")
