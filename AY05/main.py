import sys
from PyQt5.QtWidgets import QApplication
from frontend.ventana_login import VentanaLogin
from frontend.ventana_principal import VentanaPrincipal
from backend.logica_login import LogicaLogin

# Función para debuggear


def hook(type, value, traceback):
    print(type)
    print(traceback)
    sys.__excepthook__ = hook

# Se instancia la aplicación
app = QApplication([])


# Se instancian las clases
ventana_login = VentanaLogin()
ventana_principal = VentanaPrincipal()
logica_login = LogicaLogin()

# Se conectan las señales
ventana_login.senal_enviar_login(logica_login.comprobar_usuario)
logica_login.senal_respuesta_login.connect(ventana_login.recibir_login)
ventana_login.senal_abrir_ventana_principal.connect(ventana_principal.mostrar)

# Se muestra la ventana de login
ventana_login.show()

sys.exit(app.exec_())
