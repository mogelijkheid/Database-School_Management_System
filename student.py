from PyQt5 import QtWidgets,uic

class StudentWindow(QtWidgets.QMainWindow):
        def __init__(self):
            super(StudentWindow, self).__init__()
            uic.loadUi('Ui/student.ui', self)
