import sys

# from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication
from mainwindow import MainWindow

# def slider_response(data):
#     print("slider moved to :", data)


if __name__== "__main__":
    app =QApplication(sys.argv)
    window = MainWindow(app)
    window.resize(400, 100)
    window.show()
    app.exec()






# if __name__ == "__main__":
#     window = QWidget()
#     window.resize(400, 600)
#     window.show()
#     # widget.show()

#     sys.exit(app.exec())

