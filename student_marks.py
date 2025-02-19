import mysql.connector
import tkinter as tk
from tkinter import messagebox 

def setup_mysql_database():
    conn = mysql.connector.connect(
        host='127.0.0.1',
        user='root',
        password='vishwak@151370',
        database='projects'
    )

    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS students (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255),
            roll_number INT,
            email_id VARCHAR(45),
            gender VARCHAR(10),
            sci_marks INT, soc_marks INT, eng_marks INT, gk_marks INT, maths_marks INT,
            lang_marks INT
        )
    ''')

    conn.commit()
    conn.close()

def add_student(name, roll_number, email_id, gender, sci_marks, soc_marks, eng_marks, gk_marks, maths_marks, lang_marks):
    conn = mysql.connector.connect(
        host='127.0.0.1',
        user='root',
        password='vishwak@151370',
        database='projects'
    )

    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO students (name, roll_number, email_id, gender, sci_marks, soc_marks, eng_marks, gk_marks, maths_marks, lang_marks)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    ''', (name, roll_number, email_id, gender, sci_marks, soc_marks, eng_marks, gk_marks, maths_marks, lang_marks))

    conn.commit()
    conn.close()

def get_student_data(roll_number):
    conn = mysql.connector.connect(
        host='127.0.0.1',
        user='root',
        password='vishwak@151370',
        database='projects'
    )

    cursor = conn.cursor()

    cursor.execute('''
        SELECT * FROM students WHERE roll_number = %s
    ''', (roll_number,))

    student = cursor.fetchone()

    conn.close()

    return student

def generate_marks_card(student):
    if student:
        print(f'Marks Card\n\nName: {student[1]}\nRoll Number: {student[2]}\nEmailId: {student[3]}\nGender: {student[4]}\n'
              f'sci_marks: {student[5]}\nsoc_marks: {student[6]}\neng_marks: {student[7]}\ngk_marks: {student[8]}\n'
              f'maths_marks: {student[9]}\nlang_marks: {student[10]}')
    else:
        print('Student not found')

def add_student_button_click():
    name = name_entry.get()
    roll_number = int(roll_number_entry.get())
    email_id = email_entry.get()
    gender = gender_entry.get()
    sci_marks = int(sci_marks_entry.get())
    soc_marks = int(soc_marks_entry.get())
    eng_marks = int(eng_marks_entry.get())
    gk_marks = int(gk_marks_entry.get())
    maths_marks = int(maths_marks_entry.get())
    lang_marks = int(lang_marks_entry.get())

    add_student(name, roll_number, email_id, gender, sci_marks, soc_marks, eng_marks, gk_marks, maths_marks, lang_marks)
    messagebox.showinfo("Success", "Student added successfully!")

def generate_marks_card_button_click():
    roll_number = int(roll_number_entry.get())
    student_data = get_student_data(roll_number)

    if student_data:
        generate_marks_card(student_data)
    else:
        messagebox.showerror("Error", "Student not found!")

setup_mysql_database()

window = tk.Tk()
window.title("Student Management System")

name_label = tk.Label(window, text="Name:")
name_entry = tk.Entry(window)

roll_number_label = tk.Label(window, text="Roll Number:")
roll_number_entry = tk.Entry(window)

email_label = tk.Label(window, text="Email ID:")
email_entry = tk.Entry(window)

gender_label = tk.Label(window, text="Gender:")
gender_entry = tk.Entry(window)

sci_marks_label = tk.Label(window, text="Science Marks:")
sci_marks_entry = tk.Entry(window)

soc_marks_label = tk.Label(window, text="Social Marks:")
soc_marks_entry = tk.Entry(window)

eng_marks_label = tk.Label(window, text="English Marks:")
eng_marks_entry = tk.Entry(window)

gk_marks_label = tk.Label(window, text="GK Marks:")
gk_marks_entry = tk.Entry(window)

maths_marks_label = tk.Label(window, text="Maths Marks:")
maths_marks_entry = tk.Entry(window)

lang_marks_label = tk.Label(window, text="Language Marks:")
lang_marks_entry = tk.Entry(window)

add_student_button = tk.Button(window, text="Add Student", command=add_student_button_click)
generate_marks_card_button = tk.Button(window, text="Generate Marks Card", command=generate_marks_card_button_click)

name_label.grid(row=0, column=0)
name_entry.grid(row=0, column=1)

roll_number_label.grid(row=1, column=0)
roll_number_entry.grid(row=1, column=1)

email_label.grid(row=2, column=0)
email_entry.grid(row=2, column=1)

gender_label.grid(row=3, column=0)
gender_entry.grid(row=3, column=1)

sci_marks_label.grid(row=4, column=0)
sci_marks_entry.grid(row=4, column=1)

soc_marks_label.grid(row=5, column=0)
soc_marks_entry.grid(row=5, column=1)

eng_marks_label.grid(row=6, column=0)
eng_marks_entry.grid(row=6, column=1)

gk_marks_label.grid(row=7, column=0)
gk_marks_entry.grid(row=7, column=1)

maths_marks_label.grid(row=8, column=0)
maths_marks_entry.grid(row=8, column=1)

lang_marks_label.grid(row=9, column=0)
lang_marks_entry.grid(row=9, column=1)

add_student_button.grid(row=10, column=0, columnspan=2)
generate_marks_card_button.grid(row=11, column=0, columnspan=2)

window.mainloop()