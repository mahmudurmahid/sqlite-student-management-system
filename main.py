from PyQt6.QtWidgets import QApplication, QVBoxLayout, QLabel, QWidget, QGridLayout, QLineEdit, QPushButton, QMainWindow, QTableWidget, QTableWidgetItem, QDialog, QVBoxLayout, QComboBox, QToolBar, QStatusBar, QMessageBox
from PyQt6.QtGui import QAction, QIcon
from PyQt6.QtCore import Qt
import sys
import sqlite3


class DatabaseConnection:
    def __init__(self, database_filename="database.db"):
        """ Initializes the database connection with the given filename. """
        self.database_filename = database_filename
    
    def connect(self):
        """ Connects to the SQLite database and returns the connection object. """
        connection = sqlite3.connect(self.database_filename)
        return connection
    


class MainWindow(QMainWindow):
    def __init__(self):
        """ Initializes the main window of the application. """
        super().__init__() # Calls the constructor of the parent class QMainWindow
        self.setWindowTitle("Student Management System")
        self.setMinimumSize(700, 600) # Sets the minimum size of the window
        self.setFixedHeight(500)
        self.setFixedWidth(500)
        # Navigation bar items
        file_menu_item = self.menuBar().addMenu("&File")
        help_menu_item = self.menuBar().addMenu("&Help")
        edit_menu_item = self.menuBar().addMenu("&Edit")

        add_student_action = QAction(QIcon("icons/add.png"), "Add Student", self)
        add_student_action.triggered.connect(self.insert_student)
        file_menu_item.addAction(add_student_action)

        about_action = QAction("About", self)
        help_menu_item.addAction(about_action)
        about_action.setMenuRole(QAction.MenuRole.NoRole) # Allows help menu to be displayed on MacOS
        about_action.triggered.connect(self.about)

        search_student_action = QAction(QIcon("icons/search.png"),"Edit", self)
        search_student_action.triggered.connect(self.edit_student)
        edit_menu_item.addAction(search_student_action)

        # Create the table
        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(("ID", "Name", "Course", "Mobile Number"))
        self.table.verticalHeader().setVisible(False) # Hides the vertical header
        self.setCentralWidget(self.table) # Allows the table to be displayed in the main window

        # Toolbar and toolbar items
        toolbar = QToolBar()
        toolbar.setMovable(True)
        self.addToolBar(toolbar)

        toolbar.addAction(add_student_action)
        toolbar.addAction(search_student_action)

        # Status bar and status bar items
        self.status_bar = QStatusBar()
        self.setStatusBar(self.status_bar)

        self.table.cellClicked.connect(self.cell_clicked)

    def cell_clicked(self):
        """ Displays the edit and delete buttons in the status bar when a cell is clicked. """
        edit_button = QPushButton("Edit Student Record")
        edit_button.clicked.connect(self.edit_record)

        delete_button = QPushButton("Delete Student Record")
        delete_button.clicked.connect(self.delete_record)

        # Clears the previous buttons if another cell is clicked
        children = self.findChildren(QPushButton)
        if children:
            for child in children:
                self.status_bar.removeWidget(child)

        self.status_bar.addWidget(edit_button)
        self.status_bar.addWidget(delete_button)

    def load_data(self):
        """ Loads the student data from the database and displays it in the table. """
        connection = DatabaseConnection().connect()
        result = connection.execute("SELECT * FROM students")
        self.table.setRowCount(0) # Makes sure new data does not duplicate the old data
        
        for row_number, row_data in enumerate(result):
            self.table.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.table.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        connection.close()

    def insert_student(self):
        """ Opens the dialog to add a new student. """
        dialog = InsertDialog()
        dialog.exec()
    
    def edit_student(self):
        """ Opens the dialog to edit an existing student. """
        dialog = SearchDialog()
        dialog.exec()

    def edit_record(self):
        """ Opens the dialog to edit the selected student record. """
        dialog = EditDialog()
        dialog.exec()

    def delete_record(self):
        """ Opens the dialog to delete the selected student record. """
        dialog = DeleteDialog()
        dialog.exec()
    
    def about(self):
        """ Displays the about dialog. """
        dialog = AboutDialog()
        dialog.exec()


class InsertDialog(QDialog):
    def __init__(self):
        """ Initializes the dialog to add a new student. """
        super().__init__()
        self.setWindowTitle("Add Student Data")
        self.setFixedHeight(300)
        self.setFixedWidth(300)

        # Create widgets below
        layout = QVBoxLayout()
        # Student name widget
        self.student_name = QLineEdit()
        self.student_name.setPlaceholderText("Student Name")
        layout.addWidget(self.student_name)
        # Course name combo box
        self.course_name = QComboBox()
        courses = ("Computer Science", "Mathematics", "Physics", "Chemistry", "Biology")
        self.course_name.addItems(courses)
        layout.addWidget(self.course_name)
        # Mobile number widget
        self.mobile_number = QLineEdit()
        self.mobile_number.setPlaceholderText("Mobile Number")
        layout.addWidget(self.mobile_number)
        # Submit button
        submit_button = QPushButton("Submit Information")
        submit_button.clicked.connect(self.add_student)
        layout.addWidget(submit_button)

        self.setLayout(layout)
    
    def add_student(self):
        """ Adds a new student to the database. """
        name = self.student_name.text()
        course = self.course_name.itemText(self.course_name.currentIndex())
        mobile = self.mobile_number.text()
        connection = DatabaseConnection().connect()
        cursor = connection.cursor()
        cursor.execute("INSERT INTO students (name, course, mobile) VALUES (?, ?, ?)", (name, course, mobile))

        connection.commit()
        cursor.close()
        connection.close()

        main_window.load_data()


