import random
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.uic import loadUi


def exitfunction():
    app.quit()

class MenuWindow(QDialog):
    def __init__(self):
        global current_question
        global questions_type
        super(MenuWindow, self).__init__()
        loadUi("Start.ui", self)
        if questions_type[current_question] == "12":
            self.startButton.clicked.connect(self.start12function)
        if questions_type[current_question] == "22":
            self.startButton.clicked.connect(self.start22function)
        if questions_type[current_question] == "13":
            self.startButton.clicked.connect(self.start13function)
        if questions_type[current_question] == "23":
            self.startButton.clicked.connect(self.start23function)
        if questions_type[current_question] == "14":
            self.startButton.clicked.connect(self.start14function)
        if questions_type[current_question] == "24":
            self.startButton.clicked.connect(self.start24function)
        if questions_type[current_question] == "15":
            self.startButton.clicked.connect(self.start15function)
        if questions_type[current_question] == "25":
            self.startButton.clicked.connect(self.start25function)
        if questions_type[current_question] == "16":
            self.startButton.clicked.connect(self.start16function)
        if questions_type[current_question] == "26":
            self.startButton.clicked.connect(self.start26function)
        self.exitButton.clicked.connect(exitfunction)

    def start12function(self):
        global current_question
        question12Window = question12()
        all_widgets['question12widget'] = question12Window
        widget.addWidget(all_widgets['question12widget'])
        widget.setCurrentWidget(all_widgets['question12widget'])

    def start22function(self):
        global current_question
        question22Window = question22()
        all_widgets['question22widget'] = question22Window
        widget.addWidget(all_widgets['question22widget'])
        widget.setCurrentWidget(all_widgets['question22widget'])

    def start13function(self):
        global current_question
        question13Window = question13()
        all_widgets['question13widget'] = question13Window
        widget.addWidget(all_widgets['question13widget'])
        widget.setCurrentWidget(all_widgets['question13widget'])

    def start23function(self):
        global current_question
        question23Window = question23()
        all_widgets['question22widget'] = question23Window
        widget.addWidget(all_widgets['question23widget'])
        widget.setCurrentWidget(all_widgets['question23widget'])

    def start14function(self):
        global current_question
        question14Window = question14()
        all_widgets['question14widget'] = question14Window
        widget.addWidget(all_widgets['question14widget'])
        widget.setCurrentWidget(all_widgets['question14widget'])

    def start24function(self):
        global current_question
        question24Window = question24()
        all_widgets['question24widget'] = question24Window
        widget.addWidget(all_widgets['question24widget'])
        widget.setCurrentWidget(all_widgets['question24widget'])

    def start15function(self):
        global current_question
        question15Window = question15()
        all_widgets['question15widget'] = question15Window
        widget.addWidget(all_widgets['question15widget'])
        widget.setCurrentWidget(all_widgets['question15widget'])

    def start25function(self):
        global current_question
        question25Window = question25()
        all_widgets['question25widget'] = question25Window
        widget.addWidget(all_widgets['question25widget'])
        widget.setCurrentWidget(all_widgets['question25widget'])

    def start16function(self):
        global current_question
        question16Window = question16()
        all_widgets['question16widget'] = question16Window
        widget.addWidget(all_widgets['question16widget'])
        widget.setCurrentWidget(all_widgets['question16widget'])

    def start26function(self):
        global current_question
        question26Window = question26()
        all_widgets['question26widget'] = question26Window
        widget.addWidget(all_widgets['question26widget'])
        widget.setCurrentWidget(all_widgets['question26widget'])


def endfunction():
    congratulationWindow = Congratulation()
    all_widgets['congratulationwidget'] = congratulationWindow
    widget.addWidget(all_widgets['congratulationwidget'])
    widget.setCurrentWidget(all_widgets['congratulationwidget'])

def nextfunction12():
    global current_question
    current_question = current_question + 1
    question12Window = question12()
    all_widgets['question12widget'] = question12Window
    widget.addWidget(all_widgets['question12widget'])
    widget.setCurrentWidget(all_widgets['question12widget'])

