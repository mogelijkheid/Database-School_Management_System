from PyQt5 import QtWidgets,uic
import entry
import student_information
import fonx
class StudentWindow(QtWidgets.QMainWindow):
        def __init__(self):
            super(StudentWindow, self).__init__()
            uic.loadUi('Ui/loginstudent.ui', self)
            self.sbackbutton.clicked.connect(self.entry_show)
            self.sloginbutton.clicked.connect(self.student_show)
        
        def entry_show(self):
            self.inci=entry.EntryWindow()
            self.inci.show()
            self.close()
            
        def student_show (self):        
            self.student_number=self.snumberline.text()
            self.password=self.spasswordline.text()
            a=fonx.data()
            self.student=a.studentlogin(self.student_number,self.password)
            if self.student==[]:
                 self.message.setText("Password or UserName is wrong")
            else:
                self.inci=student_information.StudentWindow(self.student)   
                self.inci.show()
                self.close()
