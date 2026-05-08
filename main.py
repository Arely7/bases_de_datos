import sys
from PyQt6 import QtWidgets
from main_controller import MainController
#pip freeze > requirements.txt

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainController()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()