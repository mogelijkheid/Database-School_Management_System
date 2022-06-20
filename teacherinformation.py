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
            self.ok_button_2.clicked.connect(self.showstd3)
            self.ok_button_3.clicked.connect(self.showstd4)
            self.closebutton.clicked.connect(self.close_)
            self.add_button_2.clicked.connect(self.add_std)
            self.edit_button.clicked.connect(self.edit_std)
            self.remove_button_2.clicked.connect(self.remove_)
            self.remove_button.clicked.connect(self.remove_std)
            self.add_button.clicked.connect(self.add_)
            self.tname_label.setText(str(self.teacher[0][2].upper()))
            self.shwlesson()
            self.show()
        
        def add_(self):
            self.lesson=self.lesson_combo.currentText()
            self.a.addlesson(self.lesson)
            self.lessons,self.nolessons=self.a.teacherlesson()
            self.shwlesson()
            
        def remove_(self):
            self.lesson=self.lesson_combo_6.currentText()
            self.a.delete_(self.lesson)
            self.lessons,self.nolessons=self.a.teacherlesson()
            self.shwlesson()
            
        def shwlesson(self):
            self.lesson_widget.clear()
            self.lesson_combo.clear()
            self.lesson_combo_6.clear()
            self.lesson_combo_2.clear()
            self.lesson_combo_4.clear()
            self.lesson_combo_5.clear()
            for i in range(len(self.lessons)):
                self.lesson_widget.setItem(i,0,QTableWidgetItem(self.lessons[i][1]))
                self.lesson_widget.setItem(i,1,QTableWidgetItem(self.lessons[i][2]))
                self.lesson_widget.setItem(i,2,QTableWidgetItem(str(self.lessons[i][3])))
                self.lesson_combo_6.addItem(str(self.lessons[i][1])) 
                self.lesson_combo_2.addItem(str(self.lessons[i][1]))
                self.lesson_combo_4.addItem(str(self.lessons[i][1]))
                self.lesson_combo_5.addItem(str(self.lessons[i][1]))
            
            for i in range(len(self.nolessons)):
                self.lesson_combo.addItem(str(self.nolessons[i][1])) 
                
                
                
                
        def showstd(self):
            self.student_combo.clear()
            self.lesson=self.lesson_combo_2.currentText()
            self.student= self.a.studentlist(self.lesson)
            for i in range(len(self.student)):
                self.student_combo.addItem(str(self.student[i][1]))
            self.show_button.clicked.connect(self.showstd2)
            
        def showstd2(self):
            self.studentname=self.student_combo.currentText()
            for i in range(len(self.student)):
                if self.student[i][1]==self.studentname:
                    self.std=i
                    break;
            self.grades=self.a.shwgrades(self.lesson,self.studentname)
            self.name.setText(str(self.student[self.std][1].upper())+" "+str(self.student[self.std][2].upper()))
            self.gender.setText(str(self.student[self.std][4]))
            self.birth.setText(str(self.student[self.std][3]))
            self.midterm.setText(str(self.grades[0][0]))
            self.final_2.setText(str(self.grades[0][1]))
            self.attendance.setText(str(self.grades[0][2]))
            
        def showstd3(self):
            self.student_combo_4.clear()
            self.lesson=self.lesson_combo_5.currentText()
            self.student= self.a.studentlist(self.lesson)
            for i in range(len(self.student)):
                self.student_combo_4.addItem(str(self.student[i][1]))
        def remove_std(self):
            self.lesson=self.lesson_combo_5.currentText()
            self.student=self.student_combo_4.currentText()
            self.a.removestd(self.lesson,self.student)
            self.student= self.a.studentlist(self.lesson)
            self.shwlesson()
            self.showstd3()
        def showstd4(self):
            self.student_combo_3.clear()
            self.lesson=self.lesson_combo_4.currentText()
            self.nostudent= self.a.nostudentlist(self.lesson)
            for i in range(len(self.nostudent)):
                self.student_combo_3.addItem(str(self.nostudent[i][1]))
                
        def add_std(self):
            self.lesson=self.lesson_combo_4.currentText()
            self.student=self.student_combo_3.currentText()
            self.a.addstd(self.lesson,self.student)
            self.student= self.a.studentlist(self.lesson)
            self.shwlesson()
            self.showstd4()
        def edit_std(self):
            self.student=self.student_combo.currentText()
            self.midterm_=self.midterm.text()
            self.final_=self.final_2.text()
            self.attendance_=self.attendance.text()
            self.a.editstd(self.student,self.midterm_,self.final_,self.attendance_)
            self.student= self.a.studentlist(self.lesson)
            self.showstd2()
        def close_(self):
            self.a.close_()
            self.close()
            
            
            
            
         
            
            
        
            