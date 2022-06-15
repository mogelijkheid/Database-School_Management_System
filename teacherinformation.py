from PyQt5 import QtWidgets,uic
from PyQt5.QtWidgets import  QTableWidgetItem
import entry
import teacherfonx
class TeacherWindow(QtWidgets.QMainWindow):
        def __init__(self,teacher,a):
            self.teacher=teacher
            self.a=a
            self.lessons,self.nolessons=self.a.teacherlesson()
            self.student=self.a.studentlist()
            super(TeacherWindow, self).__init__()
            uic.loadUi('Ui/teacher1.ui', self)
            self.tname_label.setText(str(teacher[0][2].upper()))
            for i in range(len(self.lessons)):
                self.lesson_widget.setItem(i,0,QTableWidgetItem(self.lessons[i][1]))
                self.lesson_widget.setItem(i,1,QTableWidgetItem(self.lessons[i][2]))
                self.lesson_widget.setItem(i,2,QTableWidgetItem(str(self.lessons[i][3])))
                self.lesson_combo_2.addItem(str(self.lessons[i][1])) 
                
            for i in range(len(self.student)):
                self.student_combo.addItem(str(self.student[i][1]))
                
            for i in range(len(self.nolessons)):
                self.lesson_combo.addItem(str(self.nolessons[i][1])) 
            
            # self.new_lesson=self.lesson_combo.insertItem()
            self.show()
            