from PyQt6 import QtWidgets, uic
import sys

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        # завантажуємо перший файл з інтерфейсом
        uic.loadUi('page1.ui', self)
        self.pushButton_page2.clicked.connect(self.show_page2)

    def show_page2(self):
        # завантажуємо другий файл з інтерфейсом
        uic.loadUi('page2.ui', self)
        self.pushButton_page1.clicked.connect(self.show_page1)

    def show_page1(self):
        # завантажуємо перший файл з інтерфейсом
        uic.loadUi('page1.ui', self)
        self.pushButton_page2.clicked.connect(self.show_page2)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
