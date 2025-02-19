import mysql.connector
import tkinter as tk

def create_table():
    conn = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="vishwak@151370",
        database="projects"
    )
    cursor = conn.cursor() 
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS student_fees (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255),
            fees INT
        )
    ''')
    conn.commit()
    conn.close()

def register_student(name, fees):
    conn = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="vishwak@151370",
        database="projects"
    )
    cursor = conn.cursor()
    cursor.execute('INSERT INTO student_fees (name, fees) VALUES (%s, %s)', (name, fees))
    conn.commit()
    conn.close()

def generate_fees_registration():
    conn = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="vishwak@151370",
        database="projects"
    )
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM student_fees')
    data = cursor.fetchall()
    conn.close()

    result = ""
    for row in data:
        result += f"Name: {row[1]}, Fees: {row[2]}\n"
    return result

def register_button_click():
    student_name = name_entry.get()
    student_fees = int(fees_entry.get())
    register_student(student_name, student_fees)
    result_label.config(text=generate_fees_registration())

if __name__ == "__main__":
    create_table()

    window = tk.Tk()
    window.title("Student Fees Registration")

    name_label = tk.Label(window, text="Enter student name:")
    name_label.pack()

    name_entry = tk.Entry(window)
    name_entry.pack()

    fees_label = tk.Label(window, text="Enter fees:")
    fees_label.pack()

    fees_entry = tk.Entry(window)
    fees_entry.pack()

    register_button = tk.Button(window, text="Register", command=register_button_click)
    register_button.pack()

    result_label = tk.Label(window, text="")
    result_label.pack()

    window.mainloop()