# Form implementation generated from reading ui file 'd:\Навчання\2 курс\2\course work\sign_up_1.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_sign_up_1(object):
    def setupUi(self, sign_up_1):
        sign_up_1.setObjectName("sign_up_1")
        sign_up_1.resize(450, 500)
        self.centralwidget = QtWidgets.QWidget(parent=sign_up_1)
        self.centralwidget.setObjectName("centralwidget")
        self.signUp1 = QtWidgets.QLabel(parent=self.centralwidget)
        self.signUp1.setGeometry(QtCore.QRect(0, 0, 450, 500))
        self.signUp1.setText("")
        self.signUp1.setPixmap(QtGui.QPixmap("d:\\Навчання\\2 курс\\2\\course work\\4a7eaeae52140c9205af389cc1e2c7b7-Enhanced-transformed (1).jpeg"))
        self.signUp1.setObjectName("signUp1")
        self.main_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.main_label.setGeometry(QtCore.QRect(160, 40, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.main_label.setFont(font)
        self.main_label.setStyleSheet("background-color: rgb(149, 223, 223);")
        self.main_label.setObjectName("main_label")
        self.label_full_name = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_full_name.setGeometry(QtCore.QRect(30, 100, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        self.label_full_name.setFont(font)
        self.label_full_name.setStyleSheet("background-color: rgb(149, 223, 223);")
        self.label_full_name.setObjectName("label_full_name")
        self.label_email = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_email.setGeometry(QtCore.QRect(110, 150, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        self.label_email.setFont(font)
        self.label_email.setStyleSheet("background-color: rgb(149, 223, 223);")
        self.label_email.setObjectName("label_email")
        self.back2 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.back2.setGeometry(QtCore.QRect(100, 390, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.back2.setFont(font)
        self.back2.setStyleSheet("background-color: rgb(255, 170, 0);\n"
"color: rgb(255, 255, 255);")
        self.back2.setObjectName("back2")
        self.submit2 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.submit2.setGeometry(QtCore.QRect(260, 390, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.submit2.setFont(font)
        self.submit2.setStyleSheet("background-color: rgb(255, 170, 0);\n"
"color: rgb(255, 255, 255);")
        self.submit2.setObjectName("submit2")
        self.label_num_ph = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_num_ph.setGeometry(QtCore.QRect(30, 200, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        self.label_num_ph.setFont(font)
        self.label_num_ph.setStyleSheet("background-color: rgb(149, 223, 223);")
        self.label_num_ph.setObjectName("label_num_ph")
        self.radioButton_graduant = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.radioButton_graduant.setGeometry(QtCore.QRect(80, 350, 89, 20))
        self.radioButton_graduant.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(221, 221, 221, 135), stop:1 rgba(199, 199, 199, 106));")
        self.radioButton_graduant.setObjectName("radioButton_graduant")
        self.radioButton_3_admin = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.radioButton_3_admin.setGeometry(QtCore.QRect(300, 350, 101, 20))
        self.radioButton_3_admin.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(221, 221, 221, 135), stop:1 rgba(199, 199, 199, 106));")
        self.radioButton_3_admin.setObjectName("radioButton_3_admin")
        self.radioButton_2_teacher = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.radioButton_2_teacher.setGeometry(QtCore.QRect(200, 350, 71, 20))
        self.radioButton_2_teacher.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(221, 221, 221, 135), stop:1 rgba(199, 199, 199, 106));")
        self.radioButton_2_teacher.setObjectName("radioButton_2_teacher")
        self.label_pass = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_pass.setGeometry(QtCore.QRect(100, 250, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        self.label_pass.setFont(font)
        self.label_pass.setStyleSheet("background-color: rgb(149, 223, 223);")
        self.label_pass.setObjectName("label_pass")
        self.label_repeat_pass = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_repeat_pass.setGeometry(QtCore.QRect(20, 300, 145, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        self.label_repeat_pass.setFont(font)
        self.label_repeat_pass.setStyleSheet("background-color: rgb(149, 223, 223);")
        self.label_repeat_pass.setObjectName("label_repeat_pass")
        self.comboBox = QtWidgets.QComboBox(parent=self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(0, 0, 451, 501))
        self.comboBox.setObjectName("comboBox")
        self.lineEdit = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(180, 100, 231, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(180, 150, 231, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(180, 200, 231, 31))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(180, 250, 231, 31))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(180, 300, 231, 31))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.comboBox.raise_()
        self.signUp1.raise_()
        self.main_label.raise_()
        self.label_full_name.raise_()
        self.label_email.raise_()
        self.back2.raise_()
        self.submit2.raise_()
        self.label_num_ph.raise_()
        self.radioButton_graduant.raise_()
        self.radioButton_3_admin.raise_()
        self.radioButton_2_teacher.raise_()
        self.label_pass.raise_()
        self.label_repeat_pass.raise_()
        self.lineEdit.raise_()
        self.lineEdit_2.raise_()
        self.lineEdit_3.raise_()
        self.lineEdit_4.raise_()
        self.lineEdit_5.raise_()
        sign_up_1.setCentralWidget(self.centralwidget)

        self.retranslateUi(sign_up_1)
        QtCore.QMetaObject.connectSlotsByName(sign_up_1)

    def retranslateUi(self, sign_up_1):
        _translate = QtCore.QCoreApplication.translate
        sign_up_1.setWindowTitle(_translate("sign_up_1", "Реєстрація"))
        self.main_label.setText(_translate("sign_up_1", "Реєстрація"))
        self.label_full_name.setToolTip(_translate("sign_up_1", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.label_full_name.setText(_translate("sign_up_1", "Прізвище та ім\'я"))
        self.label_email.setToolTip(_translate("sign_up_1", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.label_email.setText(_translate("sign_up_1", "Email"))
        self.back2.setText(_translate("sign_up_1", "Назад"))
        self.submit2.setText(_translate("sign_up_1", "Далі"))
        self.label_num_ph.setToolTip(_translate("sign_up_1", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.label_num_ph.setText(_translate("sign_up_1", "Номер телефону"))
        self.radioButton_graduant.setText(_translate("sign_up_1", "Абітурієнт"))
        self.radioButton_3_admin.setText(_translate("sign_up_1", "Адміністратор"))
        self.radioButton_2_teacher.setText(_translate("sign_up_1", "Викладач"))
        self.label_pass.setToolTip(_translate("sign_up_1", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.label_pass.setText(_translate("sign_up_1", "Пароль"))
        self.label_repeat_pass.setToolTip(_translate("sign_up_1", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.label_repeat_pass.setText(_translate("sign_up_1", "Повторити пароль"))
