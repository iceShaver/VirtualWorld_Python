import sys
from PyQt5 import QtGui
from PyQt5.QtCore import Qt

from PyQt5.QtWidgets import QMainWindow, QApplication, QDesktopWidget, QMessageBox, QAction, QStyle, QGridLayout, \
    QPushButton, QLabel, QWidget
from PyQt5.QtGui import QIcon
from Windows import AboutWindow, ReporterWindow, OrganismsWindow, InstructionWindow, NewGameDialog
import Worlds.World
import pickle

# TODO: age increase DONE
# TODO: human special DONE
# TODO: saving/opening game state
# TODO: CyberSheep implementation DONE


class MainWindow(QMainWindow):
    main_icon = QIcon('globe_.svg')

    def __init__(self):
        super().__init__()
        self.init_ui()
        self.about_window = None
        self.reporter_window = None
        self.organisms_window = None
        self.instruction_window = None
        self.new_game_window = None
        self.world = None
        self.world_display_grid = None
        self.game_started = False

    def init_ui(self):

        self.statusBar().showMessage('Ready')
        self.setWindowTitle('Virtual world by Kamil Królikowski 165253')
        self.setWindowIcon(self.main_icon)
        self.resize(1024, 768)
        self.center()
        self.next_round_action = QAction('Next round', self)
        self.next_round_action.setShortcut("Space")
        self.next_round_action.setIcon(self.style().standardIcon(QStyle.SP_ArrowRight))
        self.next_round_action.setStatusTip('Play the next round')
        self.next_round_action.triggered.connect(self.play_next_round)
        self.next_round_action.setEnabled(False)
        new_game_action = QAction('&New game', self)
        new_game_action.setShortcut('Ctrl+N')
        new_game_action.setIcon(self.style().standardIcon(QStyle.SP_FileIcon))
        new_game_action.setStatusTip('Start a new game')
        new_game_action.triggered.connect(self.new_game)
        open_game_action = QAction('&Open game', self)
        open_game_action.setShortcut('Ctrl+O')
        open_game_action.setIcon(self.style().standardIcon(QStyle.SP_DialogOpenButton))
        open_game_action.setStatusTip('Open saved game')
        open_game_action.triggered.connect(self.open_game)
        save_game_action = QAction('&Save game', self)
        save_game_action.setShortcut('Ctrl+S')
        save_game_action.setIcon(self.style().standardIcon(QStyle.SP_DialogSaveButton))
        save_game_action.setStatusTip('Save current game')
        save_game_action.triggered.connect(self.save_game)
        quit_action = QAction('&Quit', self)
        quit_action.setShortcut('Ctrl+Q')
        quit_action.setIcon(self.style().standardIcon(QStyle.SP_DialogCloseButton))
        quit_action.setStatusTip('Quit the game')
        quit_action.triggered.connect(self.quit)
        self.menuBar().addMenu('&Game').addActions(
            [self.next_round_action,
             new_game_action,
             open_game_action,
             save_game_action,
             quit_action]
        )

        show_log_window_action = QAction('&Reporter window', self)
        show_log_window_action.setShortcut('Ctrl+R')
        show_log_window_action.setIcon(self.style().standardIcon(QStyle.SP_MessageBoxInformation))
        show_log_window_action.setStatusTip('Show reporter window')
        show_log_window_action.triggered.connect(self.show_reporter_window)

        show_all_organisms_list_action = QAction('&All Organisms', self)
        show_all_organisms_list_action.setShortcut('Ctrl+A')
        show_all_organisms_list_action.setIcon(self.style().standardIcon(QStyle.SP_FileDialogListView))
        show_all_organisms_list_action.setStatusTip('Show all organisms list window')
        show_all_organisms_list_action.triggered.connect(self.show_organisms_window)
        self.menuBar().addMenu('&View').addActions(
            [show_log_window_action,
             show_all_organisms_list_action]
        )

        show_instruction_window_action = QAction('&Instruction', self)
        show_instruction_window_action.setShortcut('Ctrl+I')
        show_instruction_window_action.setIcon(self.style().standardIcon(QStyle.SP_DialogHelpButton))
        show_instruction_window_action.setStatusTip('Show instruction window')
        show_instruction_window_action.triggered.connect(self.show_instruction_window)
        show_about_window_action = QAction('&About', self)
        show_about_window_action.setShortcut('Ctrl+C')
        show_about_window_action.setIcon(self.style().standardIcon(QStyle.SP_FileDialogInfoView))
        show_about_window_action.setStatusTip('Show about window')
        show_about_window_action.triggered.connect(self.show_about_window)
        self.menuBar().addMenu('&Help').addActions(
            [show_instruction_window_action,
             show_about_window_action]
        )
        self.addToolBar('Menu').addActions(
            [
                self.next_round_action,
                new_game_action,
                open_game_action,
                save_game_action,
                show_log_window_action,
                show_all_organisms_list_action,
                show_instruction_window_action,
                show_about_window_action,
                quit_action
            ]
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
        self.load_icons()
        name, width, height, ok = NewGameDialog.NewGameDialog.get_world_params(self)
        if ok:
            self.world = Worlds.World.World(name, width, height, self)
            central_widget = QWidget()
            self.world_display_grid = QGridLayout()
            self.world_display_grid.setSpacing(0)
            # self.world_display_grid.addWidget()
            for y, row in enumerate(self.world.fields):
                for x, button in enumerate(row):
                    self.world_display_grid.addWidget(button, x, y)
            central_widget.setLayout(self.world_display_grid)
            self.setCentralWidget(central_widget)
            self.next_round_action.setEnabled(True)
            self.game_started = True

    def load_icons(self):
        self.icons = {
            'Antelope': QIcon('./../img/Antelope.png'),
            'CyberSheep': QIcon('./../img/CyberSheep.png'),
            'Dandelion': QIcon('./../img/Dandelion.png'),
            'DeadlyNightshade': QIcon('./../img/DeadlyNightshade.png'),
            'Fox': QIcon('./../img/Fox.png'),
            'Grass': QIcon('./../img/Grass.png'),
            'Guarana': QIcon('./../img/Guarana.png'),
            'HeracleumSosnowskyi': QIcon('./../img/HeracleumSosnowskyi.png'),
            'Human': QIcon('./../img/Human.png'),
            'Sheep': QIcon('./../img/Sheep.png'),
            'Turtle': QIcon('./../img/Turtle.png'),
            'Wolf': QIcon('./../img/Wolf.png')
        }

    def open_game(self):
        pass

    def save_game(self):
        pass

    def quit(self):
        self.close()

    def show_reporter_window(self):
        self.reporter_window = ReporterWindow.ReporterWindow()
        pass

    def show_organisms_window(self):
        self.organisms_window = OrganismsWindow.OrganismsWindow()
        pass

    def show_instruction_window(self):
        self.instruction_window = InstructionWindow.InstructionWindow()
        pass

    def show_about_window(self):
        self.about_window = AboutWindow.AboutWindow()

    def play_next_round(self):
        self.world.play_round()

    def keyPressEvent(self, e):
        if self.game_started:
            if 49 <= e.key() <= 57 or e.key() == Qt.Key_S:
                self.world.handle_human_input(e)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    sys.exit(app.exec_())
