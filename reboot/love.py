import os
import sys
import webbrowser
from PyQt5.QtWidgets import QApplication, QMessageBox
from time import sleep

agreement = """Reconociendonos como seres humanos imperfectos,
con más o menos defectos, decidimos asociarnos en el Team Cachetes
a manera de simbiosis mutualista para avanzar juntos como pareja
hasta donde el universo lo permita."""

agreement = agreement.replace('\n', ' ')

def ask():
    return QMessageBox.question(None, "Will you?", agreement + "\n\nQuieres ser mi novia?",
                         QMessageBox.Yes | QMessageBox.No,
                         QMessageBox.No)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    while True:
        ans = ask()
        if ans == QMessageBox.Yes:
            break
        else:
            sleep(0.25)

    path = os.path.abspath(__file__)
    path = os.path.join(os.path.dirname(path), "us.mp4")
    path = "file://%s" % path
    webbrowser.open(path)
    sys.exit()
