import sys
from os import rename, listdir
from os.path import basename, splitext
from pytils import translit
from PyQt5.QtWidgets import (QApplication, QMainWindow)
from PyQt5.uic import loadUi


class Transliterator(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.initUi()
        self.initSignal()

    def initUi(self):
        loadUi('ui_transliterator.ui', self)

    def initSignal(self):
        self.startButton.clicked.connect(self.work_transliterator)

    def work_transliterator(self):
        path = self.directory.toPlainText()
        list_file = listdir(path)
        for n in list_file:
            transl_file_name = translit.slugify(splitext(basename(n))[0])
            extension_file = splitext(n)[1]
            rename(path + '\\' + n, path + '\\' + transl_file_name + extension_file)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    Transliterator = Transliterator()
    Transliterator.show()
    sys.exit(app.exec_())
