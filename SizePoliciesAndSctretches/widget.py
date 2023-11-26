from PySide6.QtWidgets import QWidget, QLabel, QLineEdit, QSizePolicy, QHBoxLayout, QVBoxLayout, QPushButton


class Widget(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Size policies")

        #Size policy: how the widgets behaves if container space is expanded or shrunk
        label = QLabel("Some text : ")
        line_edit = QLineEdit()

        #Simulating the defaults. Show vertical expanding and appreciate how weird it is!
        line_edit.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        #line_edit.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        #Make the label expand horizontally
        #label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

        h_layout_1 = QHBoxLayout()
        h_layout_1.addWidget(label)
        h_layout_1.addWidget(line_edit)

        self.setLayout(h_layout_1)