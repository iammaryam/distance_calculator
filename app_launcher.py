from PySide2.QtCore import QSize
from PySide2.QtGui import QFont
from PySide2.QtWidgets import (
    QApplication,
    QComboBox,
    QLabel,
    QMainWindow,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QWidget
)

from app_funcs import geo_coordinate

from app_funcs import distance


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(QSize(400, 700))
        self.setWindowTitle("Distance calculater")

        layout = QVBoxLayout()
        layout_1 = QVBoxLayout()
        layout_2 = QVBoxLayout()
        layout_3 = QVBoxLayout()
        layout_4 = QVBoxLayout()

        layout.setContentsMargins(40, 50, 30, 60)
        layout.setSpacing(70)

        layout_1.setSpacing(5)
        layout_2.setSpacing(5)
        layout_4.setSpacing(15)

        label_1 = QLabel()
        label_1.setText('First Place Name :')
        layout_1.addWidget(label_1)

        self.line_edit_1 = QLineEdit()
        self.line_edit_1.setFixedSize(QSize(270, 40))
        self.line_edit_1.setFont(QFont('Arial', 15))
        self.line_edit_1.setTextMargins(30, 0, 0, 0)
        layout_1.addWidget(self.line_edit_1)

        layout.addLayout(layout_1)

        label_2 = QLabel()
        label_2.setText('Second Place Name :')
        layout_2.addWidget(label_2)

        self.line_edit_2 = QLineEdit()
        self.line_edit_2.setFixedSize(QSize(270, 40))
        self.line_edit_2.setFont(QFont('Arial', 15))
        self.line_edit_2.setTextMargins(30, 0, 0, 0)
        layout_2.addWidget(self.line_edit_2)

        layout.addLayout(layout_2)

        self.combobox = QComboBox()
        self.combobox.setFixedSize(QSize(200, 50))
        self.combobox.addItems(["Kilometer (km)", "Meter (m)", "Mile (mi)"])
        layout_3.addWidget(self.combobox)

        layout.addLayout(layout_3)

        button = QPushButton("Calculate")
        button.setFixedSize(QSize(200, 50))
        button.clicked.connect(self.button_clicked)
        layout_4.addWidget(button)

        self.line_edit_3 = QLineEdit()
        self.line_edit_3.setFixedSize(QSize(270, 60))
        self.line_edit_3.setFont(QFont('Arial', 20))
        self.line_edit_3.setTextMargins(30, 0, 0, 0)
        layout_4.addWidget(self.line_edit_3)

        layout.addLayout(layout_4)

        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)

    def button_clicked(self):
        geo_city_one = geo_coordinate(self.line_edit_1.text())
        geo_city_two = geo_coordinate(self.line_edit_2.text())
        text = str(self.combobox.currentText())
        dist = distance(geo_city_one, geo_city_two, text)
        self.line_edit_3.setText(dist)


if __name__ == "__main__":
    app = QApplication([])
    mainWin = MainWindow()
    mainWin.show()
    app.exec_()
