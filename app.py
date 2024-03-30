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
nextbtn = QPushButton('Next')
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
mainlayout.addWidget(nextbtn, alignment= Qt.AlignCenter)
main_win.setLayout(mainlayout)

answervalue = ""

answerResultGroup.hide()
nextbtn.hide()

def setAnswerValue():
    global answervalue
    if(rbtn_1.isChecked()):
        answervalue = rbtn_1.text()
        rbtn_1.setChecked(False)
    elif(rbtn_2.isChecked()):
        answervalue = rbtn_2.text()
        rbtn_2.setChecked(False)
    elif(rbtn_3.isChecked()):
        answervalue = rbtn_3.text()
        rbtn_3.setChecked(False)
    elif(rbtn_4.isChecked()):
        answervalue = rbtn_4.text()
        rbtn_4.setChecked(False)


def checkAnswer():
    global answervalue
    setAnswerValue()

    if(answervalue == "Smurfs"):
        result.setText("You answer is CORRECT")
    else:
        result.setText("You answer is WRONG")

    answerResultGroup.show()
    nextbtn.show()

    RadioGroupBox.hide()
    answerbtn.hide()



answerbtn.clicked.connect(checkAnswer)

def nextQuestion():
    answerResultGroup.hide()
    nextbtn.hide()

    RadioGroupBox.show()
    answerbtn.show()
    

nextbtn.clicked.connect(nextQuestion)


main_win.show()
app.exec_()