def nextfunction22():
    global current_question
    current_question = current_question + 1
    question22Window = question22()
    all_widgets['question22widget'] = question22Window
    widget.addWidget(all_widgets['question22widget'])
    widget.setCurrentWidget(all_widgets['question22widget'])

def nextfunction13():
    global current_question
    current_question = current_question + 1
    question13Window = question13()
    all_widgets['question13widget'] = question13Window
    widget.addWidget(all_widgets['question13widget'])
    widget.setCurrentWidget(all_widgets['question13widget'])

def nextfunction23():
    global current_question
    current_question = current_question + 1
    question23Window = question23()
    all_widgets['question22widget'] = question23Window
    widget.addWidget(all_widgets['question23widget'])
    widget.setCurrentWidget(all_widgets['question23widget'])

def nextfunction14():
    global current_question
    current_question = current_question + 1
    question14Window = question14()
    all_widgets['question14widget'] = question14Window
    widget.addWidget(all_widgets['question14widget'])
    widget.setCurrentWidget(all_widgets['question14widget'])

def nextfunction24():
    global current_question
    current_question = current_question + 1
    question24Window = question24()
    all_widgets['question24widget'] = question24Window
    widget.addWidget(all_widgets['question24widget'])
    widget.setCurrentWidget(all_widgets['question24widget'])

def nextfunction15():
    global current_question
    current_question = current_question + 1
    question15Window = question15()
    all_widgets['question15widget'] = question15Window
    widget.addWidget(all_widgets['question15widget'])
    widget.setCurrentWidget(all_widgets['question15widget'])

def nextfunction25():
    global current_question
    current_question = current_question + 1
    question25Window = question25()
    all_widgets['question25widget'] = question25Window
    widget.addWidget(all_widgets['question25widget'])
    widget.setCurrentWidget(all_widgets['question25widget'])

def nextfunction16():
    global current_question
    current_question = current_question + 1
    question16Window = question16()
    all_widgets['question16widget'] = question16Window
    widget.addWidget(all_widgets['question16widget'])
    widget.setCurrentWidget(all_widgets['question16widget'])

def nextfunction26():
    global current_question
    current_question = current_question + 1
    question26Window = question26()
    all_widgets['question26widget'] = question26Window
    widget.addWidget(all_widgets['question26widget'])
    widget.setCurrentWidget(all_widgets['question26widget'])


def behindfunction12():
    global current_question
    current_question = current_question - 1
    question12Window = question12()
    all_widgets['question12widget'] = question12Window
    widget.addWidget(all_widgets['question12widget'])
    widget.setCurrentWidget(all_widgets['question12widget'])


def behindfunction22():
    global current_question
    current_question = current_question - 1
    question22Window = question22()
    all_widgets['question22widget'] = question22Window
    widget.addWidget(all_widgets['question22widget'])
    widget.setCurrentWidget(all_widgets['question22widget'])


def behindfunction13():
    global current_question
    current_question = current_question - 1
    question13Window = question13()
    all_widgets['question13widget'] = question13Window
    widget.addWidget(all_widgets['question13widget'])
    widget.setCurrentWidget(all_widgets['question13widget'])


def behindfunction23():
    global current_question
    current_question = current_question - 1
    question23Window = question23()
    all_widgets['question22widget'] = question23Window
    widget.addWidget(all_widgets['question23widget'])
    widget.setCurrentWidget(all_widgets['question23widget'])

def behindfunction14():
    global current_question
    current_question = current_question - 1
    question14Window = question14()
    all_widgets['question14widget'] = question14Window
    widget.addWidget(all_widgets['question14widget'])
    widget.setCurrentWidget(all_widgets['question14widget'])

def behindfunction24():
    global current_question
    current_question = current_question - 1
    question24Window = question24()
    all_widgets['question24widget'] = question24Window
    widget.addWidget(all_widgets['question24widget'])
    widget.setCurrentWidget(all_widgets['question24widget'])


def behindfunction15():
    global current_question
    current_question = current_question - 1
    question15Window = question15()
    all_widgets['question15widget'] = question15Window
    widget.addWidget(all_widgets['question15widget'])
    widget.setCurrentWidget(all_widgets['question15widget'])


