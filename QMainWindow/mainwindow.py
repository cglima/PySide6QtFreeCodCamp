from PySide6.QtWidgets import QMainWindow


class MainWindow(QMainWindow):
    def __init__(self, app):
        super().__init__()
        self.app = app #declare an app member
        self.setWindowTitle("Custom MainWindow")

        # Menubar and menus
        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu("File")
        #file_menu.addAction("Quit")
        quit_action = file_menu.addAction("Quit")
        quit_action.triggered.connect(self.quit_app)

        # Edit menu
        edit_menu = menu_bar.addMenu("Edit")
        edit_menu.addAction("Copy")
        edit_menu.addAction("Cut")
        edit_menu.addAction("Paste")
        edit_menu.addAction("Undo")
        edit_menu.addAction("Redo")

        #A bunch of other menu options just for the fun of it
        menu_bar.addMenu("Window")
        menu_bar.addMenu("Setting")
        menu_bar.addMenu("Help")

    def quit_app(self):
        self.app.quit()