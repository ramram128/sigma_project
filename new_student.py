import os
import json
import pandas as pd
from flask import Flask, request, render_template, redirect, url_for, session, jsonify
from flask_cors import CORS
from werkzeug.utils import secure_filename

app = Flask(__name__)
CORS(app)
app.secret_key = os.urandom(24)

# Configurations
FILES_FOLDER = "D:/auto_attendance/output"
IMAGES_FOLDER = "D:/auto_attendance/images"
EXCEL_FILE = os.path.join(FILES_FOLDER, "students.xlsx")

@app.route('/new-student', methods=['GET', 'POST'])
def new_student():
    if not session.get('admin_logged_in'):
        return redirect('/login')

    if request.method == 'POST':
        roll_no = request.form.get('roll_no')
        student_name = request.form.get('student_name')
        parent_no = request.form.get('parent_no')
        image = request.files.get('image')

        if roll_no and student_name and parent_no and image:
            # Save image
            filename = secure_filename(f"{roll_no}_{student_name}.jpg")
            image.save(os.path.join(IMAGES_FOLDER, filename))

            # Update Excel
            df = pd.read_excel(EXCEL_FILE)
            new_row = {
                "S/No": len(df) + 1,
                "Roll No": roll_no,
                "Student Name": student_name,
                "Parent No": parent_no
            }
            df = df.append(new_row, ignore_index=True)
            df.to_excel(EXCEL_FILE, index=False)

            return "Student Registered Successfully!"

        return "Missing Fields"

    return render_template('new_student.html')

if __name__ == '__main__':
    app.run(debug=True)
