from PyQt6.QtWidgets import QMessageBox


class Avisos():
    def __init__(self, parent=None):
        super().__init__(parent)

    def avisos(self, aviso) -> None:
        match aviso:
            case 'vazio':
                vazio = QMessageBox()
                vazio.setIcon(QMessageBox.warning())
                vazio.setText('campo de url vazia, por favor digite uma url valida')
                vazio.setWindowTitle('Url Vazia')
                vazio.setStandardButtons(QMessageBox.Ok)
                vazio.exec()
            case 'conection':
                net = QMessageBox()
                net.setIcon(QMessageBox.Critical)
                net.setText('Ocorreu algum erro de conexão, por favor verifica seu sinal de internet e tente novamente')
                net.setWindowTitle('No conection')
                net.setStandardButtons(QMessageBox.Ok)
                net.exec()
            case 'sucess':
                sucess = QMessageBox()
                sucess.setIcon(QMessageBox.information)
                sucess.setText('Video baixado com sucesso! Aproveite')
                sucess.setWindowTitle('Sucesso')
                sucess.setStandardButtons(QMessageBox.Ok)
                sucess.exec()
            case 'audio':
                sucess = QMessageBox()
                sucess.setIcon(QMessageBox.warning())
                sucess.setText('Audio baixado com sucesso! Aproveite')
                sucess.setWindowTitle('Sucesso')
                sucess.setStandardButtons(QMessageBox.Ok)
                sucess.exec()
