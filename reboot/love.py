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
if getattr(sys, 'frozen', False):
    path = sys._MEIPASS
else:
    path = os.path.dirname(os.path.abspath(__file__))

print(path)

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

    path = os.path.join(path, "us.mp4")
    path = "file://%s" % path
    print(path)
    webbrowser.open(path)
    sys.exit()