def behindfunction25():
    global current_question
    current_question = current_question - 1
    question25Window = question25()
    all_widgets['question25widget'] = question25Window
    widget.addWidget(all_widgets['question25widget'])
    widget.setCurrentWidget(all_widgets['question25widget'])


def behindfunction16():
    global current_question
    current_question = current_question - 1
    question16Window = question16()
    all_widgets['question16widget'] = question16Window
    widget.addWidget(all_widgets['question16widget'])
    widget.setCurrentWidget(all_widgets['question16widget'])


def behindfunction26():
    global current_question
    current_question = current_question - 1
    question26Window = question26()
    all_widgets['question26widget'] = question26Window
    widget.addWidget(all_widgets['question26widget'])
    widget.setCurrentWidget(all_widgets['question26widget'])


class question12(QDialog):
    def __init__(self):
        super(question12, self).__init__()
        loadUi("question12.ui", self)
        self.label.setText(questions_and_answers_text[current_question][0])
        self.btn1.setText(questions_and_answers_text[current_question][1])
        self.btn2.setText(questions_and_answers_text[current_question][2])
        self.btn1.clicked.connect(lambda checked, num=1: self.btnfunction(num))
        self.btn2.clicked.connect(lambda checked, num=2: self.btnfunction(num))

        if current_question != number_of_questions - 1:
            if questions_type[current_question + 1] == "14":
                self.behindButton.clicked.connect(behindfunction14)
            if questions_type[current_question + 1] == "24":
                self.behindButton.clicked.connect(behindfunction24)
        if current_question != number_of_questions - 1:
            if questions_type[current_question + 1] == "14":
                self.nextButton.clicked.connect(nextfunction14)
            if questions_type[current_question + 1] == "24":
                self.nextButton.clicked.connect(nextfunction24)
        if current_question == number_of_questions - 1:
            self.nextButton.setText("Завершить тест")
            self.nextButton.clicked.connect(endfunction)

    def btnfunction(self, num):
        global user_answers
        if num == 1:
            user_answers[current_question][0] = 1
        if num == 2:
            user_answers[current_question][0] = 2


class question22(QDialog):
    def __init__(self):
        super(question22, self).__init__()
        loadUi("question22.ui", self)
        self.label.setText(questions_and_answers_text[current_question][0])
        self.btn1.setText(questions_and_answers_text[current_question][1])
        self.btn2.setText(questions_and_answers_text[current_question][2])
        self.btn1.clicked.connect(lambda checked, num=1: self.btnfunction(num))
        self.btn2.clicked.connect(lambda checked, num=2: self.btnfunction(num))
        if current_question != number_of_questions - 1:
            if questions_type[current_question + 1] == "14":
                self.behindButton.clicked.connect(behindfunction14)
            if questions_type[current_question + 1] == "24":
                self.behindButton.clicked.connect(behindfunction24)
        if current_question != number_of_questions - 1:
            if questions_type[current_question + 1] == "14":
                self.nextButton.clicked.connect(nextfunction14)
            if questions_type[current_question + 1] == "24":
                self.nextButton.clicked.connect(nextfunction24)
        if current_question == number_of_questions - 1:
            self.nextButton.setText("Завершить тест")
            self.nextButton.clicked.connect(endfunction)


    def btnfunction(self, num):
        global user_answers
        if num == 1 and active_btn[0] == 0:
            user_answers[current_question][0] = 1
            active_btn[0] = 1
        elif num == 1 and active_btn[0] == 1:
            user_answers[current_question][0] = 0
            active_btn[0] = 0
        if num == 2 and active_btn[1] == 0:
            user_answers[current_question][1] = 1
            active_btn[1] = 1
        elif num == 2 and active_btn[1] == 1:
            user_answers[current_question][1] = 0
            active_btn[1] = 0


