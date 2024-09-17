from PyQt5 import  uic,QtWidgets

def funcao_principal():
    linha1 = formulario.lineEdit.text()
    linha2 = formulario.lineEdit_2.text()
    linha3 = formulario.lineEdit_3.text()
    
    if formulario.radioButton.isChecked() :
        print("Projeto em 'Development'.")
    elif formulario.radioButton_2.isChecked() :
        print("Projeto em 'Staging'.")
    else :
        print("Projeto em 'Production'.")

    print("Nome do Projeto:",linha1)
    print("Tipo do Projeto:",linha2)
    print("Descrição do Projeto",linha3)
    

app=QtWidgets.QApplication([])
formulario=uic.loadUi("formulario.ui")
formulario.pushButton.clicked.connect(funcao_principal)

formulario.show()
app.exec()