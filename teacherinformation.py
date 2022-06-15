from PyQt5 import QtWidgets,uic
from PyQt5.QtWidgets import  QTableWidgetItem
import entry
import teacherfonx
class TeacherWindow(QtWidgets.QMainWindow):
        def __init__(self,teacher,a):
            self.teacher=teacher
            self.a=a
            self.lessons,self.nolessons=self.a.teacherlesson()
            
            super(TeacherWindow, self).__init__()
            uic.loadUi('Ui/teacher1.ui', self)
            self.ok_button.clicked.connect(self.showstd)
            self.tname_label.setText(str(self.teacher[0][2].upper()))
            for i in range(len(self.lessons)):
                self.lesson_widget.setItem(i,0,QTableWidgetItem(self.lessons[i][1]))
                self.lesson_widget.setItem(i,1,QTableWidgetItem(self.lessons[i][2]))
                self.lesson_widget.setItem(i,2,QTableWidgetItem(str(self.lessons[i][3])))
                self.lesson_combo_2.addItem(str(self.lessons[i][1])) 
             
            for i in range(len(self.nolessons)):
                self.lesson_combo.addItem(str(self.nolessons[i][1])) 
            self.show()
        
            
        def showstd(self):
            self.student_combo.clear()
            self.lesson=self.lesson_combo_2.currentText()
            self.student= self.a.studentlist(self.lesson)
            for i in range(len(self.student)):
                self.student_combo.addItem(str(self.student[i][1]))
            self.show_button.clicked.connect(self.showstd2)
            
        def showstd2(self):
            self.name.setText(str(self.student[0][1].upper())+" "+str(self.student[0][2].upper()))
            self.gender.setText(str(self.student[0][4]))
            self.birth.setText(str(self.student[0][3]))
            
            
         
            
            
        
            