class question13(QDialog):
    def __init__(self):
        super(question13, self).__init__()
        loadUi("question13.ui", self)
        self.label.setText(questions_and_answers_text[current_question][0])
        self.btn1.setText(questions_and_answers_text[current_question][1])
        self.btn2.setText(questions_and_answers_text[current_question][2])
        self.btn3.setText(questions_and_answers_text[current_question][3])
        self.btn1.clicked.connect(lambda checked, num=1: self.btnfunction(num))
        self.btn2.clicked.connect(lambda checked, num=2: self.btnfunction(num))
        self.btn3.clicked.connect(lambda checked, num=3: self.btnfunction(num))
        if current_question != number_of_questions - 1:
            if questions_type[current_question + 1] == "14":
                self.behindButton.clicked.connect(behindfunction14)
            if questions_type[current_question + 1] == "24":
                self.behindButton.clicked.connect(behindfunction24)
        if current_question != number_of_questions - 1:
            if questions_type[current_question + 1] == "14":
                self.nextButton.clicked.connect(nextfunction14)
            if questions_type[current_question + 1] == "24":
                self.nextButton.clicked.connect(nextfunction24)
        if current_question == number_of_questions - 1:
            self.nextButton.setText("Завершить тест")
            self.nextButton.clicked.connect(endfunction)

    def btnfunction(self, num):
        global user_answers
        if num == 1:
            user_answers[current_question][0] = 1
        if num == 2:
            user_answers[current_question][0] = 2
        if num == 3:
            user_answers[current_question][0] = 3


class question23(QDialog):
    def __init__(self):
        super(question23, self).__init__()
        loadUi("question23.ui", self)
        self.label.setText(questions_and_answers_text[current_question][0])
        self.btn1.setText(questions_and_answers_text[current_question][1])
        self.btn2.setText(questions_and_answers_text[current_question][2])
        self.btn3.setText(questions_and_answers_text[current_question][3])
        self.btn1.clicked.connect(lambda checked, num=1: self.btnfunction(num))
        self.btn2.clicked.connect(lambda checked, num=2: self.btnfunction(num))
        self.btn3.clicked.connect(lambda checked, num=3: self.btnfunction(num))
        if current_question != number_of_questions - 1:
            if questions_type[current_question + 1] == "14":
                self.behindButton.clicked.connect(behindfunction14)
            if questions_type[current_question + 1] == "24":
                self.behindButton.clicked.connect(behindfunction24)
        if current_question != number_of_questions - 1:
            if questions_type[current_question + 1] == "14":
                self.nextButton.clicked.connect(nextfunction14)
            if questions_type[current_question + 1] == "24":
                self.nextButton.clicked.connect(nextfunction24)
        if current_question == number_of_questions - 1:
            self.nextButton.setText("Завершить тест")
            self.nextButton.clicked.connect(endfunction)


    def btnfunction(self, num):
        global user_answers
        if num == 1 and active_btn[0] == 0:
            user_answers[current_question][0] = 1
            active_btn[0] = 1
        elif num == 1 and active_btn[0] == 1:
            user_answers[current_question][0] = 0
            active_btn[0] = 0
        if num == 2 and active_btn[1] == 0:
            user_answers[current_question][1] = 1
            active_btn[1] = 1
        elif num == 2 and active_btn[1] == 1:
            user_answers[current_question][1] = 0
            active_btn[1] = 0
        if num == 3 and active_btn[2] == 0:
            user_answers[current_question][2] = 1
            active_btn[2] = 1
        elif num == 3 and active_btn[2] == 1:
            user_answers[current_question][2] = 0
            active_btn[2] = 0


