from PyQt5 import QtWidgets,uic

class TeacherWindow(QtWidgets.QMainWindow):
        def __init__(self):
            super(TeacherWindow, self).__init__()
            uic.loadUi('Ui/teacher.ui', self)