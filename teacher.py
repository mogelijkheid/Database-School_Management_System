from PyQt5 import QtWidgets,uic
import entry
import teacherfonx
import teacherinformation

class TeacherWindow(QtWidgets.QMainWindow):
        def __init__(self):
            super(TeacherWindow, self).__init__()
            uic.loadUi('Ui/loginteacher.ui', self)
            self.tbackbutton.clicked.connect(self.entry_show)
            self.tloginbutton.clicked.connect(self.teacher_show)
        
        def entry_show(self):
            self.inci=entry.EntryWindow()
            self.inci.show()
            self.close()
            
        def teacher_show (self):        
            self.username=self.usernameline.text()
            self.password=self.tpasswordline.text()
            a=teacherfonx.teacherdata(self.username,self.password)
            self.teacher=a.teacherlogin()
            self.lessons,self.nolessons=a.teacherlesson()
            # self.grades=a.gradeshow()
            if self.teacher==[]:
                 self.message.setText("PASSWORD OR USERNAME IS WRONG")
            else:
                self.inci=teacherinformation.TeacherWindow(self.teacher,self.lessons,self.nolessons)   
                self.inci.show()
                self.close()
         

