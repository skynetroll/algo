#создай приложение для запоминания информации
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget,QApplication,QLabel,QPushButton,QVBoxLayout,QHBoxLayout,QGroupBox,QRadioButton,QPushButton,QButtonGroup
from random import shuffle

app = QApplication([])
main_win = QWidget()
main_win.calk = - 1
main_win.resize(400,200)
main_win.setWindowTitle('Кто хочет стать триллионером?')

Glabel = QLabel('Какой национальности не существует?')
Plabel = QLabel('Самый сложный вопрос в мире!')


RGB = QGroupBox('Варианты ответов')
rbtn_1 = QRadioButton()
rbtn_2 = QRadioButton()
rbtn_3 = QRadioButton()
rbtn_4 = QRadioButton()
rbtn_5 = QRadioButton()
rbtn_6 = QRadioButton()

layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()

layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)
layout_ans2.addWidget(rbtn_5)
layout_ans3.addWidget(rbtn_6)
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

PGB = QGroupBox('Результат теста')
layout_ansp = QVBoxLayout()
#layout_ansp.addStretch(1)
nextp1 = QLabel('Правильно/Неправильно')
nextp2 = QLabel('Правильный ответ')
#layout_ansp.addStretch(1)
layout_ansp.addWidget(nextp1, alignment = Qt.AlignLeft)
#layout_ansp.addStretch(1)
layout_ansp.addWidget(nextp2, alignment = Qt.AlignCenter)
#layout_ansp.addStretch(1)
PGB.setLayout(layout_ansp)
layout_ansp.addStretch(1)
layout_ansp.setSpacing(10)
nextp = QPushButton('Следующий вопрос')

RGB.setLayout(layout_ans1)

ass = QPushButton('Ответить')

RGroup = QButtonGroup()
RGroup.addButton(rbtn_1)
RGroup.addButton(rbtn_2)
RGroup.addButton(rbtn_3)
RGroup.addButton(rbtn_4)
RGroup.addButton(rbtn_5)
RGroup.addButton(rbtn_6)

class Question():
    def __init__(self,right_anwser,rbtn_1,rbtn_2,rbtn_3,rbtn_4,rbtn_5,RGB):
        self.rbtn_1 = rbtn_1
        self.rbtn_2 = rbtn_2
        self.rbtn_3 = rbtn_3
        self.rbtn_4 = rbtn_4
        self.rbtn_5 = rbtn_5
        self.RGB = RGB
        self.right_anwser = right_anwser

q_list = []
q = Question('993','я умер','69','666','994','а сколько надо?','1000 - 7 =')
q_list.append(q)

def sasi():
    Glabel.hide()
    PGB.hide()
    ass.show()
    Plabel.show()
    RGB.show()
    nextp.hide()
    RGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    rbtn_5.setChecked(False)
    rbtn_6.setChecked(False)
    RGroup.setExclusive(True)


def nehochy():
    Glabel.show()
    PGB.show()
    ass.hide()
    Plabel.hide()
    RGB.hide()
    nextp.show()

anw = [rbtn_1, rbtn_2, rbtn_3, rbtn_4, rbtn_5, rbtn_6]

def ask(q: Question):
    shuffle(anw)
    anw[0].setText(q.right_anwser)
    anw[1].setText(q.rbtn_1)
    anw[2].setText(q.rbtn_2)
    anw[3].setText(q.rbtn_3)
    anw[4].setText(q.rbtn_4)
    anw[5].setText(q.rbtn_5)

    Plabel.setText(q.RGB)
    nextp2.setText(q.right_anwser)
    sasi()

def sh_cor(res):
    nextp1.setText(res)
    nehochy()

def ch_anw():
    if anw[0].isChecked():
        sh_cor('Правильно')
    else:
        if anw[1].isChecked() or anw[2].isChecked() or anw[3].isChecked():
            sh_cor('Неверно')
def next_question():
    print('it works')
    main_win.calk += 1
    if main_win.calk >= len(q_list):
        main_win.calk = 0
    ask(q_list[main_win.calk])





gv_line = QVBoxLayout()
layout_ansp = QVBoxLayout()
layout_ansp.addStretch(1)
gv_line.addWidget(Plabel, alignment = Qt.AlignCenter)
gv_line.addWidget(Glabel, alignment = Qt.AlignCenter)
gv_line.addWidget(PGB)
gv_line.addWidget(RGB)
gv_line.addWidget(nextp, alignment = Qt.AlignCenter)
gv_line.addWidget(ass, alignment = Qt.AlignCenter)
gv_line.setSpacing(10)
nextp.hide()
main_win.setLayout(gv_line)
PGB.hide()
RGB.show()
ass.clicked.connect(ch_anw)
nextp.clicked.connect(next_question)
next_question()
main_win.show()
app.exec_()
