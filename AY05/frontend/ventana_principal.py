import os
from PyQt5.QtWidgets import (QWidget, QLabel, QHBoxLayout, QVBoxLayout)
from PyQt5.QtGui import QPixmap


class VentanaPrincipal(QWidget):

    def __init__(self):
        super().__init__()
        self.init_gui()

    def init_gui(self):

        # Ventana
        self.setGeometry(400, 300, 500, 500)
        self.setWindowTitle('AvanzadaApp')

        # Imagen
        self.logo = QLabel(self)
        self.logo.setGeometry(100, 100, 100, 100)
        path_logo = os.path.join('img', 'logo.png')
        pixeles = QPixmap(path_logo)
        self.logo.setPixmap(pixeles)
        self.logo.setScaledContents(True)

        # Bienvenida
        self.bienvenida = QLabel('Bienvenido', self)

        # Layouts
        hbox_logo = QHBoxLayout()
        hbox_logo.addWidget(self.logo)
        
        hbox_bienvenida = QHBoxLayout()
        hbox_bienvenida.addStretch(1)
        hbox_bienvenida.addWidget(self.bienvenida)
        hbox_bienvenida.addStretch(1)

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addWidget(hbox_logo)
        vbox.addStretch(3)
        vbox.addWidget(hbox_bienvenida)
        vbox.addStretch(1)

        self.setLayout(vbox)

    def mostrar(self, nombre):
        #Mostrar ventana y mensaje de bienvenida
        self.bienvenida.setText(f'Bienvenid@ {nombre}')
        self.show()
        