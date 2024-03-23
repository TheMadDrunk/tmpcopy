from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QGroupBox, QVBoxLayout, QRadioButton, QHBoxLayout

app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('Card Game')

RadioGroupBox = QGroupBox("Answer options")
rbtn_1 = QRadioButton('Enets')
rbtn_2 = QRadioButton('Smurfs')
rbtn_3 = QRadioButton('Chulyms')
rbtn_4 = QRadioButton('Aleuts')
layouth1 = QHBoxLayout()   
layouth2 = QHBoxLayout()   

layouth1.addWidget(rbtn_1)
layouth1.addWidget(rbtn_2)
layouth2.addWidget(rbtn_3)
layouth2.addWidget(rbtn_4)

layoutv1 = QVBoxLayout()
layoutv1.addLayout(layouth1)
layoutv1.addLayout(layouth2)

RadioGroupBox.setLayout(layoutv1)

mainlayout = QVBoxLayout()

main_win.setLayout(mainlayout)
mainlayout.addWidget(RadioGroupBox)

main_win.show()
app.exec_()