class question14(QDialog):
    def __init__(self):
        super(question14, self).__init__()
        loadUi("question14.ui", self)
        self.label.setText(questions_and_answers_text[current_question][0])
        self.btn1.setText(questions_and_answers_text[current_question][1])
        self.btn2.setText(questions_and_answers_text[current_question][2])
        self.btn3.setText(questions_and_answers_text[current_question][3])
        self.btn4.setText(questions_and_answers_text[current_question][4])
        self.btn1.clicked.connect(lambda checked, num=1: self.btnfunction(num))
        self.btn2.clicked.connect(lambda checked, num=2: self.btnfunction(num))
        self.btn3.clicked.connect(lambda checked, num=3: self.btnfunction(num))
        self.btn4.clicked.connect(lambda checked, num=4: self.btnfunction(num))
        if current_question != number_of_questions - 1:
            if questions_type[current_question + 1] == "14":
                self.behindButton.clicked.connect(behindfunction14)
            if questions_type[current_question + 1] == "24":
                self.behindButton.clicked.connect(behindfunction24)
        if current_question != number_of_questions - 1:
            if questions_type[current_question + 1] == "14":
                self.nextButton.clicked.connect(nextfunction14)
            if questions_type[current_question + 1] == "24":
                self.nextButton.clicked.connect(nextfunction24)
        if current_question == number_of_questions - 1:
            self.nextButton.setText("Завершить тест")
            self.nextButton.clicked.connect(endfunction)

    def btnfunction(self, num):
        global user_answers
        if num == 1:
            user_answers[current_question][0] = 1
        if num == 2:
            user_answers[current_question][0] = 2
        if num == 3:
            user_answers[current_question][0] = 3
        if num == 4:
            user_answers[current_question][0] = 4


class question24(QDialog):
    def __init__(self):
        super(question24, self).__init__()
        loadUi("question24.ui", self)
        self.label.setText(questions_and_answers_text[current_question][0])
        self.btn1.setText(questions_and_answers_text[current_question][1])
        self.btn2.setText(questions_and_answers_text[current_question][2])
        self.btn3.setText(questions_and_answers_text[current_question][3])
        self.btn4.setText(questions_and_answers_text[current_question][4])
        self.btn1.clicked.connect(lambda checked, num=1: self.btnfunction(num))
        self.btn2.clicked.connect(lambda checked, num=2: self.btnfunction(num))
        self.btn3.clicked.connect(lambda checked, num=3: self.btnfunction(num))
        self.btn4.clicked.connect(lambda checked, num=4: self.btnfunction(num))
        if current_question != number_of_questions - 1:
            if questions_type[current_question + 1] == "14":
                self.behindButton.clicked.connect(behindfunction14)
            if questions_type[current_question + 1] == "24":
                self.behindButton.clicked.connect(behindfunction24)
        if current_question != number_of_questions - 1:
            if questions_type[current_question + 1] == "14":
                self.nextButton.clicked.connect(nextfunction14)
            if questions_type[current_question + 1] == "24":
                self.nextButton.clicked.connect(nextfunction24)
        if current_question == number_of_questions - 1:
            self.nextButton.setText("Завершить тест")
            self.nextButton.clicked.connect(endfunction)


    def btnfunction(self, num):
        global user_answers
        if num == 1 and active_btn[0] == 0:
            user_answers[current_question][0] = 1
            active_btn[0] = 1
        elif num == 1 and active_btn[0] == 1:
            user_answers[current_question][0] = 0
            active_btn[0] = 0
        if num == 2 and active_btn[1] == 0:
            user_answers[current_question][1] = 1
            active_btn[1] = 1
        elif num == 2 and active_btn[1] == 1:
            user_answers[current_question][1] = 0
            active_btn[1] = 0
        if num == 3 and active_btn[2] == 0:
            user_answers[current_question][2] = 1
            active_btn[2] = 1
        elif num == 3 and active_btn[2] == 1:
            user_answers[current_question][2] = 0
            active_btn[2] = 0
        if num == 4 and active_btn[3] == 0:
            user_answers[current_question][3] = 1
            active_btn[3] = 1
        elif num == 4 and active_btn[3] == 1:
            user_answers[current_question][3] = 0
            active_btn[3] = 0


