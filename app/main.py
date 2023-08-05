#!/usr/bin/env python3

"""Main script for running the arachne AI image generator/display"""

import sys
from PyQt5.QtWidgets import QApplication
import arachne

def main():
    """The main application to launch the window"""
    app = QApplication(sys.argv)
    window = arachne.ImageGenerator()
    window.show()
    return app.exec_()

if __name__ == '__main__':
    sys.exit(main())
