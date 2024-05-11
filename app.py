from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget,  QVBoxLayout, QTextEdit, QPushButton

MyApp = QApplication([])

MainWin = QWidget()

mainLayout = QVBoxLayout()

MainWin.setLayout(mainLayout)

fileContent = ""

with open("file.txt","r") as readingFile:
    fileContent = readingFile.read()

textEdit = QTextEdit(fileContent)
saveButton =QPushButton("Save")

def onClickSave():
    global textEdit
    with open("file.txt",'w') as file:
        file.write(textEdit.toPlainText())

mainLayout.addWidget(textEdit,alignment=Qt.AlignCenter)
mainLayout.addWidget(saveButton,alignment=Qt.AlignCenter)

saveButton.clicked.connect(onClickSave)


MainWin.show()
MyApp.exec_()

myNotes = {
    "todos":"my_todos.txt"
}

# find a widget that allows the user to write text -> QTextEdit
# create a GUI using that widget 
# crete a button that saves the text to a file 
