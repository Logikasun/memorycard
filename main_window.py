from PyQt5.QtWidgets import*
from app import app
from PyQt5.QtCore import*
from card_layout import layout_card
from data import *
from main_layout import *
from card_layout import *

main_width = 1000
main_height = 700
card_width = 800
card_height = 700
time_unit = 1000 

win_card = QWidget()
win_card.resize(main_width, main_height)
win_card.setWindowTitle('Memory Card')

# Глобальні змінні
questions_listmodel = QuestionListModel()
radio_list = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]
frm_card = 0 
timer = QTimer() 
win_main = QWidget()

# Тестові данні
def testlist():
    frm = Question('Якої країни цей бренд "Ariston"?', 'Італія', 'Україна' , 'Китай', 'Оттава')
    questions_listmodel.form_list.append(frm)
    frm = Question('Якої країни цей бренд "Hotpoint"?', 'Велика Британія', 'Лісабон', 'Бризилія', 'Америка')
    questions_listmodel.form_list.append(frm)
    frm = Question('Якої країни цей бренд "Miele"?', 'Німеччина', 'Київ', 'Австрія', 'Айзербайджан')
    questions_listmodel.form_list.append(frm)
    frm = Question('Якої країни цей бренд "Panasonic"?', 'Японія', 'Канада', 'Jiafei😍', 'Xiaomi')
    questions_listmodel.form_list.append(frm)
    frm = Question('Якої країни цей бренд "Haier"?', 'Китай', 'Македонія', 'Норвегія', 'Париж')
    questions_listmodel.form_list.append(frm)
    frm = Question('Якої країни цей бренд "Electrolux"?', 'Швеція', 'Синевир', 'Україна', 'Чехія')
    questions_listmodel.form_list.append(frm)
    frm = Question('Якої країни цей бренд "LG"?', 'Корея', 'Лісабон', 'Бризилія', 'Америка')
    questions_listmodel.form_list.append(frm)
    frm = Question('Якої країни цей бренд "Атлант"?', 'Білорусь', 'Меркурій', 'Венеція', 'Тайвань')
    questions_listmodel.form_list.append(frm)
    

def set_card():
    ''' задає, який вигляд має вікно картки'''
    win_card.resize(card_width, card_height)
    win_card.move(300, 300)
    win_card.setWindowTitle('Memory Card')
    win_card.setLayout(layout_card)

def sleep_card():
    ''' картка ховається на час, зазначений у таймері'''
    win_card.hide()
    timer.setInterval(time_unit * box_Minutes.value() )
    timer.start()

def show_card():
    ''' показує вікно (за таймером), таймер зупиняється'''
    win_card.show()
    timer.stop()

def show_random():
    ''' показати випадкове запитання '''
    global frm_card 
    frm_card = random_AnswerCheck(questions_listmodel, lb_Question, radio_list, lb_Correct, lb_Result)
    frm_card.show() 
    show_question()

def click_OK():
    ''' перевіряє запитання або завантажує нове запитання '''
    if btn_OK.text() != 'Наступне питання':
        frm_card.check()
        show_result()
    else:
        show_random()

def back_to_menu():
    ''' повернення з тесту у вікно редактора '''
    win_card.hide()
    win_main.showNormal()

# Функції для редагування питань
def set_main():
    ''' задає, який вигляд має основне вікно'''
    win_main.resize(main_width, main_height)
    win_main.move(100, 100)
    win_main.setWindowTitle('Список питань')
    win_main.setLayout(layout_main)

def edit_question(index):
    ''' завантажує у форму редагування запитання і відповіді, що відповідають переданому рядку '''
    if index.isValid():
        i = index.row()
        frm = questions_listmodel.form_list[i]

def add_form():
    ''' додає нове запитання і пропонує його змінити '''
    questions_listmodel.insertRows()  
    last = questions_listmodel.rowCount(0) - 1 
    index = questions_listmodel.index(
        last)  
    list_questions.setCurrentIndex(index)  
    edit_question(index)  
    
def del_form():
    ''' видаляє питання і перемикає фокус '''
    questions_listmodel.removeRows(list_questions.currentIndex().row())
    edit_question(list_questions.currentIndex())

def start_test():
    ''' на початку тесту форма зв'язується з випадковим питанням і показується '''
    show_random()
    win_card.show()
    win_main.showMinimized()

# Встановлення потрібних з`єднань
def connects():
    list_questions.setModel(questions_listmodel) 
    list_questions.clicked.connect(edit_question) 
    btn_add.clicked.connect(add_form) 
    btn_delete.clicked.connect(del_form)
    btn_start.clicked.connect(start_test)
    btn_OK.clicked.connect(click_OK) 
    btn_Menu.clicked.connect(back_to_menu) 
    timer.timeout.connect(show_card)
    btn_Sleep.clicked.connect(sleep_card)

# Запуск програми
testlist()
set_card()
set_main()
connects()

win_main.show()
app.exec_()