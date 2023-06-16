import sys
from PyQt6.QtWidgets import (QApplication, QWidget, QPushButton, QFrame, QLabel, QVBoxLayout, QHBoxLayout, QSizePolicy)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon, QPixmap


class HomeWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("<b>QUIZZLA</b>")
        self.setWindowIcon(QIcon("images/quizzla_logo.png"))
        self.setMaximumSize(500, 500)

        self.initializeUI()
        self.show()

    def initializeUI(self):
        """ create and arrange widget in window"""
        category = ["General", "Science", "Mathematics", "Music", "Social", "Movies", "Art", "History", "Literature",
                    "Comm Skills"]

        cat_v_layout = QVBoxLayout()

        for cat_btn in category:
            btn_widget = QPushButton(cat_btn)
            cat_v_layout.addWidget(btn_widget)
        # cat_box.setLayout(cat_v_layout)
        cat_v_layout.addSpacing(20)

        # create frame and add cat_box
        self.cat_box_frame = QFrame()
        size_policy = QSizePolicy(QSizePolicy.Policy.Expanding,
                                  QSizePolicy.Policy.Preferred)
        self.cat_box_frame.setSizePolicy(size_policy)
        self.cat_box_frame.setFrameShape(QFrame.Shape.Panel)
        self.cat_box_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.cat_box_frame.setLineWidth(3)
        self.cat_box_frame.setMidLineWidth(5)

        # set the layout for the QFrame object
        self.cat_box_frame.setLayout(cat_v_layout)

        quiz_img_path = "images/quiz_image2.jpeg"
        image_label = QLabel()
        image_label.setPixmap(QPixmap(quiz_img_path))

        # welcome label and profile btn
        welcome_label = QLabel()
        welcome_label.setText("<h2>Welcome</h2>")
        welcome_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # profile_btn
        profile_btn = QPushButton("Profile")

        # container and widget for profile_btn and welcome_label
        profile_welcome = QWidget()
        pro_wel_v_layout = QVBoxLayout()
        pro_wel_v_layout.addWidget(welcome_label, 1, Qt.AlignmentFlag.AlignCenter)
        pro_wel_v_layout.addWidget(image_label, 1, Qt.AlignmentFlag.AlignCenter)
        pro_wel_v_layout.addWidget(profile_btn, 1, Qt.AlignmentFlag.AlignCenter)
        pro_wel_v_layout.addStretch()

        profile_welcome.setLayout(pro_wel_v_layout)

        # create container widget for category, welcome label and profile btn
        top_container = QWidget()
        top_container_h_layout = QHBoxLayout()
        top_container_h_layout.addWidget(self.cat_box_frame)
        top_container_h_layout.addWidget(profile_welcome, 1)
        top_container_h_layout.addStretch()
        top_container.setLayout(top_container_h_layout)

        history_label = QLabel("<b><u> QUIZ HISTORY <u></b>")
        history_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.time_line1_label = QLabel()
        self.time_line1_label.setText("<b>CATEGORY: </b>" + "Math")
        self.time_line1_score = QLabel()
        self.time_line1_score.setText("<b>SCORE: </b>" + "100")

        history_container = QWidget()
        history_v_layout = QVBoxLayout()
        history_v_layout.addWidget(history_label)
        history_v_layout.addWidget(self.time_line1_label)
        history_v_layout.addWidget(self.time_line1_score)

        history_container.setLayout(history_v_layout)

        # create main layout for window
        main_v_layout = QVBoxLayout()
        main_v_layout.addWidget(top_container)
        main_v_layout.addWidget(history_container)

        self.setLayout(main_v_layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = HomeWindow()
    sys.exit(app.exec())

