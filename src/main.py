"""
@author Daniel Burrell

"""

from GUI.librarysystem import WelcomeScreen
from PyQt5 import QtWidgets, QtCore




def main():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = WelcomeScreen.getWelcomeScreen(MainWindow)
    ui.screen.show()
    sys.exit(app.exec_())






if __name__ == "__main__":
    main()
    