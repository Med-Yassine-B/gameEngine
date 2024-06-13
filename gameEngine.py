import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QWidget,QDesktopWidget,QLabel,QVBoxLayout,QHBoxLayout


class RightWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-color: #808080;")
        self.ui_init()
    

    def ui_init(self):
        main_layout=QHBoxLayout()
        
       
        self.lable=QLabel()
        self.lable.setText("text text")
        main_layout.addWidget(self.lable)

        self.setLayout(main_layout)
        pass

class MiddelWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.ui_init()
        self.setStyleSheet("background-color: red;")


    def ui_init(self):
        main_layout=QHBoxLayout()
       
        self.lable=QLabel()
        self.lable.setText("text text")
        main_layout.addWidget(self.lable)

        self.setLayout(main_layout)
        # self.

class LeftWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.ui_init()
        self.setStyleSheet("background-color: gray;")


    def ui_init(self):
        main_layout=QHBoxLayout()
       
        self.lable=QLabel()
        self.lable.setText("text text")
        main_layout.addWidget(self.lable)

        self.setLayout(main_layout)
        pass


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("gameEngine")
        self.resize_and_center(0.7)
        self.ui_init()
        self.setStyleSheet("background-color:black")

    def ui_init(self):
        main_widget=QWidget()
        layout=QHBoxLayout()
        widgets=[LeftWidget(),MiddelWidget(),RightWidget()]

        for widget in widgets:
            layout.addWidget(widget)
            layout.setStretchFactor(widget,1)
            
        layout.setStretchFactor(widgets[1],3)
        
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
    pass


if __name__=='__main__':
    app=QApplication(sys.argv)

    window=Window()
    window.show()
    sys.exit(app.exec_())