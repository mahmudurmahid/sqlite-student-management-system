# 🎓 SQLite Student Management System

A Python 3.13-based desktop application designed to manage student records efficiently using SQLite. This project demonstrates CRUD (Create, Read, Update, Delete) operations with a user-friendly interface, making it ideal for educational institutions and administrative tasks.

---

## 📖 Table of Contents

- [User Experience (UX)](#user-experience-ux)
  - [User Stories](#user-stories)
- [Design](#design)
  - [Interface Structure](#interface-structure)
  - [Color Scheme & Typography](#color-scheme--typography)
- [Features](#features)
  - [Implemented Features](#implemented-features)
  - [Planned Improvements](#planned-improvements)
- [Technologies Used](#technologies-used)
  - [Languages Used](#languages-used)
  - [Libraries Used](#libraries-used)
- [Project Files](#project-files)
- [Installation & Usage](#installation--usage)
  - [How to Run](#how-to-run)
  - [Modifying the Database](#modifying-the-database)
- [Testing](#testing)
- [Credits](#credits)
  - [Author](#author)
  - [Tools Used](#tools-used)
  - [Acknowledgements](#acknowledgements)

---

## 🧑‍💼 User Experience (UX)

### 🧾 User Stories

**As an administrator**, I want to:

- Add new student records with details like name, age, and course.
- View a list of all students in the database.
- Update existing student information.
- Delete student records when necessary.

**As a user**, I want to:

- Search for a student by name or ID.
- Navigate the application with ease and clarity.

---

## 🎨 Design

### 🗂 Interface Structure

The application features a graphical user interface (GUI) built with Tkinter, comprising:

- **Input Fields**: For entering student details.
- **Buttons**: To execute actions like Add, Update, Delete, and Search.
- **Display Area**: A table or listbox showing current student records.

### 🌈 Color Scheme & Typography

- **Color Scheme**: Neutral tones for a professional appearance.
- **Typography**: Standard system fonts for readability.

---

## 🚀 Features

### ✅ Implemented Features

- **Add Student**: Input and save new student details to the SQLite database.
- **View Students**: Display all student records in a structured format.
- **Update Student**: Modify existing student information.
- **Delete Student**: Remove student records from the database.
- **Search Functionality**: Find students by name or ID.
- **Data Persistence**: All data is stored locally in an SQLite database file.

### 🛠️ Planned Improvements

- **Input Validation**: Ensure all fields are correctly filled before submission.
- **Enhanced Search**: Implement advanced search filters (e.g., by course or age).
- **User Authentication**: Add login functionality for administrators.
- **Export Data**: Allow exporting student records to CSV or PDF formats.
- **Responsive Design**: Improve GUI layout for different screen sizes.

---

## 💻 Technologies Used

### 🧑‍💻 Languages Used

- Python 3.13

### 📚 Libraries Used

- `tkinter`: For building the GUI.
- `sqlite3`: For database operations.

---

## 📁 Project Files

```bash
sqlite-student-management-system/
├── main.py # Main application script
├── database.db # SQLite database file
├── requirements.txt # List of dependencies
├── README.md # Project documentation
└── icons/ # Folder containing icon images
```

---

## 🛠 Installation & Usage

### ⚙️ How to Run

1. **Clone the repository**:

   ```bash
   git clone https://github.com/mahmudurmahid/sqlite-student-management-system.git
   cd sqlite-student-management-system
   ```

2. Install dependencies:

Ensure you have Python 3.13 installed. Install required libraries (if any):

```bash
pip install -r requirements.txt
```

3. Run the application:

```bash
python main.py
```

### 🧾 Modifying the Database

To view or edit the database directly, you can use tools like DB Browser for SQLite.

The database file database.db contains all student records.

## ✅ Testing

Manual testing has been conducted to ensure:

- Accurate addition of new student records.
- Proper display of all student data.
- Successful updating and deletion of records.
- Effective search functionality.

## 🙌 Credits

### 👨‍💻 Author

This project was created and maintained by **Mahmudur Mahid**. It serves as a portfolio-level demonstration of object-oriented programming principles applied in a practical Python application. Mahmudur is passionate about developing intuitive, educational, and well-structured backend systems and enjoys exploring how fundamental concepts like OOP can be used in real-world problem solving.

- [GitHub Profile](https://github.com/mahmudurmahid)
- [LinkedIn](#https://www.linkedin.com/in/mahmudur-mahid-a4aa78162/)

### 🛠 Tools Used

- Python 3.13 – Primary programming language.
- Tkinter – GUI development.
- SQLite3 – Lightweight relational database engine.
- DB Browser for SQLite – Used to visually inspect and manage the SQLite database during development. Official Site

### 🙏 Acknowledgements

- Python official documentation for guidance on syntax and module usage.
- Tkinter community examples for layout and widget structuring.
- The SQLite community and tutorials for database design and query structure.
- Open-source GUI database tools like DB Browser for SQLite for simplifying database inspection and debugging.
- Any peers or mentors who provided feedback or testing insights during development.
