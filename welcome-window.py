import sys
from PyQt6.QtWidgets import (QApplication, QWidget, QVBoxLayout, QLabel, QPushButton)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap, QIcon


class WelcomeMessage(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("<h3>QUIZZLA</h3>")
        self.setWindowIcon(QIcon("images/quizzla_logo.png"))
        self.setMaximumSize(500, 500)

        self.initializeUI()
        self.show()

    def initializeUI(self):
        """create and arrange widget for window"""
        logo_path = "images/quiz_image.jpg"
        logo = QPixmap(logo_path)
        quiz_logo = QLabel("Image here")
        quiz_logo.setPixmap(logo)
        quiz_logo.setObjectName("logoBorder")
        quiz_logo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        quiz_logo.setContentsMargins(10, 10, 10, 10)

        welcome_msg = QLabel()
        welcome_msg.setText("<h3>Welcome to Quizzla</h3>")
        welcome_msg.setWordWrap(True)
        welcome_msg.setObjectName("welcomeMsg")
        welcome_msg.setAlignment(Qt.AlignmentFlag.AlignCenter)

        continue_btn = QPushButton("Continue")
        continue_btn.setObjectName("confirmBtn")

        main_v_layout = QVBoxLayout()
        main_v_layout.addWidget(quiz_logo)
        main_v_layout.addWidget(welcome_msg)
        main_v_layout.addWidget(continue_btn, 1, Qt.AlignmentFlag.AlignCenter)
        main_v_layout.addStretch()

        self.setLayout(main_v_layout)

    def loadImage(self, image_path):
        image = QLabel(self)
        pixmap = QPixmap(image_path)
        aspect_ratio = Qt.AspectRatioMode.KeepAspectRatioByExpanding
        transform = Qt.TransformationMode.SmoothTransformation
        image.setPixmap(pixmap.scaled(image.size(), aspect_ratio, transform))
        return image


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = WelcomeMessage()
    sys.exit(app.exec())
