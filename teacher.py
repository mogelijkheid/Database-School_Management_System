from PyQt5 import QtWidgets,uic
import entry

class TeacherWindow(QtWidgets.QMainWindow):
        def __init__(self):
            super(TeacherWindow, self).__init__()
            uic.loadUi('Ui/loginteacher.ui', self)
            self.tbackbutton.clicked.connect(self.entry_show)
        
        def entry_show(self):
            self.inci=entry.EntryWindow()
            self.inci.show()
            self.close()
         

