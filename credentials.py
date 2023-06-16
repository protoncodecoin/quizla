import sys
from PyQt6.QtWidgets import (QApplication, QWidget, QLabel, QPushButton, QButtonGroup, QGroupBox, QLineEdit,
                             QMessageBox, QVBoxLayout, QCheckBox)
from PyQt6.QtGui import QPixmap, QIcon
from PyQt6.QtCore import Qt


class Credentials(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("<h3>QUIZZLA</h3>")
        self.setWindowIcon(QIcon("images/quizzla_logo.png"))
        self.setMaximumSize(500, 500)

        self.initializeUI()
        self.show()

    def initializeUI(self):
        """ create and arrange widget in the window"""
        image_path = "images/quizzla_logo2.png"
        image_label = QLabel("")
        image_label.setPixmap(QPixmap(image_path))
        image_label.setMaximumSize(400, 400)
        image_label.setObjectName("logoBorder")
        image_label.setScaledContents(True)

        # user credentials form
        fullname_label = QLabel("<b>Full Name: </b>")
        fullname_edit = QLineEdit()
        fullname_edit.setPlaceholderText("Enter your full name")
        fullname_edit.setContentsMargins(0, 0, 0, 10)

        # submit btn to submit form
        submit_btn = QPushButton("confirm")
        submit_btn.setObjectName("confirmBtn")

        # quiz category
        category = ["General", "Science", "Music", "Mathematics"]

        # create check box for category
        cat_gb = QGroupBox("Choose Your Field")
        cat_gb.setObjectName("categoryHeading")
        cat_v_layout = QVBoxLayout()

        # QButtonGroup for category
        self.cat_btngroup = QButtonGroup()

        for cat in category:
            cat_widget = QCheckBox(cat)
            if cat == "General":
                cat_widget.setChecked(True)
            cat_v_layout.addWidget(cat_widget)
            self.cat_btngroup.addButton(cat_widget)
        self.cat_btngroup.setExclusive(False)
        cat_gb.setLayout(cat_v_layout)

        # main layout
        main_v_layout = QVBoxLayout()
        main_v_layout.addWidget(image_label)
        main_v_layout.addWidget(fullname_label)
        main_v_layout.addWidget(fullname_edit)
        main_v_layout.addWidget(cat_gb)
        main_v_layout.addSpacing(20)
        main_v_layout.addWidget(submit_btn, 1, Qt.AlignmentFlag.AlignRight)

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
    window = Credentials()
    sys.exit(app.exec())
