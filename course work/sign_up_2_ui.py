# Form implementation generated from reading ui file 'd:\Навчання\2 курс\2\course work\sign_up_2.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_sign_up_2(object):
    def setupUi(self, sign_up_2):
        sign_up_2.setObjectName("sign_up_2")
        sign_up_2.resize(440, 500)
        self.centralwidget = QtWidgets.QWidget(parent=sign_up_2)
        self.centralwidget.setObjectName("centralwidget")
        self.image = QtWidgets.QLabel(parent=self.centralwidget)
        self.image.setGeometry(QtCore.QRect(0, 0, 450, 500))
        self.image.setText("")
        self.image.setPixmap(QtGui.QPixmap("d:\\Навчання\\2 курс\\2\\course work\\4a7eaeae52140c9205af389cc1e2c7b7-Enhanced-transformed (1).jpeg"))
        self.image.setObjectName("image")
        self.main_lable = QtWidgets.QLabel(parent=self.centralwidget)
        self.main_lable.setGeometry(QtCore.QRect(160, 30, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.main_lable.setFont(font)
        self.main_lable.setStyleSheet("background-color: rgb(149, 223, 223);")
        self.main_lable.setObjectName("main_lable")
        self.label_addres = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_addres.setGeometry(QtCore.QRect(50, 80, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        self.label_addres.setFont(font)
        self.label_addres.setStyleSheet("background-color: rgb(149, 223, 223);")
        self.label_addres.setObjectName("label_addres")
        self.label_name_ed_institution = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_name_ed_institution.setGeometry(QtCore.QRect(10, 180, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        self.label_name_ed_institution.setFont(font)
        self.label_name_ed_institution.setStyleSheet("background-color: rgb(149, 223, 223);")
        self.label_name_ed_institution.setObjectName("label_name_ed_institution")
        self.back3 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.back3.setGeometry(QtCore.QRect(100, 430, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.back3.setFont(font)
        self.back3.setStyleSheet("background-color: rgb(255, 170, 0);\n"
"color: rgb(255, 255, 255);")
        self.back3.setObjectName("back3")
        self.submit3 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.submit3.setGeometry(QtCore.QRect(250, 430, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.submit3.setFont(font)
        self.submit3.setStyleSheet("background-color: rgb(255, 170, 0);\n"
"color: rgb(255, 255, 255);")
        self.submit3.setObjectName("submit3")
        self.comboBox_ed_level = QtWidgets.QComboBox(parent=self.centralwidget)
        self.comboBox_ed_level.setGeometry(QtCore.QRect(170, 130, 251, 31))
        self.comboBox_ed_level.setObjectName("comboBox_ed_level")
        self.comboBox_ed_level.addItem("")
        self.comboBox_ed_level.setItemText(0, "")
        self.comboBox_ed_level.addItem("")
        self.comboBox_ed_level.addItem("")
        self.comboBox_ed_level.addItem("")
        self.comboBox_ed_level.addItem("")
        self.comboBox_ed_level.addItem("")
        self.label_ed_level = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_ed_level.setGeometry(QtCore.QRect(60, 130, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        self.label_ed_level.setFont(font)
        self.label_ed_level.setStyleSheet("background-color: rgb(149, 223, 223);")
        self.label_ed_level.setObjectName("label_ed_level")
        self.label_num_atestat = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_num_atestat.setGeometry(QtCore.QRect(40, 230, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        self.label_num_atestat.setFont(font)
        self.label_num_atestat.setStyleSheet("background-color: rgb(149, 223, 223);")
        self.label_num_atestat.setObjectName("label_num_atestat")
        self.label_num_dodatok = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_num_dodatok.setGeometry(QtCore.QRect(40, 280, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        self.label_num_dodatok.setFont(font)
        self.label_num_dodatok.setStyleSheet("background-color: rgb(149, 223, 223);")
        self.label_num_dodatok.setObjectName("label_num_dodatok")
        self.label_faculty = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_faculty.setGeometry(QtCore.QRect(80, 330, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        self.label_faculty.setFont(font)
        self.label_faculty.setStyleSheet("background-color: rgb(149, 223, 223);")
        self.label_faculty.setObjectName("label_faculty")
        self.label_benefits = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_benefits.setGeometry(QtCore.QRect(110, 380, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        self.label_benefits.setFont(font)
        self.label_benefits.setStyleSheet("background-color: rgb(149, 223, 223);")
        self.label_benefits.setObjectName("label_benefits")
        self.comboBox_faculty = QtWidgets.QComboBox(parent=self.centralwidget)
        self.comboBox_faculty.setGeometry(QtCore.QRect(170, 330, 251, 31))
        self.comboBox_faculty.setObjectName("comboBox_faculty")
        self.comboBox_faculty.addItem("")
        self.comboBox_faculty.setItemText(0, "")
        self.comboBox_faculty.addItem("")
        self.comboBox_faculty.addItem("")
        self.comboBox_faculty.addItem("")
        self.comboBox_benefits = QtWidgets.QComboBox(parent=self.centralwidget)
        self.comboBox_benefits.setGeometry(QtCore.QRect(170, 380, 251, 31))
        self.comboBox_benefits.setObjectName("comboBox_benefits")
        self.comboBox_benefits.addItem("")
        self.comboBox_benefits.setItemText(0, "")
        self.comboBox_benefits.addItem("")
        self.comboBox_benefits.addItem("")
        self.comboBox_benefits.addItem("")
        self.comboBox_benefits.addItem("")
        self.lineEdit = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(170, 80, 251, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(170, 180, 251, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(170, 230, 251, 31))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(170, 280, 251, 31))
        self.lineEdit_4.setObjectName("lineEdit_4")
        sign_up_2.setCentralWidget(self.centralwidget)

        self.retranslateUi(sign_up_2)
        QtCore.QMetaObject.connectSlotsByName(sign_up_2)

    def retranslateUi(self, sign_up_2):
        _translate = QtCore.QCoreApplication.translate
        sign_up_2.setWindowTitle(_translate("sign_up_2", "Реєстрація"))
        self.main_lable.setText(_translate("sign_up_2", "Реєстрація"))
        self.label_addres.setToolTip(_translate("sign_up_2", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.label_addres.setText(_translate("sign_up_2", "Повна адреса"))
        self.label_name_ed_institution.setToolTip(_translate("sign_up_2", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.label_name_ed_institution.setText(_translate("sign_up_2", "Назва навч. закладу"))
        self.back3.setText(_translate("sign_up_2", "Назад"))
        self.submit3.setText(_translate("sign_up_2", "Підтвердити"))
        self.comboBox_ed_level.setItemText(1, _translate("sign_up_2", "початкова освіта"))
        self.comboBox_ed_level.setItemText(2, _translate("sign_up_2", "базова середня освіта"))
        self.comboBox_ed_level.setItemText(3, _translate("sign_up_2", "профільна середня освіта"))
        self.comboBox_ed_level.setItemText(4, _translate("sign_up_2", "фахова передвища освіта"))
        self.comboBox_ed_level.setItemText(5, _translate("sign_up_2", "вища освіта"))
        self.label_ed_level.setToolTip(_translate("sign_up_2", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.label_ed_level.setText(_translate("sign_up_2", "Рівень освіти"))
        self.label_num_atestat.setToolTip(_translate("sign_up_2", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.label_num_atestat.setText(_translate("sign_up_2", "Номер атестату"))
        self.label_num_dodatok.setToolTip(_translate("sign_up_2", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.label_num_dodatok.setText(_translate("sign_up_2", "Номер додатку"))
        self.label_faculty.setToolTip(_translate("sign_up_2", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.label_faculty.setText(_translate("sign_up_2", "Факультет"))
        self.label_benefits.setToolTip(_translate("sign_up_2", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.label_benefits.setText(_translate("sign_up_2", "Квоти"))
        self.comboBox_faculty.setItemText(1, _translate("sign_up_2", "Англійської мови"))
        self.comboBox_faculty.setItemText(2, _translate("sign_up_2", "Географії"))
        self.comboBox_faculty.setItemText(3, _translate("sign_up_2", "Української мови"))
        self.comboBox_benefits.setItemText(1, _translate("sign_up_2", "Квота-1"))
        self.comboBox_benefits.setItemText(2, _translate("sign_up_2", "Квота-2"))
        self.comboBox_benefits.setItemText(3, _translate("sign_up_2", "Квота-3"))
        self.comboBox_benefits.setItemText(4, _translate("sign_up_2", "Квота-іноземців"))