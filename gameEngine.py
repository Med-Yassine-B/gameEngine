import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QDesktopWidget, QLabel, QVBoxLayout, QHBoxLayout,QPushButton
import subprocess
import os

class RightWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-color: #808080;")
        self.ui_init()
    
    def ui_init(self):
        main_layout = QHBoxLayout()
        main_layout.setSpacing(0)  # Set spacing to 0
        main_layout.setContentsMargins(0, 0, 0, 0)  # Set margins to 0
        
        self.label = QLabel()
        self.label.setText("text text")
        main_layout.addWidget(self.label)

        self.setLayout(main_layout)


class MiddleWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.ui_init()
        self.setStyleSheet("background-color: red;")
        self.functions()

    def ui_init(self):
        main_layout = QHBoxLayout()
        main_layout.setSpacing(0)  # Set spacing to 0
        #main_layout.setContentsMargins(5, 0, 5, 0)  # Set margins to 0
        
        self.runButton=QPushButton("run",self)
        main_layout.addWidget(self.runButton)

        self.setLayout(main_layout)

    def functions(self):
        self.runButton.clicked.connect(self.runGame)
    
    def runGame(self):
        print("running the game...")
        subprocess.Popen("g++ src\\main.cpp -o bin\\game.exe -I src\\include -L src\\lib -lmingw32 -lSDL2main -lSDL2")
        subprocess.Popen("bin\\game.exe")
    def open_file(self,file):
        os.startfile(file)
        

class LeftWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.ui_init()
        self.setStyleSheet("background-color: gray;")

    def ui_init(self):
        main_layout = QHBoxLayout()
        main_layout.setSpacing(0)  # Set spacing to 0
        main_layout.setContentsMargins(0, 0, 0, 0)  # Set margins to 0
        
        self.label = QLabel()
        self.label.setText("text text")
        main_layout.addWidget(self.label)

        self.setLayout(main_layout)


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("gameEngine")
        self.ui_init()
        self.setStyleSheet("background-color:black")
        self.resize_and_center(0.7)

    def ui_init(self):
        main_widget = QWidget()
        layout = QHBoxLayout()
        layout.setSpacing(0)  # Set spacing to 0
        layout.setContentsMargins(0, 0, 0, 0)  # Set margins to 0
        widgets = [LeftWidget(), MiddleWidget(), RightWidget()]

        for widget in widgets:
            layout.addWidget(widget)
            layout.setStretchFactor(widget, 1)
            
        layout.setStretchFactor(widgets[1], 3)
        
        main_widget.setLayout(layout)
        self.setCentralWidget(main_widget)

    def resize_and_center(self, percent: float):
        screen = QDesktopWidget().screenGeometry()
        width = int(screen.width() * percent)
        height = int(screen.height() * percent)
        self.setGeometry(
            (screen.width() - width) // 2,
            (screen.height() - height) // 2,
            width,
            height
        )


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = Window()
    window.show()
    sys.exit(app.exec_())
