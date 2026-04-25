#создай приложение для запоминания информации
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget,  QPushButton,QButtonGroup, QHBoxLayout, QVBoxLayout, QLabel, QGroupBox, QMessageBox, QRadioButton)
from random import randint, shuffle #не было импорта
class Question():
    def __init__(self, question, rignt_ansver, wrong1, wrong2, wrong3):
        self.question = question
        self.rignt_ansver = rignt_ansver
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

app = QApplication([])
main_win = QWidget()

btn_OK = QPushButton('Ответить')


RadioGroupBox = QGroupBox("Варианты ответов")
rdtn_1 = QRadioButton('Энцы')
rdtn_2 = QRadioButton('Смурфы')
rdtn_3 = QRadioButton('Чулымцы')
rdtn_4 = QRadioButton('Алеуты')
layout_ans1 = QHBoxLayout()
layout_ans2 = QHBoxLayout()
layout_ans3 = QHBoxLayout()

layout_ans2.addWidget(rdtn_1)
layout_ans2.addWidget(rdtn_2)
layout_ans3.addWidget(rdtn_3)
layout_ans3.addWidget(rdtn_4)
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)
question = QLabel('Какой национальность не существует')

RadioGroupBox.setLayout(layout_ans1)

layoutH1 = QHBoxLayout()
layoutH2 = QHBoxLayout()
layoutH3 = QHBoxLayout()
layoutH1.addWidget(question, alignment = Qt.AlignCenter)
layoutH2.addWidget(RadioGroupBox)

layoutH3.addStretch(1)
layoutH3.addWidget(btn_OK)
layoutH3.addStretch(1)
layout_card = QVBoxLayout()

RadioGroup = QButtonGroup()
RadioGroup.addButton(rdtn_1)
RadioGroup.addButton(rdtn_2)
RadioGroup.addButton(rdtn_3)
RadioGroup.addButton(rdtn_4)

layout_card.addLayout(layoutH1)
layout_card.addLayout(layoutH2)
layout_card.addStretch(1)
layout_card.addLayout(layoutH3)
layout_card.addStretch(1)
layout_card.addStretch(5)

AnsGroupBox = QGroupBox("Результат текста")
lb_Result = QLabel('прав ты или нет')
lb_Correct = QLabel('ответ будет тут!')

layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter)
AnsGroupBox.setLayout(layout_res)

layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()

layout_line1.addWidget(question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layout_line2.addWidget(RadioGroupBox)
layout_line2.addWidget(AnsGroupBox)

layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK)
layout_line3.addStretch(1)
AnsGroupBox.hide()

def show_result():
    ''' показать панель ответов '''
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText('Следующий вопрос')

def show_question():
    ''' показать панель ответов '''
    RadioGroupBox.show() # ОШИБКА: должна показывать RadioGroupBox, а скрывать!
    AnsGroupBox.hide()# ОШИБКА: должна скрывать AnsGroupBox!
    btn_OK.setText('Ответить')
    RadioGroup.setExclusive(False)
    rdtn_1.setChecked(False) #setCnecked вместо setChecked
    rdtn_2.setChecked(False) #setCnecked вместо setChecked
    rdtn_3.setChecked(False) #setCnecked вместо setChecked
    rdtn_4.setChecked(False) #setCnecked вместо setChecked
    RadioGroup.setExclusive(True)

answers = [rdtn_1, rdtn_2, rdtn_3, rdtn_4]

def ask(q: Question):#аргументы
    
    shuffle(answers) 
    answers[0].setText(q.rignt_ansver)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    question.setText(q.question) #question вместо lb
    lb_Correct.setText(q.rignt_ansver)
    show_question()

questions_list = []
questions_list.append(Question('Государственный язык Бразилии', 'Португалия', 'Английский', 'Испанский', 'Бразилия'))
questions_list.append(Question('Какой цвета нет на флаге России?', 'Зелёный', 'Красный', 'Белый', 'Синий'))
questions_list.append(Question('Национальная хижина якутов', 'Ураса', 'Юрта', 'Иглу', 'Хата'))

def check_answer():
    if answers[0].isChecked():
        show_correct('Правильно!')
        main_win.score += 1
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct('Неправильно!')


           
            print('Статистика\n-Всего вопросов: ', main_win.total, '\n-Правильных ответов: ', main_win.score)#window
            print('Рейтинг: ', (main_win.score/main_win.total*100), '%')#window
        else:
            if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked:
                show_correct('Неверно!')
                print('Рейтинг: ', (main_win.score/main_win.total*100), '%') #window

def next_question(): #переделать полностью 

    main_win.total += 1
    print('Статистика\n-Всего вопросов: ', main_win.total, '\n-Правильных ответов: ', main_win.score)
    cur_question = randint(0, len(questions_list) - 1)  # нам не нужно старое значение, 
                                                        # поэтому можно использовать локальную переменную! 
            # случайно взяли вопрос в пределах списка
            # если внести около сотни слов, то редко будет повторяться
    q = questions_list[cur_question] # взяли вопрос
    ask(q) # спросили

def show_correct(res):
    ''' показать результат - установим переданный текст в надпись "результат" и покажем нужную панель '''
    lb_Result.setText(res)
    show_result()


def click_OK(): #был отступ
    if btn_OK.text() == 'Ответить:':
        check_answer()
    else:
        next_question()

main_win.setLayout(layout_card)
main_win.setWindowTitle('Memo card')


btn_OK.clicked.connect(click_OK) # по нажатии на кнопку выбираем, что конкретно происходит


main_win.score = 0 #window
main_win.total = 0 #window
next_question() #вызов
main_win.setLayout(layout_card)
main_win.show()
app.exec_()

#18