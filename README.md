# Student-Management-System

# 🎓 Student Management System  

A **Python-based Tkinter GUI** application that integrates **MySQL** to manage **student records, marks, and fees**. This system allows users to store, retrieve, and display student marks and fees securely in a structured database.  

## 📌 Features  

✅ **Student Marks Management:**  
- Add student records (Name, Roll Number, Email, Gender, Subject-wise Marks)  
- Store data securely in a **MySQL database**  
- Retrieve student details using Roll Number  
- Generate and display a **Marks Card**  

✅ **Student Fees Management:**  
- Register student fees  
- Store student fee records in MySQL  
- Display a list of all students with their fee details  

## 🛠️ Technologies Used  

- **Python** 🐍  
- **Tkinter** (for GUI)  
- **MySQL Connector** (for database interactions)  

## 📂 File Overview  

1. **`mysql_installation.md`** – Provides installation options for MySQL on macOS (Apple Silicon & Intel).  
2. **`student_management.py`** – Handles student records and marks management.  
3. **`student_fees.py`** – Manages student fee registration.  
4. **`README.md`** – Project documentation.  

## 🚀 Installation Guide  

### **Step 1: Install MySQL**  

- For **macOS users**, check the installation guide in `mysql_installation.md`  
- For **Windows/Linux**, download MySQL from [MySQL Official Site](https://dev.mysql.com/downloads/)  

### **Step 2: Install Python Dependencies**  

```sh
pip install mysql-connector-python tk
