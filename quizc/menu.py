from quizc.console.quiz_ui_handler import *

class Menu(object):
    MENU_PROMPT = "> "

    def __init__(self):
        self.car = ""
        self.quiz = None
        self.quiz_answers = None

    def show_main_menu(self):
        print("""
Quizc - A command quiz utility
======================================
1. Create quiz
2. Fill quiz
3. Show quiz
4. Exit
======================================
        """)

    def create(self):
            self.quiz = QuizUIHandler.create_quiz()

    def fill(self):
        if self.quiz is None:
            print("No quiz available, you must create first a quiz")
        else:
            self.quiz_answers = QuizUIHandler.fill_quiz(self.quiz)

    def show(self):
        if self.quiz_answers is None:
            print("No filled quiz available, you must create first a quiz")
        else:
            QuizUIHandler.show_quiz(self.quiz_answers)

    def process(self):
        should_exit = False
        self.show_main_menu()
        option = input(self.MENU_PROMPT)
        if option=="1":
            self.create()
        elif option=="2":
            self.fill()
        elif option=="3":
            self.show()
        else:
            should_exit = True
        return should_exit
