from quizc.console.quiz_ui_handler import *


def show_main_menu():
    print("""
Quizc - A command quiz utility
======================================
1. Create quiz
2. Fill quiz
3. Show quiz
4. Exit
======================================
    """)


class Menu(object):
    MENU_PROMPT = "> "

    def __init__(self):
        self.car = ""
        self.quiz = None
        self.quiz_answers = None

    def process(self):
        show_main_menu()
        option = input(self.MENU_PROMPT)
        should_exit = False
        if option == "1":
            self.quiz = QuizUIHandler.create_quiz()

        if option == "2" and self.quiz is not None:
            self.quiz_answers = QuizUIHandler.fill_quiz(self.quiz)
        elif option == "2":
            print("No quiz available, you must create first a quiz")

        if option == "3" and self.quiz_answers is not None:
            QuizUIHandler.show_quiz(self.quiz_answers)
        elif option == "3":
            print("No filled quiz available, you must create first a quiz")

        if option == "4":
            should_exit = True

        return should_exit
