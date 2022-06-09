from entry import EntryWindow
from PyQt5 import QtWidgets
import sys

app = QtWidgets.QApplication(sys.argv)
window = EntryWindow()
app.exec_()