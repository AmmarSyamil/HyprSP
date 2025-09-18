from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout
from list_todo import AppCard
import sys

app = QApplication(sys.argv)

window = QWidget()
layout = QVBoxLayout(window)

card = AppCard(
    title="Test Title",
    due_in="2 days left",
    completed="pending",
    priorities=5
)

layout.addWidget(card)
window.setLayout(layout)
window.show()

sys.exit(app.exec())
