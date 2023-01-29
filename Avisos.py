from PyQt6.QtWidgets import QMessageBox


class Avisos():

    def avisos(self, aviso) -> None:
        match aviso:
            case 'vazio':
                vazio = QMessageBox()
                vazio.setIcon(QMessageBox.Icon.Information)
                vazio.setText('Url vazia, por favor digite um like valido')
                vazio.setWindowTitle('campo vazio')
                vazio.setStandardButtons(QMessageBox.StandardButton.Ok)
                vazio.exec()
            case 'conection':
                net = QMessageBox()
                net.setIcon(QMessageBox.Icon.Critical)
                net.setText('Ocorreu algum erro de conexão, por favor verifica seu sinal de internet e tente novamente')
                net.setWindowTitle('No conection')
                net.setStandardButtons(QMessageBox.StandardButton.Ok)
                net.exec()
            case 'sucess':
                sucess = QMessageBox()
                sucess.setIcon(QMessageBox.Icon.Information)
                sucess.setText('Video baixado com sucesso! Aproveite')
                sucess.setWindowTitle('Sucesso')
                sucess.setStandardButtons(QMessageBox.StandardButton.Ok)
                sucess.exec()
            case 'audio':
                sucess = QMessageBox()
                sucess.setIcon(QMessageBox.Icon.Warning)
                sucess.setText('Audio baixado com sucesso! Aproveite')
                sucess.setWindowTitle('Sucesso')
                sucess.setStandardButtons(QMessageBox.StandardButton.Ok)
                sucess.exec()
