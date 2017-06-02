from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QSpinBox, QGridLayout, QDialog, QPushButton, QVBoxLayout, \
    QDialogButtonBox, QSizePolicy
import PyQt5.Qt

from Windows import MainWindow


class NewGameDialog(QDialog):
    def __init__(self, parent):
        super().__init__(parent)
        self.init_ui()

    def init_ui(self):
        self.resize(400, 0)
        self.setWindowTitle('New game - Virtual world')
        self.setWindowIcon(MainWindow.MainWindow.main_icon)
        name_label = QLabel('Name')
        width_label = QLabel('World width')
        height_label = QLabel('World height')
        self.name = QLineEdit(self)
        self.width = QSpinBox(self)
        self.height = QSpinBox(self)
        content = QWidget()
        content_layout = QGridLayout();
        content_layout.addWidget(name_label, 0, 0)
        content_layout.addWidget(width_label, 1, 0)
        content_layout.addWidget(height_label, 2, 0)
        content_layout.addWidget(self.name, 0, 1)
        content_layout.addWidget(self.width, 1, 1)
        content_layout.addWidget(self.height, 2, 1)
        content.setLayout(content_layout)
        self.width.setRange(10, 50)
        self.width.setValue(30)
        self.height.setRange(10, 50)
        self.height.setValue(20)
        self.name.setText('New World')
        layout = QVBoxLayout(self)
        layout.addWidget(content)
        buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel, self)
        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)
        layout.addWidget(buttons)
        self.show()

    def params(self):
        return self.name.text(), self.width.value(), self.height.value()

    @staticmethod
    def get_world_params(parent=None):
        dialog = NewGameDialog(parent)
        result = dialog.exec_()
        name, width, height = dialog.params()
        return name, width, height, result == QDialog.Accepted