class question15(QDialog):
    def __init__(self):
        super(question15, self).__init__()
        loadUi("question15.ui", self)
        self.label.setText(questions_and_answers_text[current_question][0])
        self.btn1.setText(questions_and_answers_text[current_question][1])
        self.btn2.setText(questions_and_answers_text[current_question][2])
        self.btn3.setText(questions_and_answers_text[current_question][3])
        self.btn4.setText(questions_and_answers_text[current_question][4])
        self.btn5.setText(questions_and_answers_text[current_question][5])
        self.btn1.clicked.connect(lambda checked, num=1: self.btnfunction(num))
        self.btn2.clicked.connect(lambda checked, num=2: self.btnfunction(num))
        self.btn3.clicked.connect(lambda checked, num=3: self.btnfunction(num))
        self.btn4.clicked.connect(lambda checked, num=4: self.btnfunction(num))
        self.btn5.clicked.connect(lambda checked, num=5: self.btnfunction(num))
        if current_question != number_of_questions - 1:
            if questions_type[current_question + 1] == "14":
                self.behindButton.clicked.connect(behindfunction14)
            if questions_type[current_question + 1] == "24":
                self.behindButton.clicked.connect(behindfunction24)
        if current_question != number_of_questions - 1:
            if questions_type[current_question + 1] == "14":
                self.nextButton.clicked.connect(nextfunction14)
            if questions_type[current_question + 1] == "24":
                self.nextButton.clicked.connect(nextfunction24)
        if current_question == number_of_questions - 1:
            self.nextButton.setText("Завершить тест")
            self.nextButton.clicked.connect(endfunction)

    def btnfunction(self, num):
        global user_answers
        if num == 1:
            user_answers[current_question][0] = 1
        if num == 2:
            user_answers[current_question][0] = 2
        if num == 3:
            user_answers[current_question][0] = 3
        if num == 4:
            user_answers[current_question][0] = 4
        if num == 5:
            user_answers[current_question][0] = 5


class question25(QDialog):
    def __init__(self):
        super(question25, self).__init__()
        loadUi("question25.ui", self)
        self.label.setText(questions_and_answers_text[current_question][0])
        self.btn1.setText(questions_and_answers_text[current_question][1])
        self.btn2.setText(questions_and_answers_text[current_question][2])
        self.btn3.setText(questions_and_answers_text[current_question][3])
        self.btn4.setText(questions_and_answers_text[current_question][4])
        self.btn5.setText(questions_and_answers_text[current_question][5])
        self.btn1.clicked.connect(lambda checked, num=1: self.btnfunction(num))
        self.btn2.clicked.connect(lambda checked, num=2: self.btnfunction(num))
        self.btn3.clicked.connect(lambda checked, num=3: self.btnfunction(num))
        self.btn4.clicked.connect(lambda checked, num=4: self.btnfunction(num))
        self.btn5.clicked.connect(lambda checked, num=5: self.btnfunction(num))
        if current_question != number_of_questions - 1:
            if questions_type[current_question + 1] == "14":
                self.behindButton.clicked.connect(behindfunction14)
            if questions_type[current_question + 1] == "24":
                self.behindButton.clicked.connect(behindfunction24)
        if current_question != number_of_questions - 1:
            if questions_type[current_question + 1] == "14":
                self.nextButton.clicked.connect(nextfunction14)
            if questions_type[current_question + 1] == "24":
                self.nextButton.clicked.connect(nextfunction24)
        if current_question == number_of_questions - 1:
            self.nextButton.setText("Завершить тест")
            self.nextButton.clicked.connect(endfunction)


    def btnfunction(self, num):
        global user_answers
        if num == 1 and active_btn[0] == 0:
            user_answers[current_question][0] = 1
            active_btn[0] = 1
        elif num == 1 and active_btn[0] == 1:
            user_answers[current_question][0] = 0
            active_btn[0] = 0
        if num == 2 and active_btn[1] == 0:
            user_answers[current_question][1] = 1
            active_btn[1] = 1
        elif num == 2 and active_btn[1] == 1:
            user_answers[current_question][1] = 0
            active_btn[1] = 0
        if num == 3 and active_btn[2] == 0:
            user_answers[current_question][2] = 1
            active_btn[2] = 1
        elif num == 3 and active_btn[2] == 1:
            user_answers[current_question][2] = 0
            active_btn[2] = 0
        if num == 4 and active_btn[3] == 0:
            user_answers[current_question][3] = 1
            active_btn[3] = 1
        elif num == 4 and active_btn[3] == 1:
            user_answers[current_question][3] = 0
            active_btn[3] = 0
        if num == 5 and active_btn[4] == 0:
            user_answers[current_question][4] = 1
            active_btn[4] = 1
        elif num == 5 and active_btn[4] == 1:
            user_answers[current_question][4] = 0
            active_btn[4] = 0


