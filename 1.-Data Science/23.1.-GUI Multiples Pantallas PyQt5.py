import sys
from PyQt5 import QtWidgets, QtGui, QtCore

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Time Zone Selector")
        self.setGeometry(100, 100, 800, 600)
        self.open_windows = []  # List to hold references to opened windows

        self.create_widgets()
        
    def create_widgets(self):
        # Logo
        logo_label = QtWidgets.QLabel()
        iconPath = "C:/Users/diego/OneDrive/Documents/The_MechaBible/p_Python_ESP/1.-Data Science/0.-Archivos_Ejercicios_Python/Img/IconoBlancoDi_cer0.png"
        pixmap = QtGui.QPixmap(iconPath)
        # Resize the image
        pixmap = pixmap.scaled(50, 50, QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
        logo_label.setPixmap(pixmap)
        
        # Text in the middle
        text_label = QtWidgets.QLabel("Select Time Zone:")
        
        # ComboBox for time zones
        self.timezones_combo = QtWidgets.QComboBox()
        self.timezones_combo.addItems(["GMT", "UTC", "CET", "PST", "EST"])
        
        # Container for squares
        self.container_layout = QtWidgets.QHBoxLayout()
        self.container_layout.addWidget(self.create_square("Square 1", "This is square 1", "Create 1"))
        self.container_layout.addWidget(self.create_square("Square 2", "This is square 2", "Create 2"))
        
        # Main layout
        main_layout = QtWidgets.QVBoxLayout()
        
        # Create a widget to contain the menu items
        menu_widget = QtWidgets.QWidget()
        menu_layout = QtWidgets.QHBoxLayout(menu_widget)
        menu_layout.addWidget(logo_label)
        menu_layout.addWidget(text_label)
        menu_layout.addWidget(self.timezones_combo)
        
        # Set fixed height for the menu widget
        menu_widget.setFixedHeight(100)
        
        # Apply the background color to the menu widget
        menu_widget.setStyleSheet("background-color: blue;")
        
        main_layout.addWidget(menu_widget)
        main_layout.addStretch()  # Add stretch to push the next widget to the top
        
        # Create a light gray container widget
        light_gray_container = QtWidgets.QWidget()
        light_gray_container.setStyleSheet("background-color: lightgray;")
        light_gray_layout = QtWidgets.QVBoxLayout(light_gray_container)
        light_gray_layout.addStretch()  # Add stretch to push content to the middle
        light_gray_layout.addLayout(self.container_layout)
        light_gray_layout.addStretch()  # Add stretch to push content to the middle
        
        main_layout.addWidget(light_gray_container)
        main_layout.addStretch()  # Add stretch to push content to the middle
        
        central_widget = QtWidgets.QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)
        
    def create_square(self, name, text, button_text):
        square = QtWidgets.QFrame()
        square.setFrameShape(QtWidgets.QFrame.StyledPanel)
        square.setFixedSize(200, 200)
        square.setStyleSheet("background-color: darkgray;")
        square.mousePressEvent = lambda event: self.open_window(name)
        
        # Add layout to square
        layout = QtWidgets.QVBoxLayout()
        square.setLayout(layout)
        
        # Text label
        text_label = QtWidgets.QLabel(text)
        layout.addWidget(text_label)
        
        # Button
        create_button = QtWidgets.QPushButton(button_text)
        create_button.clicked.connect(lambda: self.open_window(f"{name} Window", name))
        layout.addWidget(create_button)
        
        return square
    
    def open_window(self, name, window_number):
        window = QtWidgets.QWidget()
        window.setWindowTitle(name)
        window.setGeometry(200, 200, 400, 300)
        
        # Top container with blue background color
        top_container = QtWidgets.QWidget()
        top_container.setStyleSheet("background-color: blue;")
        
        # Below container with gray background color
        below_container = QtWidgets.QWidget()
        below_container.setStyleSheet("background-color: lightgray;")
        
        # Add text labels and buttons to the below container
        text_label1 = QtWidgets.QLabel("This is line 1.")
        text_label2 = QtWidgets.QLabel("This is line 2.")
        
        confirm_button = QtWidgets.QPushButton("Confirm")
        return_button = QtWidgets.QPushButton("Return")
        
        button_layout = QtWidgets.QHBoxLayout()
        button_layout.addWidget(confirm_button)
        button_layout.addWidget(return_button)
        
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(text_label1)
        layout.addWidget(text_label2)
        layout.addLayout(button_layout)
        below_container.setLayout(layout)
        
        # Add top and below containers to the window
        window_layout = QtWidgets.QVBoxLayout()
        window_layout.addWidget(top_container)
        window_layout.addWidget(below_container)
        
        window.setLayout(window_layout)
        
        confirm_button.clicked.connect(lambda: print(f"Confirm button clicked in Window {window_number}"))
        return_button.clicked.connect(window.close)
        
        window.show()
        
        # Keep a reference to the opened window
        self.open_windows.append(window)
        
    def timezone_changed(self, index):
        timezone = self.timezones_combo.currentText()
        print("Selected Time Zone:", timezone)
        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())