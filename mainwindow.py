# from PySide6.QtWidgets import QMainWindow, QPushButton


# class ButtonHolder(QMainWindow):

#     def button_clicked():
#         print("You clicked the button, right?!")
    
#     def __init__ (self):
#         super().__init__()
#         self.setWindowTitle("Button Stuffs")
#         QPushButton("click me")
#         QPushButton("click me").clicked.connect(self.button_clicked)


#         # self.setCentralWidget(button)

#         # button.clicked.connect(self.button_clicked)

from PySide6.QtWidgets import QMainWindow, QToolBar
from PySide6.QtCore import QSize 
from PySide6.QtGui import QAction 

class MainWindow(QMainWindow):

    def quit_app(self):
        self.app.quit()

    def toolbar_button_click(self):
        print("action1 triggered")


    def __init__(self, app):
        super().__init__()
        self.app = app #declare an app member
        self.setWindowTitle("Custom MainWindow")

        # Menubar and menus
        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu("File")
        quit1=file_menu.addAction("Quit")
        quit1.triggered.connect(self.quit_app)

        edit_menu = menu_bar.addMenu("Edit")
        edit_menu.addAction("Copy")
        edit_menu.addAction("Cut")
        edit_menu.addAction("Paste")
        edit_menu.addAction("Undo")
        edit_menu.addAction("Redo")

        menu_bar.addMenu("Window")
        menu_bar.addMenu("Setting")
        menu_bar.addMenu("Help")

        # Working with toolbar objects
        toolbar = QToolBar("My main toolbar")
        toolbar.setIconSize(QSize(16,16))
        self.addToolBar(toolbar)

        toolbar.addAction(quit1)

        action1 = QAction("Some Action", self)
        action1.setStatusTip("Status message for some action")
        action1.triggered.connect(self.toolbar_button_click)
        toolbar.addAction(action1)

