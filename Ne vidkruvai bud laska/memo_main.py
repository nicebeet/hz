from memo_card_layout import(
app,layout_card,
lb_Question,lb_Correct,lb_Result,
rbtn_1,rbtn_2,rbtn_3,rbtn_4,
btn_OK,show_question,show_results)   


from PyQt5.QtWidgets import QWidget,QApplication
from random import shuffle


card_width, card_height = 600,500
main_width,mai_height = 1000,450
time_unit  = 1000

#question_listmodel = QuestionListModel()
#frm_edit = QuestionEdit(0,txt_Question,txt_Answer,
 #                       txt_Wrong1,txtWrong2,txtWrong3,)
#frm_card = 0
#timer = QTimer()





text_wrong = 'Неправильно'
text_correct = 'Правильно'

frm_question = 'Яблуко'
frm_right = 'apple'
frm_wrong1 = 'yablyko'
frm_wrong2 = 'pen'
frm_wrong3 = 'trash'

radio_list = [rbtn_1,rbtn_2,rbtn_3,rbtn_4]
shuffle(radio_list)


answer = radio_list[0]
wrong_answer1 , wrong_answer2 ,wrong_answer3 = radio_list[1],radio_list[2],radio_list[3]


def show_data():
    
    lb_Question.setText(frm_question)
    lb_Correct.setText(frm_right)
    answer.setText(frm_right)
    wrong_answer1.setText(frm_wrong1)
    wrong_answer2.setText(frm_wrong2)
    wrong_answer3.setText(frm_wrong3)

def check_result():
    correct = answer.isChecked()
    if correct:
        lb_Result.setText(text_correct)
        show_results()
    else:
        incorrect = wrong_answer1.isChecked() or wrong_answer2.isChecked or wrong_answer3.isChecked
        if incorrect:
            lb_Result.setText(text_wrong)
            show_results()

def click_Ok(self):
    
    if btn_OK.text() != 'наступне питання':
        check_result()


#def back_to_menu():



win_card = QWidget()
win_card.resize(card_width,card_height)
win_card.move(300,300)
win_card.setWindowTitle('Memory card')

win_card.setLayout(layout_card)
show_data()
show_question()
btn_OK.clicked.connect(click_Ok)

win_card.show()
app.exec_()


