from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
Form, Window = uic.loadUiType("uibd.ui")
app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)
window.show()
app.exec_()