class question16(QDialog):
    def __init__(self):
        super(question16, self).__init__()
        loadUi("question16.ui", self)
        self.label.setText(questions_and_answers_text[current_question][0])
        self.btn1.setText(questions_and_answers_text[current_question][1])
        self.btn2.setText(questions_and_answers_text[current_question][2])
        self.btn3.setText(questions_and_answers_text[current_question][3])
        self.btn4.setText(questions_and_answers_text[current_question][4])
        self.btn5.setText(questions_and_answers_text[current_question][5])
        self.btn5.setText(questions_and_answers_text[current_question][6])
        self.btn1.clicked.connect(lambda checked, num=1: self.btnfunction(num))
        self.btn2.clicked.connect(lambda checked, num=2: self.btnfunction(num))
        self.btn3.clicked.connect(lambda checked, num=3: self.btnfunction(num))
        self.btn4.clicked.connect(lambda checked, num=4: self.btnfunction(num))
        self.btn5.clicked.connect(lambda checked, num=5: self.btnfunction(num))
        self.btn5.clicked.connect(lambda checked, num=6: self.btnfunction(num))
        if current_question != number_of_questions - 1:
            if questions_type[current_question + 1] == "14":
                self.behindButton.clicked.connect(behindfunction14)
            if questions_type[current_question + 1] == "24":
                self.behindButton.clicked.connect(behindfunction24)
        if current_question != number_of_questions - 1:
            if questions_type[current_question + 1] == "14":
                self.nextButton.clicked.connect(nextfunction14)
            if questions_type[current_question + 1] == "24":
                self.nextButton.clicked.connect(nextfunction24)
        if current_question == number_of_questions - 1:
            self.nextButton.setText("Завершить тест")
            self.nextButton.clicked.connect(endfunction)

    def btnfunction(self, num):
        global user_answers
        if num == 1:
            user_answers[current_question][0] = 1
        if num == 2:
            user_answers[current_question][0] = 2
        if num == 3:
            user_answers[current_question][0] = 3
        if num == 4:
            user_answers[current_question][0] = 4
        if num == 5:
            user_answers[current_question][0] = 5
        if num == 6:
            user_answers[current_question][0] = 6


class question26(QDialog):
    def __init__(self):
        super(question26, self).__init__()
        loadUi("question26.ui", self)
        self.label.setText(questions_and_answers_text[current_question][0])
        self.btn1.setText(questions_and_answers_text[current_question][1])
        self.btn2.setText(questions_and_answers_text[current_question][2])
        self.btn3.setText(questions_and_answers_text[current_question][3])
        self.btn4.setText(questions_and_answers_text[current_question][4])
        self.btn5.setText(questions_and_answers_text[current_question][5])
        self.btn6.setText(questions_and_answers_text[current_question][5])
        self.btn1.clicked.connect(lambda checked, num=1: self.btnfunction(num))
        self.btn2.clicked.connect(lambda checked, num=2: self.btnfunction(num))
        self.btn3.clicked.connect(lambda checked, num=3: self.btnfunction(num))
        self.btn4.clicked.connect(lambda checked, num=4: self.btnfunction(num))
        self.btn5.clicked.connect(lambda checked, num=5: self.btnfunction(num))
        self.btn6.clicked.connect(lambda checked, num=6: self.btnfunction(num))
        if current_question != number_of_questions - 1:
            if questions_type[current_question + 1] == "14":
                self.behindButton.clicked.connect(behindfunction14)
            if questions_type[current_question + 1] == "24":
                self.behindButton.clicked.connect(behindfunction24)
        if current_question != number_of_questions - 1:
            if questions_type[current_question + 1] == "14":
                self.nextButton.clicked.connect(nextfunction14)
            if questions_type[current_question + 1] == "24":
                self.nextButton.clicked.connect(nextfunction24)
        if current_question == number_of_questions - 1:
            self.nextButton.setText("Завершить тест")
            self.nextButton.clicked.connect(endfunction)


    def btnfunction(self, num):
        global user_answers
        if num == 1 and active_btn[0] == 0:
            user_answers[current_question][0] = 1
            active_btn[0] = 1
        elif num == 1 and active_btn[0] == 1:
            user_answers[current_question][0] = 0
            active_btn[0] = 0
        if num == 2 and active_btn[1] == 0:
            user_answers[current_question][1] = 1
            active_btn[1] = 1
        elif num == 2 and active_btn[1] == 1:
            user_answers[current_question][1] = 0
            active_btn[1] = 0
        if num == 3 and active_btn[2] == 0:
            user_answers[current_question][2] = 1
            active_btn[2] = 1
        elif num == 3 and active_btn[2] == 1:
            user_answers[current_question][2] = 0
            active_btn[2] = 0
        if num == 4 and active_btn[3] == 0:
            user_answers[current_question][3] = 1
            active_btn[3] = 1
        elif num == 4 and active_btn[3] == 1:
            user_answers[current_question][3] = 0
            active_btn[3] = 0
        if num == 5 and active_btn[4] == 0:
            user_answers[current_question][4] = 1
            active_btn[4] = 1
        elif num == 5 and active_btn[4] == 1:
            user_answers[current_question][4] = 0
            active_btn[4] = 0
        if num == 6 and active_btn[5] == 0:
            user_answers[current_question][5] = 1
            active_btn[5] = 1
        elif num == 6 and active_btn[5] == 1:
            user_answers[current_question][5] = 0
            active_btn[5] = 0


