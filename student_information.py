from PyQt5 import QtWidgets,uic
from PyQt5.QtWidgets import  QTableWidgetItem
import entry
import student
class StudentWindow(QtWidgets.QMainWindow):
        def __init__(self,student,lessons,grades):
            self.student=student
            self.lessons=lessons
            self.grades=grades
            super(StudentWindow, self).__init__()
            uic.loadUi('Ui/student.ui', self)
            self.back_button.clicked.connect(self.backmenu)
            self.number_label.setText(str(student[0][0]))
            self.name_label.setText(str(student[0][1].upper()))
            self.surname_label.setText(str(student[0][2].upper()))
            self.birth_label.setText(str(student[0][3]))
            self.gender_label.setText(str(student[0][4]).upper())
            for i in range(len(lessons)):
                self.term_widget.setItem(i,0,QTableWidgetItem(lessons[i][0]))
            for i in range(len(grades)):
                self.term_widget.setItem(i,1,QTableWidgetItem(str(grades[i][0])))
                self.term_widget.setItem(i,2,QTableWidgetItem(str(grades[i][1])))
            
            self.show()
            
        def backmenu(self):
            self.inci=entry.EntryWindow()
            self.inci.show()
            self.close()
            
