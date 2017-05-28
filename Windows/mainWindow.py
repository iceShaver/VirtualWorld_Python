import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QDesktopWidget, QMessageBox, QAction
from PyQt5.QtGui import QIcon


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.statusBar().showMessage('Ready')
        self.setWindowTitle('Virtual world by Kamil Królikowski 165253')
        self.setWindowIcon(QIcon('globe_.svg'))
        self.resize(1024, 768)
        self.center()

        new_game_action = QAction('&New game', self)
        new_game_action.setShortcut('Ctrl+N')
        new_game_action.setStatusTip('Start a new game')
        new_game_action.triggered.connect(self.new_game)
        open_game_action = QAction('&Open game', self)
        open_game_action.setShortcut('Ctrl+O')
        open_game_action.setStatusTip('Open saved game')
        open_game_action.triggered.connect(self.open_game)
        save_game_action = QAction('&Save game', self)
        save_game_action.setShortcut('Ctrl+S')
        save_game_action.setStatusTip('Save current game')
        save_game_action.triggered.connect(self.save_game)
        quit_action = QAction('&Quit', self)
        quit_action.setShortcut('Ctrl+Q')
        quit_action.setStatusTip('Quit the game')
        quit_action.triggered.connect(self.quit)
        self.menuBar().addMenu('&Game').addActions(
            [new_game_action,
             open_game_action,
             save_game_action,
             quit_action]
        )

        show_log_window_action = QAction('&Reporter window', self)
        show_log_window_action.setShortcut('Ctrl+R')
        show_log_window_action.setStatusTip('Show reporter window')
        show_log_window_action.triggered.connect(self.show_reporter_window)

        show_all_organisms_list_action = QAction('&All Organisms', self)
        show_all_organisms_list_action.setShortcut('Ctrl+A')
        show_all_organisms_list_action.setStatusTip('Show all organisms list window')
        show_all_organisms_list_action.triggered.connect(self.show_organisms_window)
        self.menuBar().addMenu('&View').addActions(
            [show_log_window_action,
             show_all_organisms_list_action]
        )

        show_instruction_window_action = QAction('&Instruction', self)
        show_instruction_window_action.setShortcut('Ctrl+I')
        show_instruction_window_action.setStatusTip('Show instruction window')
        show_instruction_window_action.triggered.connect(self.show_instruction_window)
        show_about_window_action = QAction('&About', self)
        show_about_window_action.setShortcut('Ctrl+C')
        show_about_window_action.setStatusTip('Show about window')
        show_about_window_action.triggered.connect(self.show_about_window)
        self.menuBar().addMenu('&Help').addActions(
            [show_instruction_window_action,
             show_about_window_action]
        )

        self.show()

    def center(self):
        window_geometry = self.frameGeometry()
        center_point = QDesktopWidget().availableGeometry().center()
        window_geometry.moveCenter(center_point)
        self.move(window_geometry.topLeft())

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Confirm operation', 'Do you really want to quit?',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def new_game(self):
        pass

    def open_game(self):
        pass

    def save_game(self):
        pass

    def quit(self):
        self.close()

    def show_reporter_window(self):
        pass

    def show_organisms_window(self):
        pass

    def show_instruction_window(self):
        pass

    def show_about_window(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    sys.exit(app.exec_())