class SearchDialog(QDialog):
    def __init__(self):
        """ Initializes the dialog to search for a student. """
        super().__init__()
        self.setWindowTitle("Search Student Data")
        self.setFixedHeight(300)
        self.setFixedWidth(300)

        # Create widgets below
        layout = QVBoxLayout()
        # Student name widget
        self.student_name = QLineEdit()
        self.student_name.setPlaceholderText("Student Name")
        layout.addWidget(self.student_name)
        # Search button
        search_button = QPushButton("Search Student")
        search_button.clicked.connect(self.search_student)
        layout.addWidget(search_button)

        self.setLayout(layout)

    def search_student(self):
        """ Searches for a student in the database. """
        name = self.student_name.text()
        connection = sqlite3.connect("database.db")
        cursor = connection.cursor()
        result = cursor.execute("SELECT * FROM students WHERE name = ?", (name,))
        row = list(result)[0]
        print(row)
        items = main_window.table.findItems(name, Qt.MatchFlag.MatchFixedString)
        for item in items:
            print(item)
            main_window.table.item(item.row(), 1).setSelected(True)

        cursor.close()
        connection.close()


class EditDialog(QDialog):
    def __init__(self):
        """ Initializes the dialog to edit an existing student. """
        super().__init__()
        self.setWindowTitle("Update Student Data")
        self.setFixedHeight(300)
        self.setFixedWidth(300)
        
        # Create widgets below
        layout = QVBoxLayout()

        # Get student name from the selected row
        index = main_window.table.currentRow()
        student_name = main_window.table.item(index, 1).text() # Fix student name to pop un window
        # Get student ID from the selected row
        self.student_id = main_window.table.item(index, 0).text()
        # Student name widget
        self.student_name = QLineEdit(student_name) # Fix student name to pop up window
        self.student_name.setPlaceholderText("Student Name")
        layout.addWidget(self.student_name)
        # Course name combo box
        course_name = main_window.table.item(index, 2).text() # Fix course name to pop up window

        self.course_name = QComboBox()
        courses = ["Computer Science", "Mathematics", "Physics", "Chemistry", "Biology", "Astronomy"]
        self.course_name.addItems(courses)
        self.course_name.setCurrentText(course_name) # Fix course name to pop up window
        layout.addWidget(self.course_name)
        # Mobile number widget
        mobile_number = main_window.table.item(index, 3).text() # Fix mobile number to pop up window

        self.mobile_number = QLineEdit(mobile_number) # Fix mobile number to pop up window
        self.mobile_number.setPlaceholderText("Mobile Number")
        layout.addWidget(self.mobile_number)
        # Submit button
        submit_button = QPushButton("Update Information")
        submit_button.clicked.connect(self.update_student)
        layout.addWidget(submit_button)

        self.setLayout(layout)
    
    def update_student(self):
        """ Updates the student information in the database. """
        connection = DatabaseConnection().connect()
        cursor = connection.cursor()
        cursor.execute("UPDATE students SET name = ?, course = ?, mobile = ? WHERE id = ?", (self.student_name.text(), self.course_name.currentText(), self.mobile_number.text(), self.student_id))

        connection.commit()
        cursor.close()
        connection.close()
        main_window.load_data()


class DeleteDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Delete Student Data")

        layout = QGridLayout()

        confirmation_message = QLabel("Are you sure you want to delete this student record?")
        yes_button = QPushButton("Yes")
        no_button = QPushButton("No")

        layout.addWidget(confirmation_message, 0, 0, 1, 2)
        layout.addWidget(yes_button, 1, 0)
        layout.addWidget(no_button, 1, 1)
        self.setLayout(layout)

        yes_button.clicked.connect(self.delete_student)

    def delete_student(self):
        # Get selected student index & ID from the selected row
        index = main_window.table.currentRow()
        student_id = main_window.table.item(index, 0).text()
        # Delete student record from the database
        connection = DatabaseConnection().connect()
        cursor = connection.cursor()
        cursor.execute("DELETE FROM students WHERE id = ?", (student_id, ))

        connection.commit()
        cursor.close()
        connection.close()
        main_window.load_data()

        self.close()

        confirmation_widget = QMessageBox()
        confirmation_widget.setWindowTitle("Confirmed Deletion")
        confirmation_widget.setText("Student record has been deleted.")
        confirmation_widget.exec()


class AboutDialog(QMessageBox):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("About")
        content = "This is a simple student management system built using PyQt6 and SQLite. It allows you to add, edit, and delete student records."
        self.setText(content)

# To run the application
app = QApplication(sys.argv)
main_window = MainWindow()
main_window.show()
main_window.load_data()
sys.exit(app.exec())