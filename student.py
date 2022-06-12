from PyQt5 import QtWidgets,uic
import entry
class StudentWindow(QtWidgets.QMainWindow):
        def __init__(self):
            super(StudentWindow, self).__init__()
            uic.loadUi('Ui/loginstudent.ui', self)
            self.sbackbutton.clicked.connect(self.entry_show)
        
        def entry_show(self):
            self.inci=entry.EntryWindow()
            self.inci.show()
            self.close()
         
