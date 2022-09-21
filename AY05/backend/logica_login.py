from PyQt5.QtCore import QObject, pyqtSignal


class LogicaLogin(QObject):

    #  Señales
    senal_respuesta_login = pyqtSignal(bool)

    def __init__(self):
        super().__init__()

    def comprobar_usuario(self, usuario, contrasena):
        #  Validar si el usuario y la contraseña es correcta y enviar señal
        if usuario == 'ADMIN' and contrasena == 'IIC2233':
            valido = True
        else:
            valido = False
        self.senal_respuesta_login.emit(valido)
