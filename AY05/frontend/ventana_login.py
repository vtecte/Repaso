import os
from PyQt5.QtWidgets import (QWidget, QPushButton, QLabel,
                             QHBoxLayout, QVBoxLayout, QLineEdit)
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QPixmap


class VentanaLogin(QWidget):

    #  Señales
    senal_enviar_login = pyqtSignal(str, str)
    senal_abrir_ventana_principal = pyqtSignal(str)

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

        # Usuario
        self.usuario = QLabel('Ingrese su nombre de usuario: ', self)
        self.usuario_ingresar = QLineEdit('')

        # Contraseña
        self.contrasena = QLabel('Ingrese su contrasena: ', self)
        self.contrasena_ingresar = QLineEdit('')
        self.contrasena_ingresar.setEchoMode(QLineEdit.EchoMode.Password)

        # Boton
        self.boton_inicio = QPushButton('Iniciar sesion', self)
        self.boton_inicio.clicked.connect(self.enviar_login)

        # Layouts
        hbox_usuario = QHBoxLayout()
        hbox_usuario.addWidget(self.usuario)
        hbox_usuario.addWidget(self.usuario_ingresar)

        hbox_contrasena = QHBoxLayout()
        hbox_contrasena.addWidget(self.contrasena)
        hbox_contrasena.addWidget(self.contrasena)

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addWidget(self.logo)
        vbox.addStretch(3)
        vbox.addLayout(hbox_usuario)
        vbox.addLayout(hbox_contrasena)
        vbox.addStretch(1)
        vbox.addWidget(self.boton_inicio)
        vbox.addStretch(1)

        self.setLayout(vbox)

    def enviar_login(self):
        # Enviar señal para validar login
        usuario = self.usuario_ingresar.text()
        contrasena = self.contrasena_ingresar.text()
        self.senal_enviar_login.emit(usuario, contrasena)

    def recibir_login(self, valido):
        # Abrir ventana principal si es correcto el login
        if valido:
            self.hide()
            usuario = self.usuario_ingresar.text()
            self.senal_abrir_ventana_principal.emit(usuario)
        else:
            self.usuario_ingresar.setText('Invalido')
            self.contrasena_ingresar.setText('')
