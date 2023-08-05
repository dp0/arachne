"""
Application to generate and display two captioned images side-by-side
"""

import os
import sys

from PyQt5.QtWidgets import QLabel, QMainWindow, QBoxLayout, QWidget
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtCore import Qt

class CaptionedImage(QWidget):
    """A widget that provides both an image and a caption at the bottom"""
    def __init__(self):
        super().__init__()
        self.image = QLabel()
        self.text = QLabel()

        layout = QBoxLayout(QBoxLayout.TopToBottom)
        layout.setSpacing(0)
        layout.setContentsMargins(0, 0, 0, 0)

        pixmap = QPixmap(os.path.join(os.path.dirname(os.path.realpath(__file__)), '..',
            'resources', 'thinking.png'))
        self.image.setPixmap(pixmap)
        layout.addWidget(self.image)

        self.text.setText('Generating Images...')
        self.text.setFont(QFont('Ubuntu Mono', 20))
        self.text.setAlignment(Qt.AlignCenter)
        self.text.setStyleSheet('background-color: black; color: white;')

        layout.addWidget(self.text)

        self.setLayout(layout)

    def update_content(self, filename, caption):
        """Updates the image and caption for this widget"""
        pixmap = QPixmap(filename)
        self.image.setPixmap(pixmap)
        self.text.setText(caption)


class ImageGenerator(QMainWindow):
    """The window to hold the captioned images"""
    def __init__(self):
        super().__init__()

        layout = QBoxLayout(QBoxLayout.LeftToRight)
        layout.setSpacing(0)
        layout.setContentsMargins(0, 0, 0, 0)

        self.image_left = CaptionedImage()
        layout.addWidget(self.image_left)

        self.image_right = CaptionedImage()
        layout.addWidget(self.image_right)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        self.resize(1024,600)
        self.showFullScreen()

    def update_image(self, left_path, left_caption, right_path, right_caption):
        """Updates the images and captions"""
        self.image_left.update_content(left_path, left_caption)
        self.image_right.update_content(right_path, right_caption)
