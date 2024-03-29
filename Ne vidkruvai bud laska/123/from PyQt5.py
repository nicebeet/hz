import json
from PyQt5.QtCore import Qt 
from PyQt5.QtWidgets import (
        QApplication,QWidget,QListWidget,QLineEdit,
        QHBoxLayout,QVBoxLayout,
        QPushButton,QLabel,QTextEdit,QInputDialog)
app = QApplication([])
win = QWidget()
win.setWindowTitle("Розумні підказки")
win.resize(900,600)

notes = {
    "Ласкаво просимо":{
        "текст":"Це найкращий додаток для заміток у світі",
        "теги":["добро","інструкція"]
    }
}

text = QTextEdit()

with open("notes_data.json","w")as file:
    json.dump(notes,file )

name_list1 = QLabel("Список заміток")
list_notes = QListWidget()

but1 = QPushButton("Створити замітку")
but2 = QPushButton("Видалити замітку")
but3 = QPushButton("Зберегти")

name_list2 = QLabel("Список тегів")
list_tag = QListWidget()

edit_tag = QLineEdit('')
edit_tag.setPlaceholderText("Введіть тег")

but4 = QPushButton("Додати до замітки")
but5 = QPushButton("Відкріпити від замітки")
but6 = QPushButton("Шукати замітки по тегу")

lineH = QHBoxLayout()
lineH1 = QHBoxLayout()
lineH2 = QHBoxLayout()

lineV2 = QVBoxLayout()
lineV1 = QVBoxLayout()

lineV1.addWidget(text)
lineV2.addWidget(name_list1)
lineV2.addWidget(list_notes)

lineH1.addWidget(but1)
lineH1.addWidget(but2)
lineV2.addWidget(but3)
lineV2.addLayout(lineH1)

lineV2.addWidget(name_list2)
lineV2.addWidget(list_tag)
lineV2.addWidget(edit_tag)

lineH2.addWidget(but4)
lineH2.addWidget(but5)
lineV2.addLayout(lineH2)

lineV2.addWidget(but6)

lineH.addLayout(lineV1,stretch=2)
lineH.addLayout(lineV2,stretch=1)

win.setLayout(lineH)

def show():
    key = list_notes.selectedItems()[0].text()
    print(key)
    text.setText(notes[key]["текст"]) 
    list_tag.clear()
    list_tag.addItems(notes[key]["теги"])

def add_note():
    note_name, ok = QInputDialog.getText(win,"Додати замітку","Nazva zamitki:")
    if ok and note_name != "":
        notes[note_name] = {"текст":"","теги" : []}
        list_notes.addItem(note_name)
        list_tag.addItem(notes[note_name]["теги"])
        print(notes)

def del_tag():
    if list_tag.selectedItems()[0].text():
        key = list_notes.selectedItems()[0].text()
        tag = list_tag.selectedItems()[0].text()
        notes[key]["теги"].remove(tag)
        list_tag.clear()
        list_tag.addItems(notes[key]["теги"])
        with open("notes_data.json","w") as file:
            json.dump(notes,file,sort_keys=True, ensure_ascii=False)
    else:
        print("Тег для вилучення не обраний")


def del_note():
    if list_notes.selectedItems()[0].text():
        key =  list_notes.selectedItems()[0].text()
        del notes[key]
        list_notes.clear()
        list_tag.clear()
        text.clear()
        list_notes.addItem(notes)
        with open("notes_data.json","w") as file:
            json.dump(notes,file,sort_keys=True,ensure_ascii=False)
        print(notes)
    else:
        print("Замітка для вилучення не обрана")

def save_note():
    if list_notes.selectedItems():
        key = list_notes.selectedItems()[0].text()
        notes[key]["текст"] = text.toPlainText()
        with open("otes_data.json","w") as file:
            json.dump(notes,file, sort_keys=True , ensure_ascii=False )
            print(notes)
    else:
        print("war pigs")
        

def add_tag():
    if list_notes.selectedItems():
        key = list_notes.selectedItems()[0].text()
        tag = edit_tag.text()
        if not tag in notes[key]["теги"]:
            list_tag.addItem(tag)
            edit_tag.clear()
        with open ("notes_data.json","w") as file:
            json.dump(notes,file,sort_keys=True,ensure_ascii=False)
            print(notes)
    else:
        print("kakashka")
def search_tag():
    print(but6.text())
    tag = edit_tag.text()
    if but6.text() == "Шукати замітку по тегу" and tag:
        print(tag)
        notes_f = {}
        for note in notes:
            notes_f[note] = notes[note]
        but6.setText("Вася")
        list_notes.clear()
        list_tag.clear()
        list_notes.addItem(notes_f)
        print(but6.text())
    elif but6.text() == "POPA PIPISKA KAKASHKA":
        text.clear()
        list_notes.clear()
        list_tag.clear()
        list_notes.addItem()
        but6.setText("Шукати замітку")
        print(but6.text())
    else:
        pass   

but5.clicked.connect(del_tag)
but2.clicked.connect(del_note)
but1.clicked.connect(add_note)
but3.clicked.connect(save_note)
but4.clicked.connect(add_tag)

with open("notes_data.json","r",encoding="utf-8") as file:
    notes = json.load(file)
list_notes.addItems(notes)

win.show()
app.exec_()






















































