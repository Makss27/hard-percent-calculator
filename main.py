from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QHBoxLayout,
    QVBoxLayout,
    QGroupBox,
    QRadioButton,
    QPushButton,
    QLineEdit,
    QLabel)

def calc(summa_input, percent_input, years_input, layout):
    summa = int(summa_input.text())
    percent = int(percent_input.text())
    years = int(years_input.text())
    percent = percent/100+1
    for i in range(years):
        summa *= percent
    str_summa = str(summa)
    index_dot = str_summa.find(".")
    result = "В итоге ваша сумма составит:\n" + str_summa[0:index_dot+3]
    label = QLabel(result)
    label.setStyleSheet("font-size:20px;color:red")
    layout.addWidget(label)



app = QApplication([])
window = QWidget()
layout = QVBoxLayout()
window.setStyleSheet("background:black;border:2px dashed white")

label_title = QLabel("Калькулятор")
label_title.setStyleSheet("color:yellow;font-size:32px;")
layout.addWidget(label_title)

label_summa = QLabel("Введите сумму вклада")
label_summa.setStyleSheet("color:yellow;font-size:32px;")
layout.addWidget(label_summa)
summa_input = QLineEdit()
summa_input.setStyleSheet("color:yellow;font-size:20px")
layout.addWidget(summa_input)

label_years = QLabel("Введите срок вклада")
label_years.setStyleSheet("color:blue;font-size:32px;")
layout.addWidget(label_years)
years_input = QLineEdit()
years_input.setStyleSheet("color:blue;font-size:20px")
layout.addWidget(years_input)

label_percent = QLabel("Введите процент вклада")
label_percent.setStyleSheet("color:blue;font-size:32px;")
layout.addWidget(label_percent)
percent_input = QLineEdit()
percent_input.setStyleSheet("color:blue;font-size:20px")
layout.addWidget(percent_input)

dtn = QPushButton("Вычеслить")
dtn.clicked.connect(lambda: calc(summa_input, percent_input, years_input, layout))
layout.addWidget(dtn)


window.setLayout(layout)
window.resize(20, 20)
window.setStyleSheet("color:blue;font-size:40px")
dtn.setStyleSheet("color:blue;font-size:40px")
window.show()
app.exec_()


