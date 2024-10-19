import sys
from PyQt6.QtWidgets import QApplication, QLabel, QWidget

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle('PyQt6 App')
window.setGeometry(100, 100, 280, 80)

label = QLabel('<h1>Hello, PyQt6!</h1>', parent=window)
label.move(60, 15)

window.show()

sys.exit(app.exec())
