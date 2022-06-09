from PyQt5 import QtWidgets,uic
import student
import teacher

class EntryWindow(QtWidgets.QMainWindow):
    
    def __init__(self):
        super(EntryWindow, self).__init__()
        uic.loadUi('Ui/entry.ui', self)
        self.StudentButton.clicked.connect(self.student_show)
        self.TeacherButton.clicked.connect(self.teacher_show)
        self.show()

    def student_show (self):
        self.inci=student.StudentWindow()
        self.inci.show()
        self.close()

    def teacher_show(self):
        self.inci=teacher.TeacherWindow()
        self.inci.show()
        self.close()