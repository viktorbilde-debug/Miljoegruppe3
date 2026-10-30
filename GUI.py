import sys
from PySide6.QtWidgets import (QLineEdit, QPushButton, QApplication,
    QVBoxLayout, QDialog)
import requests


class window(QDialog):

 
 def __init__(self, parent=None):
        super(window, self).__init__(parent)
        # Create widgets
        
        self.button1 = QPushButton("humidity")
        self.button2 = QPushButton("temp_dry")
        self.button3 = QPushButton ("pressure")
        # Create layout and add widgets
        layout = QVBoxLayout()
        layout.addWidget(self.button1)
        layout.addWidget(self.button2)
        layout.addWidget(self.button3)
        # Set dialog layout
        self.setLayout(layout)
        # Add button signal to greetings slot
        
        self.button1.clicked.connect(self.extract_from_API_H)
        self.button3.clicked.connect(self.extract_from_API_p)
        self.button2.clicked.connect(self.extract_from_API_t)
 
 def extract_from_API_H(self):
    response = requests.get("http://127.0.0.1:8000/?table_name=humidity&num_obs=4&source=DMI")
    if not response.ok:  ### Returns false if response error is 400+
        return "Failed API response"
    extracted_data = response.json()
    print(f"humidity: {extracted_data}")

 def extract_from_API_t(self):
    response = requests.get("http://127.0.0.1:8000/?table_name=temp_dry&num_obs=4&source=DMI")
    if not response.ok:  ### Returns false if response error is 400+
        return "Failed API response"
    extracted_data = response.json()
    print(f"temp_dry: {extracted_data}")
 def extract_from_API_p(self):
    response = requests.get("http://127.0.0.1:8000/?table_name=pressure&num_obs=4&source=DMI")
    if not response.ok:  ### Returns false if response error is 400+
        return "Failed API response"
    extracted_data = response.json()
    print(f"pressure: {extracted_data}")


if __name__ == '__main__':
    # Create the Qt Application
    app = QApplication(sys.argv)
    # Create and show the form
    form = window()
    form.show()
    # Run the main Qt loop
    sys.exit(app.exec())
