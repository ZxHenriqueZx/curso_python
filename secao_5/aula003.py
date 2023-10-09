# QWidget e QLayout de PySide6.QtWidgets
# QWidget -> genérico
# QLayout -> Um widget de layout que recebe outros widgets
# QMainWindow e centralWidget
# -> QApplication (app)
#   -> QMainWindow (window->setCentralWidget)
#       -> CentralWidget (central_widget)
#           -> Layout (layout)
#               -> Widget 1 (botao1)
#               -> Widget 2 (botao2)
#               -> Widget 3 (botao3)
#   -> show
# -> exec
import sys

from PySide6.QtWidgets import (QApplication, QGridLayout, QPushButton, QWidget,
                               QMainWindow)

#Cria a aplicação
app = QApplication(sys.argv)

#Cria a janela principal
window = QMainWindow()
central_widget = QWidget()
window.setCentralWidget(central_widget)
window.setWindowTitle('Teste Título')

#Botoes
botao = QPushButton('Texto do botão')
botao.setStyleSheet('font-size: 80px;')

botao2 = QPushButton('Botão 2')
botao2.setStyleSheet('font-size: 40px;')

botao3 = QPushButton('Botão 3')
botao3.setStyleSheet('font-size: 40px;')

#configura o layout
layout = QGridLayout()
central_widget.setLayout(layout)
layout.addWidget(botao, 1, 1, 1, 1)
layout.addWidget(botao2, 1, 2, 1, 1)
layout.addWidget(botao3, 3, 1, 1, 2)

#status bar
status_bar = window.statusBar()
status_bar.showMessage('Hello World')

#menu
def mostrar():
    print('Hello World!!')

menu = window.menuBar()
menu_1 = menu.addMenu('Teste menu')
acao_1 = menu_1.addAction('Teste ação')
acao_1.triggered.connect(mostrar)


#executa a aplicação
window.show()  # Central widget entre na hierarquia e mostre sua janela
app.exec()  # O loop da aplicação