class Congratulation(QDialog):
    def __init__(self):
        super(Congratulation, self).__init__()
        loadUi("Congratulation.ui", self)
        res = 0
        for i in range(number_of_questions):
            if str(user_answers[i][0]) == correct_answers[i][0]:
                res = res + 1

        self.result.setText("Результат тестирования: " + str(res) + "/" + str(number_of_questions))
        self.exitButton.clicked.connect(exitfunction)
        self.restartButton.clicked.connect(self.restartfunction)

    def restartfunction(self):
        global current_question
        if questions_type[0] == "24":
            current_question = 0
            question2Window = question24()
            all_widgets['question2widget'] = question2Window
            widget.addWidget(all_widgets['question2widget'])
            widget.setCurrentWidget(all_widgets['question2widget'])
        if questions_type[0] == "14":
            current_question = 0
            question1Window = question14()
            all_widgets['question1widget'] = question1Window
            widget.addWidget(all_widgets['question1widget'])
            widget.setCurrentWidget(all_widgets['question1widget'])




active_btn = [0],[0],[0],[0],[0],[0]
i = 0
data = []
with open("test.txt", encoding="utf-8") as test:
    for line in test:
        data.append(line.rstrip('\n'))
number_of_questions = int(data[0])
questions_type = []
t = 0
q = 0
a = 0
c = 0
j = 1
questions_and_answers_text = [[]for i in range(number_of_questions)]
correct_answers = [[]for i in range(number_of_questions)]
for i in range(len(data)):
    if data[i] == "type:":
        questions_type.append(data[i+1])
        t = t + 1
    if data[i] == "question:":
        questions_and_answers_text[q].append(data[i + 1])
        q = q + 1
    if data[i] == "answers:":
        questions_and_answers_text[a].append(data[i + 1])
        questions_and_answers_text[a].append(data[i + 2])
        questions_and_answers_text[a].append(data[i + 3])
        questions_and_answers_text[a].append(data[i + 4])
        a = a + 1
    if data[i] == "correct:":
        correct_answers[c].append(data[i + 1])
        c = c + 1

current_question = 0
user_answers = [[0 for j in range(4)] for i in range(number_of_questions)]


app = QApplication(sys.argv)
menuWindow = MenuWindow()
all_widgets = {'menuwidget': menuWindow}
widget = QtWidgets.QStackedWidget()
widget.addWidget(all_widgets['menuwidget'])
widget.setCurrentWidget(all_widgets['menuwidget'])
widget.setFixedWidth(1350)
widget.setFixedHeight(650)
widget.setWindowTitle('Geleos & Grunt Test System')
widget.show()
app.exec_()
