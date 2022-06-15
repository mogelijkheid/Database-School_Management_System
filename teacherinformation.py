from PyQt5 import QtWidgets,uic
from PyQt5.QtWidgets import  QTableWidgetItem
import entry
import student
class TeacherWindow(QtWidgets.QMainWindow):
        def __init__(self,teacher,lessons,nolessons):
            self.teacher=teacher
            self.lessons=lessons
            self.nolessons=nolessons
            super(TeacherWindow, self).__init__()
            uic.loadUi('Ui/teacher1.ui', self)
            self.tname_label.setText(str(teacher[0][2].upper()))
            for i in range(len(lessons)):
                self.lesson_widget.setItem(i,0,QTableWidgetItem(lessons[i][1]))
                self.lesson_widget.setItem(i,1,QTableWidgetItem(lessons[i][2]))
                self.lesson_widget.setItem(i,2,QTableWidgetItem(str(lessons[i][3])))
            for i in range(len(nolessons)):
                self.lesson_combo.addItem(str(nolessons[i][1])) 
            self.show()
            