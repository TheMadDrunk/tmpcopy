from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QGroupBox, QVBoxLayout, QRadioButton, QHBoxLayout, QPushButton, QLabel

app = QApplication([])

# widgets
main_win = QWidget()
RadioGroupBox = QGroupBox("Answer options")
rbtn_1 = QRadioButton('Enets')
rbtn_2 = QRadioButton('Smurfs')
rbtn_3 = QRadioButton('Chulyms')
rbtn_4 = QRadioButton('Aleuts')
answerbtn = QPushButton('Answer')
question = QLabel("this is a question ?")
  
# layouts
layouth1 = QHBoxLayout()   
layouth2 = QHBoxLayout() 
layoutv1 = QVBoxLayout()
mainlayout = QVBoxLayout()

# answer group component
layouth1.addWidget(rbtn_1)
layouth1.addWidget(rbtn_2)
layouth2.addWidget(rbtn_3)
layouth2.addWidget(rbtn_4)
layoutv1.addLayout(layouth1)
layoutv1.addLayout(layouth2)
RadioGroupBox.setLayout(layoutv1)

# answer result component
answerResultGroup = QGroupBox("Test Result")
answerGroupLayout = QVBoxLayout()
result = QLabel("You answer is")
answerGroupLayout.addWidget(result, alignment=Qt.AlignCenter)
answerResultGroup.setLayout(answerGroupLayout)


# main window
main_win.setWindowTitle('Card Game')
mainlayout.addWidget(question,alignment=Qt.AlignCenter)
mainlayout.addWidget(RadioGroupBox,alignment=Qt.AlignCenter)
mainlayout.addWidget(answerResultGroup)
mainlayout.addWidget(answerbtn,alignment=Qt.AlignCenter)
main_win.setLayout(mainlayout)

main_win.show()
app.exec_()
