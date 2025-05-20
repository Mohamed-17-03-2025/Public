import sys
import json
from pathlib import Path
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QVBoxLayout, QWidget, QPushButton, QHBoxLayout
from PyQt5.QtCore import Qt, QRect, QPoint
from PyQt5.QtGui import QColor

class StickyNote(QMainWindow):
    def __init__(self):
        
        super().__init__()
        self.setWindowTitle("Sticky Note")
        
        # Use Tool window to minimize taskbar presence, stay on bottom
        self.setWindowFlags(Qt.Tool | Qt.WindowStaysOnBottomHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        # Main widget and layout
        self.central_widget = QWidget()
        self.central_widget.setStyleSheet("background-color: #FFFF99; border: 2px solid #333333; border-radius: 5px;")
        self.setCentralWidget(self.central_widget)
        self.main_layout = QVBoxLayout(self.central_widget)
        self.main_layout.setContentsMargins(10, 10, 10, 10)

        # Top bar for close button
        self.top_bar = QWidget()
        self.top_layout = QHBoxLayout(self.top_bar)
        self.top_layout.setContentsMargins(0, 0, 0, 0)
        self.top_layout.addStretch()
        self.close_button = QPushButton("×")
        self.close_button.setFixedSize(20, 20)
        self.close_button.setStyleSheet("background-color: #FF9999; border: none; font-weight: bold; border-radius: 3px;")
        self.close_button.clicked.connect(self.close)
        self.top_layout.addWidget(self.close_button)
        self.main_layout.addWidget(self.top_bar)

        # Text area
        self.text_edit = QTextEdit()
        self.text_edit.setStyleSheet("background-color: #FFFF99; border: none; font-size: 14px; font-family: Arial;")
        self.text_edit.textChanged.connect(self.save_note)
        self.main_layout.addWidget(self.text_edit)

        # File path for saving note data
        self.file_path = Path.home() / "sticky_note.json"

        # Load saved note data
        self.load_note()

        # Variables for dragging
        self.dragging = False
        self.offset = None

    def load_note(self):
        if self.file_path.exists():
            with open(self.file_path, "r") as f:
                data = json.load(f)
                self.text_edit.setPlainText(data.get("text", ""))
                geometry = data.get("geometry", [100, 100, 300, 200])
                self.setGeometry(*geometry)
        else:
            self.setGeometry(100, 100, 300, 200)

    def save_note(self):
        
        data = {
                "text": self.text_edit.toPlainText(),
                "geometry": [self.x(), self.y(), self.width(), self.height()]
               }
        
        with open(self.file_path, "w") as f:
            json.dump(data, f)

    def mousePressEvent(self, event):
        
        if event.button() == Qt.LeftButton and not self.close_button.underMouse():
            self.dragging = True
            self.offset = event.pos()

    def mouseMoveEvent(self, event):
        
        if self.dragging:
            self.move(self.mapToParent(event.pos() - self.offset))

    def mouseReleaseEvent(self, event):
        
        if event.button() == Qt.LeftButton:
            self.dragging = False
            self.save_note()

    def resizeEvent(self, event):
        
        super().resizeEvent(event)
        self.save_note()

if __name__ == "__main__":
    
    app = QApplication(sys.argv)
    
    note = StickyNote()
    note.show()
    
    sys.exit(app.exec_())
