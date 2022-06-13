from PyQt5 import QtWidgets,uic
import entry
import student
class StudentWindow(QtWidgets.QMainWindow):
        def __init__(self,student):
            self.student=student
            super(StudentWindow, self).__init__()
            uic.loadUi('Ui/student.ui', self)
            self.number_label.setText(str(student[0][0]))
            self.name_label.setText(str(student[0][1].upper()))
            self.surname_label.setText(str(student[0][2].upper()))
            self.birth_label.setText(str(student[0][3]))
            self.gender_label.setText(str(student[0][4]).upper())
            self.show()
            
