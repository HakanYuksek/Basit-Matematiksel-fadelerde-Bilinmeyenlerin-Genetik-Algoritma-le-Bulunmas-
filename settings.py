from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox


class Ui_Dialog(object):
    def setupUi(self, Ui_Dialog,Dialog,population_size = 15, mutation_rate = 15,selection_method = "roulette_wheel",
                cross_over_method = "order_based", max_generation_size = 1000,Ui_MainWindow = 0):

        self.Dialog = Dialog
        self.MainWindow = Ui_MainWindow
                
        Dialog.setObjectName("Dialog")
        Dialog.resize(408, 273)
        Dialog.setFixedSize(408, 273)
        Dialog.setStyleSheet("background-color: rgb(85, 85, 255);\n"
"color: rgb(255, 255, 255);")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 10, 401, 31))
        self.label.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(-10, 40, 481, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.formLayoutWidget = QtWidgets.QWidget(Dialog)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 60, 387, 147))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";")
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.spinBox = QtWidgets.QSpinBox(self.formLayoutWidget)
        self.spinBox.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.spinBox.setAlignment(QtCore.Qt.AlignCenter)
        self.spinBox.setMinimum(1)
        self.spinBox.setMaximum(100)
        self.spinBox.setObjectName("spinBox")
        self.spinBox.setValue(mutation_rate)
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.spinBox)
        self.spinBox_2 = QtWidgets.QSpinBox(self.formLayoutWidget)
        self.spinBox_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 0, 0);\n"
"")
        self.spinBox_2.setAlignment(QtCore.Qt.AlignCenter)
        self.spinBox_2.setMinimum(15)
        self.spinBox_2.setMaximum(1000)
        self.spinBox_2.setObjectName("spinBox_2")
        self.spinBox_2.setValue(population_size)
        
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.spinBox_2)
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_4.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";")
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.comboBox = QtWidgets.QComboBox(self.formLayoutWidget)
        self.comboBox.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.comboBox)
        self.label_5 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_5.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";")
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.comboBox_2 = QtWidgets.QComboBox(self.formLayoutWidget)
        self.comboBox_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.comboBox_2)
        self.label_6 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_6.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";")
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.spinBox_3 = QtWidgets.QSpinBox(self.formLayoutWidget)
        self.spinBox_3.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.spinBox_3.setAlignment(QtCore.Qt.AlignCenter)
        self.spinBox_3.setMinimum(1)
        self.spinBox_3.setMaximum(2000)
        self.spinBox_3.setObjectName("spinBox_3")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.spinBox_3)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_3.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";\n"
"font: 75 16pt \"MS Shell Dlg 2\";")
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(210, 220, 131, 31))
        self.pushButton_2.setStyleSheet("background-color: rgb(240, 240, 240);\n"
"color: rgb(0, 0, 0);\n"
"")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(60, 220, 131, 31))
        self.pushButton_3.setStyleSheet("background-color: rgb(240, 240, 240);\n"
"color: rgb(0, 0, 0);\n"
"")
        self.pushButton_3.setObjectName("pushButton_3")

        if selection_method == "roulette_wheel":
            self.comboBox.setCurrentIndex(0)
        else:
            self.comboBox.setCurrentIndex(1)

        if cross_over_method == "order_based":
            self.comboBox_2.setCurrentIndex(1)
        else:
            self.comboBox_2.setCurrentIndex(0)
        
        self.spinBox_3.setValue(max_generation_size)

        self.pushButton_2.clicked.connect(self.exit)
        self.pushButton_3.clicked.connect(self.save_changes)
        
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Ayarlar"))
        self.label.setText(_translate("Dialog", "GENETİK ALGORİTMA HİPERPARAMETRELER"))
        self.label_2.setText(_translate("Dialog", "Popülasyon Boyutu"))
        self.label_4.setText(_translate("Dialog", "Seçme Yöntemi"))
        self.comboBox.setItemText(0, _translate("Dialog", "Rulet Tekeri"))
        self.comboBox.setItemText(1, _translate("Dialog", "Sıralama Seçimi"))
        self.label_5.setText(_translate("Dialog", "Çaprazlama Yöntemi"))
        self.comboBox_2.setItemText(0, _translate("Dialog", "Uniform Crossover"))
        self.comboBox_2.setItemText(1, _translate("Dialog", "Order-Based Crossover"))
        self.label_6.setText(_translate("Dialog", "Max Jenerasyon Sayısı"))
        self.label_3.setText(_translate("Dialog", "Mutasyon Olasılığı"))
        self.pushButton_2.setText(_translate("Dialog", "ÇIKIŞ"))
        self.pushButton_3.setText(_translate("Dialog", "KAYDET"))

    # This method provides to hide this window
    def exit(self):
        self.Dialog.hide()

    # This method saves the changes and close the window
    def save_changes(self):

        self.MainWindow.population_size = int(self.spinBox_2.value())
        self.MainWindow.mutation_rate = int(self.spinBox.value())
        if self.comboBox.currentText() == "Rulet Tekeri":
            self.MainWindow.selection_method = "roulette_wheel"
        else:
            self.MainWindow.selection_method = "selection"

        if self.comboBox_2.currentText() == "Order-Based Crossover":
            self.MainWindow.cross_over_method = "order_based"
        else:
            self.MainWindow.cross_over_method = "uniform"
            
        self.MainWindow.max_generation_size = int(self.spinBox_3.value())

        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText("Değişiklikler Kaydedildi...")
        msgBox.setWindowTitle("Bilgi Mesajı")
        ret = msgBox.exec_()  

        self.Dialog.hide()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
