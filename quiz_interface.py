import sys
from PyQt6.QtWidgets import (QApplication, QWidget, QLabel, QPushButton,
                             QButtonGroup, QGroupBox, QRadioButton, QVBoxLayout, QHBoxLayout)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon


class QuizInference(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("<b>QUIZZLA</b>")
        self.setWindowIcon(QIcon("images/quizzla_logo.png"))
        self.setMinimumSize(500, 500)

        self.initializeUI()
        self.show()

    def initializeUI(self):
        """ Create and arrange widget for main window"""
        self.quiz_category = QLabel()
        self.quiz_category.setText("<b>CATEGORY: </b>" + "General")
        self.level = QLabel()
        self.level.setText("<b>LEVEL: </b>" + "Medium")

        # layout for question category
        quiz_cat = QWidget()
        quiz_cat_h_layout = QHBoxLayout()
        quiz_cat_h_layout.addWidget(self.quiz_category)
        quiz_cat_h_layout.addWidget(self.level)

        quiz_cat.setLayout(quiz_cat_h_layout)

        # question component
        answers = ["A. Neil Armstrong", "B. Neil Patrick Harris", "C. Patrick Buns", "D. Daniel Sky"]
        # self.ques_label = QLabel("Who is the first man to step on the moon.")
        # self.ques_label.setObjectName("quesHead")

        # group box for question
        question_gb = QGroupBox("1.Who is the first man to step on the moon.")
        question_gb_v_layout = QVBoxLayout()

        # buttonGroup for answers
        self.ans_bg = QButtonGroup()

        # answers radio btn
        for ans in answers:
            ans_rb = QRadioButton(ans)
            question_gb_v_layout.addWidget(ans_rb)
            self.ans_bg.addButton(ans_rb)
        question_gb.setLayout(question_gb_v_layout)

        # submit btn
        submit_ans = QPushButton("Next")
        submit_ans.setObjectName("confirmBtn")

        # create main layout for question and answers
        main_v_layout = QVBoxLayout()
        main_v_layout.addWidget(quiz_cat)
        main_v_layout.addSpacing(20)
        main_v_layout.addWidget(question_gb)
        main_v_layout.addWidget(submit_ans, 1, Qt.AlignmentFlag.AlignRight)
        main_v_layout.addStretch()

        self.setLayout(main_v_layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QuizInference()
    sys.exit(app.exec())

