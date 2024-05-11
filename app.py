from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QListWidgetItem, QWidget, QListWidget,  QVBoxLayout, QTextEdit, QPushButton, QHBoxLayout

MyApp = QApplication([])

MainWin = QWidget()

mainLayout = QHBoxLayout()
letfLayout = QVBoxLayout()
rightLayout = QVBoxLayout()

mainLayout.addLayout(letfLayout)
mainLayout.addLayout(rightLayout)

MainWin.setLayout(mainLayout)

fileContent = ""
try:
    with open("file.txt","r") as readingFile:
        fileContent = readingFile.read()
except:
    print("file does not exist")

textEdit = QTextEdit(fileContent)
saveButton =QPushButton("Save")

def onClickSave():
    global textEdit
    with open("file.txt",'w') as file:
        file.write(textEdit.toPlainText())

# LEFT
letfLayout.addWidget(textEdit,alignment=Qt.AlignCenter)
letfLayout.addWidget(saveButton,alignment=Qt.AlignCenter)

saveButton.clicked.connect(onClickSave)


#RIGHT
widgetList = QListWidget()
widgetList.addItem(QListWidgetItem("My Item"))
rightLayout.addWidget(widgetList)

MainWin.show()
MyApp.exec_()


# TODO :
# CREATE A DICTIONNARY WITH  KEY: note_name  VALUE: file_path
# CREATE QwitdgetItems out of the DICTIONNARY
# create files that are in that dictionnary
# open the selected files in that list
