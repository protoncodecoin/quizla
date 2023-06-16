import sys
from PyQt6.QtWidgets import (QDialog, QApplication, QLabel, QVBoxLayout, QGridLayout, QWidget)
from PyQt6.QtGui import QPixmap, QIcon
from PyQt6.QtCore import Qt


class Profile(QDialog):
    def __init__(self):
        super().__init__()
        # self.setModal(True)

        self.initializeUI()
        self.show()

    def initializeUI(self):
        """create and arrange widget for window"""
        self.setMaximumSize(400, 400)
        self.setWindowTitle("<b>PROFILE</b>")
        self.setWindowIcon(QIcon("images/quizzla_logo.png"))

        image_path = "images/profile2.png"
        self.image_label = QLabel()
        self.image_label.setPixmap(QPixmap(image_path))
        self.image_label.setMaximumSize(500, 500)
        self.image_label.setScaledContents(True)
        self.image_label.setAlignment(Qt.AlignmentFlag.AlignRight)

        self.fullname = QLabel()
        self.fullname.setText("<b>FULL NAME: </b>" + "Prince Asante")
        self.fullname.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.highest_score = QLabel()
        self.highest_score.setText("<b>HIGHEST SCORE: </b>" + "100")
        self.highest_score.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.highest_score.setObjectName("highestScoreL")
        self.category_name = QLabel()
        self.category_name.setText("<b>CATEGORY: </b>" + "Science")
        self.category_name.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.category_name.setObjectName("categoryHighestL")
        self.badge = QLabel()
        self.badge.setText("<b>BADGE: </b>" + "⭐⭐⭐⭐⭐")
        self.badge.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.badge.setObjectName("badgeL")

        # main layout for the dialog
        main_v_layout = QVBoxLayout()
        main_v_layout.addWidget(self.image_label)
        main_v_layout.addWidget(self.fullname)
        main_v_layout.addWidget(self.highest_score)
        main_v_layout.addWidget(self.category_name)
        main_v_layout.addWidget(self.badge)
        main_v_layout.addStretch()

        self.setLayout(main_v_layout)

    # def loadImage(self, image_path):
    #     image = QLabel(self)
    #     pixmap = QPixmap(image_path)
    #     aspect_ratio = Qt.AspectRatioMode.KeepAspectRatioByExpanding
    #     transform = Qt.TransformationMode.SmoothTransformation
    #     image.setPixmap(pixmap.scaled(image.size(), aspect_ratio, transform))
    #     return image


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window_dialog = Profile()
    sys.exit(app.exec())
