from PyQt5 import uic,QtWidgets

def funcao_principal():
    linha1 = tela.lineEdit.text()
    linha2 = tela.lineEdit_2.text()
    linha3 = tela.spinBox.text()
    linha4 = tela.spinBox_2.text()
    linha5 = tela.spinBox_4.text()
    linha6 = tela.spinBox_3.text()
    linha7 = tela.spinBox_5.text()
    linha8 = tela.spinBox_6.text()
    linha9 = tela.spinBox_7.text()
    linha10 = tela.spinBox_8.text()
    linha11 = tela.spinBox_9.text()
    linha12 = tela.spinBox_10.text()




    print("mandante",linha1)
    print("Visitante", linha2)
    print("Gol Mandante", linha3)
    print("GOl Visitante", linha4)
    print("Escanteios Mandante", linha5)
    print("Escanteios Visitante", linha6)
    print("Finalizações Mandante", linha7)
    print("Finalizações Visitante", linha8)
    print("Cartões Amarelos Mandante", linha9)
    print("Cartões Amarelos Visitante", linha10)
    print("Laterais mandante", linha11)
    print("Laterais Visitante", linha12)

app=QtWidgets.QApplication([])
tela=uic.loadUi("tela.ui")
tela.pushButton.clicked.connect(funcao_principal)

tela.show()
app.exec()
