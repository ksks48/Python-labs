from PyQt6 import QtWidgets, uic
from PyQt6.QtWidgets import QMessageBox
import sys
from db_connection_new import *
from decimal import Decimal


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('start.ui', self)
        self.btn_sign_in.clicked.connect(self.show_log)
        self.btn_sign_up.clicked.connect(self.show_reg)

    def show_log(self):
        uic.loadUi('sign_in.ui', self)
        self.back1.clicked.connect(self.show_start)
        self.lineEdit.setPlaceholderText("0999999999")
        self.submit1.clicked.connect(self.check_login)


    def show_start(self):
        window.setFixedSize(450,500)
        uic.loadUi('start.ui', self)
        self.btn_sign_in.clicked.connect(self.show_log)
        self.btn_sign_up.clicked.connect(self.show_reg)


    def show_reg(self):
        uic.loadUi('sign_up_1.ui', self)
        self.back2.clicked.connect(self.show_start)

        self.lineEdit_2_email.setPlaceholderText('someemail@gmail.com')
        self.lineEdit_3_ph_num.setPlaceholderText("0999999999")
        self.submit2.clicked.connect(self.check_reg_1)
   
    def show_sign_up_2(self):
        uic.loadUi('sign_up_2.ui', self)
        self.back3.clicked.connect(self.show_reg)
        self.submit3.clicked.connect(self.check_reg_2)
        self.lineEdit_full_address.setPlaceholderText('область місто вулиця номер будинку')

    def show_sign_up_teacher(self):
        uic.loadUi('sign_up_teacher.ui', self)
        self.back4.clicked.connect(self.show_reg)
        self.submit4.clicked.connect(self.check_teach_reg)
    
    def check_teach_reg(self):
        self.teachers_faculty = self.comboBox.currentText()
        self.teachers_posada = self.comboBox_2.currentText()
        if self.teachers_faculty != "" and self.teachers_posada != "":
            window.setFixedSize(755,620)
            insert_data_teacher(self, self.name_and_surname, self.email, self.phone_number, self.teachers_faculty, self.teachers_posada, self.password)
        else:
            QMessageBox.about(self, "Виникла помилка!" ,"Будь ласка, оберіть запропановані варіанти")

    def check_login(self):
        self.phone_number = self.lineEdit.text()
        password = self.lineEdit_2.text()
        
        if self.phone_number.isdigit() and len(self.phone_number) == 10 and check_login(self.phone_number, password):
            if check_login(self.phone_number, password) == 1:
                window.setFixedSize(755,620)
                make_new_ac(self)
            elif check_login(self.phone_number, password) == 2:
                self.teach_phone = self.phone_number
                window.setFixedSize(755,620)
                make_new_teach_ac(self)
            else:
                self.admin_phone = self.phone_number
                window.setFixedSize(755,620)
                make_new_admin_ac(self)
        else:
            QMessageBox.about(self, "Виникла помилка!" ,"Перевірте чи правильно ви ввели дані")
    

    def check_reg_1(self):
        self.name_surname = self.lineEdit_fullname.text()
        self.email = self.lineEdit_2_email.text()
        self.phone_number = self.lineEdit_3_ph_num.text()
        self.password = self.lineEdit_4_pass.text()
        self.password_again = self.lineEdit_5_rep_pass.text()
        self.name_and_surname = self.name_surname.strip().split(" ")

        if len(self.name_and_surname) == 2:
            if '@' in self.email and '.' in self.email:
                if self.phone_number.isdigit() and len(self.phone_number) == 10:
                    if self.password == self.password_again and len(self.password)>0:
                        
                        if self.radioButton_graduant.isChecked():
                            self.show_sign_up_2()
                        elif self.radioButton_2_teacher.isChecked():
                            self.show_sign_up_teacher()
                        elif self.radioButton_3_admin.isChecked():
                            window.setFixedSize(755,620)
                            self.admin_phone = self.phone_number
                            insert_admin_data(self,self.name_and_surname, self.email, self.admin_phone,self.password)
                        
                    else:
                        QMessageBox.about(self, "Виникла помилка!" ,"Перевірте вказані вами паролі, вони мають співпадати")   
                        return False 
                else:
                    QMessageBox.about(self, "Виникла помилка!" ,"Вкажіть номер телефону правильно, як вказано в прикладі -> 0991234567")   
                    self.check_reg_1
                    return False
            else:
                QMessageBox.about(self, "Виникла помилка!" ,"Вкажіть пошту в форматі, як вказано в наведеному прикладі -> someemail@gmail.com")   
                self.check_reg_1
                return False
        else:
            QMessageBox.about(self, "Виникла помилка!" ,"Вкажіть прізвище та ім'я в таком форматі -> Прізвище Ім'я")  
            self.check_reg_1
            return False

    def check_reg_2(self):
        self.adress = self.lineEdit_full_address.text()
        self.ed_level = self.comboBox_ed_level.currentText()
        self.name_ed_institution = self.lineEdit_2_inst_name.text()
        self.num_atestat = self.lineEdit_3_num_atestat.text()
        self.num_dodatok = self.lineEdit_4_num_dodatok.text()
        selected_text = self.comboBox_faculty.currentText()
        if selected_text == "Англійської мови":
            self.faculty = 1
        elif selected_text == "Географії":
            self.faculty = 2
        elif selected_text == "Української мови":
            self.faculty = 3
        else:
            self.faculty = ""

        selected_benefits = self.comboBox_benefits.currentText()
        if selected_benefits == "Квота-1":
            self.benefits = 1
        elif selected_benefits == "Квота-2":
            self.benefits = 2
        elif selected_benefits == "Квота-3":
            self.benefits = 3
        elif selected_benefits == "Квота-іноземців":
            self.benefits = 4
        else:
            self.benefits = 5


        self.full_adress = self.adress.split(" ")
        if len(self.full_adress) == 5:
            if len(self.ed_level) > 0:
                if len(self.name_ed_institution) > 0:
                    if len(self.num_atestat) == 10:
                        if len(self.num_dodatok) == 8:
                            if self.faculty != "":
                                self.insert_data()
                            
                            else:
                                QMessageBox.about(self, "Виникла помилка!" ,"Будь ласка, оберіть факультет")   
                        else:
                            QMessageBox.about(self, "Виникла помилка!" ,"Будь ласка, вкажіть номер додатку правильно")   
                    else:
                        QMessageBox.about(self, "Виникла помилка!" ,"Будь ласка, вкажіть номер атестату правильно")   
                else:
                    QMessageBox.about(self, "Виникла помилка!" ,"Будь ласка, вкажіть назву навч. закладу")   
            else:
                QMessageBox.about(self, "Виникла помилка!" ,"Будь ласка, оберіть свій рівень освіти")   
        else:
            QMessageBox.about(self, "Виникла помилка!" ,"Вкажіть повну адресу в такому форматі -> область місто вулиця номер будинку")  

    def insert_data(self):
        window.setFixedSize(755,620)
        if insert_data(self, self.name_and_surname, self.email, self.phone_number, self.full_adress,self.ed_level,self.name_ed_institution,self.num_atestat,self.num_dodatok,self.faculty,self.benefits, self.password):
            pass

    
    """
        Оновлення даних
        !!!!!!!!!!!!!!!
    """
   
    def confirm_delete_account(self):
        confirmation = QMessageBox.question(self, "Підтвердження видалення", "Ви впевнені, що хочете видалити аккаунт?", QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        if confirmation == QMessageBox.StandardButton.Yes:
            delete_account(self)
            self.show_start()
        else:
            make_new_ac(self)

    def confirm_delete_account_teach(self):
        confirmation = QMessageBox.question(self, "Підтвердження видалення", "Ви впевнені, що хочете видалити аккаунт?", QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        if confirmation == QMessageBox.StandardButton.Yes:
            delete_teach_account(self)
            self.show_start()
        else:
            make_new_teach_ac(self)

    def confirm_delete_admin_account(self):
        confirmation = QMessageBox.question(self, "Підтвердження видалення", "Ви впевнені, що хочете видалити аккаунт?", QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        if confirmation == QMessageBox.StandardButton.Yes:
            delete_admin_account(self)
            self.show_start()
        else:
            make_new_admin_ac(self)



    def update_data(self): 
        window.setFixedSize(755,620)
        uic.loadUi('upd_data.ui', self)
        input_old_data(self)
        self.btn_upd.clicked.connect(self.confirm_upd)
        self.btn_back.clicked.connect(self.make_new_ac)

    """
        Graduant
    """ 
    def make_new_ac(self):
        make_new_ac(self)

    def show_table_common_rate(self):
        show_table_common_rate(self)

    def show_table_enroled(self):
        show_table_enroled(self)

    def show_table_ordered_rate(self):
        show_table_ordered_rate(self)

    def show_grad_scores(self):
        show_grad_scores(self)
        

    """
        Admin
    """ 

    def make_new_admin_ac(self):
        make_new_admin_ac(self)

    def show_admin_tbl(self):
        show_admin_tbl(self)    

    def show_benefits_tbl(self):
        show_benefits_tbl(self)

    def show_exams_tbl(self):
        show_exams_tbl(self)

    def show_exams_results(self):
        show_exams_results(self)    

    def show_faculty_tbl(self):
        show_faculty_tbl(self)

    def show_graduants_tbl(self):
        show_graduants_tbl(self)

    def show_scores_tbl(self):
        show_scores_tbl(self)

    def show_teacher_tbl(self):
        show_teacher_tbl(self)


    def upd_admin_admin(self):
        self.admin_name_surname = self.take_name_and_surname.text()
        self.admin_email = self.take_email.text()
        self.admin_phone = self.take_phone.text()
        self.admin_password = self.take_password.text()
        self.admin_password_again = self.take_password_again.text()
        
        self.admin_name_surname = self.admin_name_surname.strip().split(" ")
        
        if len(self.admin_name_surname) == 2:
            if '@' in self.admin_email and '.' in self.admin_email:
                if self.admin_phone.isdigit() and len(self.admin_phone) == 10:
                    if self.admin_password == self.admin_password_again and len(self.admin_password)>0:
                        update_new_admin(self,self.admin_name_surname, self.admin_email, self.admin_phone, self.admin_password, self.admin_id)
                        make_new_admin_ac(self)
                    else:
                        QMessageBox.about(self, "Виникла помилка!" ,"Перевірте вказані вами паролі, вони мають співпадати")   
                else:
                    QMessageBox.about(self, "Виникла помилка!" ,"Вкажіть номер телефону правильно, як вказано в прикладі -> 0991234567")   
            else:
                QMessageBox.about(self, "Виникла помилка!" ,"Вкажіть пошту в форматі, як вказано в наведеному прикладі -> someemail@gmail.com")   
        else:
            QMessageBox.about(self, "Виникла помилка!" ,"Вкажіть прізвище та ім'я в таком форматі -> Прізвище Ім'я")  

    def update_admin_data(self):
        window.setFixedSize(755,620)
        uic.loadUi('upd_admin.ui',self)
        input_old_admin(self)
        self.btn_upd_admin.clicked.connect(self.confirm_upd_admin)
        self.btn_back_admin.clicked.connect(self.make_new_admin_ac)

    def delete_some_ac(self):
        self.current_id_ = self.input_admin.text()
        
        delete_some_ac(self, self.current_id_)

    def confirm_upd(self):
        self.name_surname = self.lineEdit_fullname.text()
        self.email = self.lineEdit_2_email.text()
        self.phone_number = self.lineEdit_3_ph_num.text()
        self.password = self.lineEdit_4_pass.text()
        self.password_again = self.lineEdit_5_rep_pass.text()
        self.name_and_surname = self.name_surname.split(" ")

        if len(self.name_and_surname) == 2:
            if '@' in self.email and '.' in self.email:
                if self.phone_number.isdigit() and len(self.phone_number) == 10:
                    if self.password == self.password_again and len(self.password)>0:
                        pass
                        
                    else:
                        QMessageBox.about(self, "Виникла помилка!" ,"Перевірте вказані вами паролі, вони мають співпадати")   
                        return False 
                else:
                    QMessageBox.about(self, "Виникла помилка!" ,"Вкажіть номер телефону правильно, як вказано в прикладі -> 0991234567")   
                    self.check_reg_1
                    return False
            else:
                QMessageBox.about(self, "Виникла помилка!" ,"Вкажіть пошту в форматі, як вказано в наведеному прикладі -> someemail@gmail.com")   
                self.check_reg_1
                return False
        else:
            QMessageBox.about(self, "Виникла помилка!" ,"Вкажіть прізвище та ім'я в таком форматі -> Прізвище Ім'я")  
            self.check_reg_1
            return False
        
        self.adress = self.lineEdit_full_address.text()
        self.ed_level = self.comboBox_ed_level.currentText()
        self.name_ed_institution = self.lineEdit_2_inst_name.text()
        self.num_atestat = self.lineEdit_3_num_atestat.text()
        self.num_dodatok = self.lineEdit_4_num_dodatok.text()
        selected_text = self.comboBox_faculty.currentText()
        if selected_text == "Англійської мови":
            self.faculty = 1
        elif selected_text == "Географії":
            self.faculty = 2
        elif selected_text == "Української мови":
            self.faculty = 3
        else:
            self.faculty = ""

        selected_benefits = self.comboBox_benefits.currentText()
        if selected_benefits == "Квота-1":
            self.benefits = 1
        elif selected_text == "Квота-2":
            self.benefits = 2
        elif selected_text == "Квота-3":
            self.benefits = 3
        elif selected_text == "Квота-іноземців":
            self.benefits = 4
        else:
            self.benefits = 5


        self.full_adress = self.adress.split(" ")
        if len(self.full_adress) == 5:
            if len(self.ed_level) > 0:
                if len(self.name_ed_institution) > 0:
                    if len(self.num_atestat) == 10:
                        if len(self.num_dodatok) == 8:
                            if self.faculty != "":
                                update_new_data(self, self.name_and_surname, self.email, self.phone_number, self.full_adress,self.ed_level,self.name_ed_institution,self.num_atestat,self.num_dodatok,self.faculty,self.benefits, self.password, self.graduants_id)
                                make_new_ac(self)

                            else:
                                QMessageBox.about(self, "Виникла помилка!" ,"Будь ласка, оберіть факультет")   
                        else:
                            QMessageBox.about(self, "Виникла помилка!" ,"Будь ласка, вкажіть номер додатку правильно")   
                    else:
                        QMessageBox.about(self, "Виникла помилка!" ,"Будь ласка, вкажіть номер атестату правильно")   
                else:
                    QMessageBox.about(self, "Виникла помилка!" ,"Будь ласка, вкажіть назву навч. закладу")   
            else:
                QMessageBox.about(self, "Виникла помилка!" ,"Будь ласка, оберіть свій рівень освіти")   
        else:
            QMessageBox.about(self, "Виникла помилка!" ,"Вкажіть повну адресу в такому форматі -> область місто вулиця номер будинку")

    def confirm_upd_admin(self):
        self.admin_name_surname = self.lineEdit_fullname_admin.text()
        self.admin_email = self.lineEdit_2_email_admin.text()
        self.admin_phone = self.lineEdit_3_ph_num_admin.text()
        self.admin_password = self.lineEdit_4_pass_admin.text()
        self.admin_password_again = self.lineEdit_5_rep_pass_admin.text()
        
        self.admin_name_surname = self.admin_name_surname.strip().split(" ")
        
        if len(self.admin_name_surname) == 2:
            if '@' in self.admin_email and '.' in self.admin_email:
                if self.admin_phone.isdigit() and len(self.admin_phone) == 10:
                    if self.admin_password == self.admin_password_again and len(self.admin_password)>0:
                        
                        update_new_admin(self,self.admin_name_surname, self.admin_email, self.admin_phone, self.admin_password, self.admin_id)
                        make_new_admin_ac(self)
                    else:
                        QMessageBox.about(self, "Виникла помилка!" ,"Перевірте вказані вами паролі, вони мають співпадати")   
                        return False 
                else:
                    QMessageBox.about(self, "Виникла помилка!" ,"Вкажіть номер телефону правильно, як вказано в прикладі -> 0991234567")   
                    self.check_reg_1
                    return False
            else:
                QMessageBox.about(self, "Виникла помилка!" ,"Вкажіть пошту в форматі, як вказано в наведеному прикладі -> someemail@gmail.com")   
                self.check_reg_1
                return False
        else:
            QMessageBox.about(self, "Виникла помилка!" ,"Вкажіть прізвище та ім'я в таком форматі -> Прізвище Ім'я")  
            self.check_reg_1
            return False


    def upd_some_ac(self):
        choice = take_choice(self)
        self.current_id_ = self.input_admin.text()
        if len(self.current_id_)>0: 
            if choice != -1:   
                if choice == 1:
                    upd_some_ac_admin(self,self.current_id_)
                elif choice == 2:
                    upd_some_ac_benefits(self,self.current_id_)
                elif choice == 3:
                    upd_some_ac_exams(self,self.current_id_)
                elif choice == 4:
                    QMessageBox.about(self, "Виникла помилка!" ,"Вибачте, але оновлювати дані до цієї таблиці не можна")
                elif choice == 5:
                    upd_some_ac_faculty(self,self.current_id_)
                elif choice == 6:
                    upd_some_ac_graduants(self,self.current_id_)
                elif choice == 7:
                    upd_some_ac_scores(self,self.current_id_)
                elif choice == 8:
                    upd_some_ac_teacher(self,self.current_id_)
        else:
            QMessageBox.about(self, "Виникла помилка!" ,"Вибачте, але для цієї функції обов'язоково потрібно вказати айді")

    def confirm_update_admin(self):
        self.admin_name_surname = self.lineEdit_fullname_admin.text()
        self.admin_email = self.lineEdit_2_email_admin.text()
        self.admin_phone = self.lineEdit_3_ph_num_admin.text()
        self.admin_password = self.lineEdit_4_pass_admin.text()
        self.admin_password_again = self.lineEdit_5_rep_pass_admin.text()
        
        self.admin_name_surname = self.admin_name_surname.strip().split(" ")
        
        if len(self.admin_name_surname) == 2:
            if '@' in self.admin_email and '.' in self.admin_email:
                if self.admin_phone.isdigit() and len(self.admin_phone) == 10:
                    if self.admin_password == self.admin_password_again and len(self.admin_password)>0:
                        
                        update_new_admin(self,self.admin_name_surname, self.admin_email, self.admin_phone, self.admin_password, self.admin_id)
                        make_new_admin_ac(self)
                    else:
                        QMessageBox.about(self, "Виникла помилка!" ,"Перевірте вказані вами паролі, вони мають співпадати")   
                        return False 
                else:
                    QMessageBox.about(self, "Виникла помилка!" ,"Вкажіть номер телефону правильно, як вказано в прикладі -> 0991234567")   
                    self.check_reg_1
                    return False
            else:
                QMessageBox.about(self, "Виникла помилка!" ,"Вкажіть пошту в форматі, як вказано в наведеному прикладі -> someemail@gmail.com")   
                self.check_reg_1
                return False
        else:
            QMessageBox.about(self, "Виникла помилка!" ,"Вкажіть прізвище та ім'я в таком форматі -> Прізвище Ім'я")  
            self.check_reg_1
            return False

    def confirm_upd_benefits(self):
        self.benefit = self.take_benefit_name.text()
        self.num_of_places = self.take_num_of_places.text()
        
        if len(self.benefit)>0:
            if len(self.num_of_places)>0:
                confirm_upd_benefits(self,self.benefit,self.num_of_places,self.current_id_)
            else:
                QMessageBox.about(self, "Виникла помилка!" ,"Вкажіть кількість місць")  
        else:
            QMessageBox.about(self, "Виникла помилка!" ,"Вкажіть назву квоти")  

    def confirm_upd_exams(self):
        self.exams_name = self.take_exams_name.text()
        self.exams_date = self.take_exams_date.text()
        self.exams_min_pass = self.take_exams_min_pass.text()
        self.exams_time = self.take_exams_time.text()
        self.exams_faculty = self.take_faculty.currentText()

        if self.exams_faculty == 'Англійської мови':
            self.exams_faculty = 1
        elif self.exams_faculty == 'Географії':
            self.exams_faculty = 2
        elif self.exams_faculty == 'Української мови':
            self.exams_faculty = 3
        else:
            self.exams_faculty = 0

        if len(self.exams_name)!=0:
            if len(self.exams_date)!=0 and '-' in str(self.exams_date):
                if self.exams_min_pass.isdigit() and len(self.exams_min_pass)!=0:
                    if ':' in str(self.exams_time) and len(self.exams_time)!=0:
                        if self.exams_faculty!=0:
                            confirm_upd_exams(self,self.exams_name,self.exams_date,self.exams_min_pass,self.exams_time,self.exams_faculty,self.current_id_)
                        else:
                            QMessageBox.about(self, "Виникла помилка!" ,"Потрібно обрати факультет") 
                    else:
                        QMessageBox.about(self, "Виникла помилка!" ,"Вкажіть час, як вказано на наведеному прикладі -> 01:30:00") 
                else:
                    QMessageBox.about(self, "Виникла помилка!" ,"Вкажіть мінімальний прохідний числом") 
            else:
                QMessageBox.about(self, "Виникла помилка!" ,"Вкажіть дату правильно, як вказано в наведеному прикладі -> 2023-01-01") 
        else:
            QMessageBox.about(self, "Виникла помилка!" ,"Вкажіть назву екзамена")  

    def confirm_upd_faculty(self):
        self.faculty_name = self.take_faculty_name.text()
        self.faculty_adress = self.take_faculty_adress.text()
        self.faculty_phone = self.take_faculty_phone.text()
        self.comp_subject = self.take_comp_subject.text()
        self.num_of_places = self.take_num_of_places.text()
        self.num_of_budget_places = self.take_num_of_budget_places.text()
        
        self.faculty_adress = self.faculty_adress.split(" ")
        if len(self.faculty_name)!=0:
            if len(self.faculty_adress) == 4:
                if len(self.faculty_phone) == 10 and self.faculty_phone.isdigit():
                    if len(self.comp_subject)!=0:
                        if len(self.num_of_places)!=0 and self.num_of_places.isdigit():
                            if len(self.num_of_budget_places)!=0 and self.num_of_budget_places.isdigit():
                                confirm_upd_faculty(self,self.faculty_name,self.faculty_adress,self.faculty_phone,self.comp_subject,self.num_of_places,self.num_of_budget_places,self.current_id_)
                            else:
                                QMessageBox.about(self, "Виникла помилка!" ,"Вкажіть кількість бюджетних місць")
                        else:
                            QMessageBox.about(self, "Виникла помилка!" ,"Вкажіть кількість всіх місць")
                    else:
                        QMessageBox.about(self, "Виникла помилка!" ,"Вкажіть обов'язкові предмети")
                else:
                    QMessageBox.about(self, "Виникла помилка!" ,"Вкажіть номер телеофну правильно, як вказано на наведеному прикладі -> 0991234567")
            else:
                QMessageBox.about(self, "Виникла помилка!" ,"Вкажіть адресу правильно, як вказано на наведеному прикладі -> область місто вулиця номер_будинку")
        else:
            QMessageBox.about(self, "Виникла помилка!" ,"Вкажіть назву факультета")

    def confirm_upd_graduants(self):
        self.name_surname = self.lineEdit_fullname.text()
        self.email = self.lineEdit_2_email.text()
        self.phone_number = self.lineEdit_3_ph_num.text()
        self.password = self.lineEdit_4_pass.text()
        self.password_again = self.lineEdit_5_rep_pass.text()
        self.name_and_surname = self.name_surname.split(" ")

        if len(self.name_and_surname) == 2:
            if '@' in self.email and '.' in self.email:
                if self.phone_number.isdigit() and len(self.phone_number) == 10:
                    if self.password == self.password_again and len(self.password)>0:
                        pass
                        
                    else:
                        QMessageBox.about(self, "Виникла помилка!" ,"Перевірте вказані вами паролі, вони мають співпадати")   
                else:
                    QMessageBox.about(self, "Виникла помилка!" ,"Вкажіть номер телефону правильно, як вказано в прикладі -> 0991234567")   
            else:
                QMessageBox.about(self, "Виникла помилка!" ,"Вкажіть пошту в форматі, як вказано в наведеному прикладі -> someemail@gmail.com")   
        else:
            QMessageBox.about(self, "Виникла помилка!" ,"Вкажіть прізвище та ім'я в таком форматі -> Прізвище Ім'я")  
        
        self.adress = self.lineEdit_full_address.text()
        self.ed_level = self.comboBox_ed_level.currentText()
        self.name_ed_institution = self.lineEdit_2_inst_name.text()
        self.num_atestat = self.lineEdit_3_num_atestat.text()
        self.num_dodatok = self.lineEdit_4_num_dodatok.text()
        selected_text = self.comboBox_faculty.currentText()
        if selected_text == "Англійської мови":
            self.faculty = 1
        elif selected_text == "Географії":
            self.faculty = 2
        elif selected_text == "Української мови":
            self.faculty = 3
        else:
            self.faculty = ""

        selected_benefits = self.comboBox_benefits.currentText()
        if selected_benefits == "Квота-1":
            self.benefits = 1
        elif selected_text == "Квота-2":
            self.benefits = 2
        elif selected_text == "Квота-3":
            self.benefits = 3
        elif selected_text == "Квота-іноземців":
            self.benefits = 4
        else:
            self.benefits = 5

        self.full_adress = self.adress.split(" ")
        if len(self.full_adress) == 5:
            if len(self.ed_level) > 0:
                if len(self.name_ed_institution) > 0:
                    if len(self.num_atestat) == 10:
                        if len(self.num_dodatok) == 8:
                            if self.faculty != "":
                                confirm_upd_graduants(self, self.name_and_surname, self.email, self.phone_number, self.full_adress,self.ed_level,self.name_ed_institution,self.num_atestat,self.num_dodatok,self.faculty,self.benefits, self.password, self.current_id_)
                            else:
                                QMessageBox.about(self, "Виникла помилка!" ,"Будь ласка, оберіть факультет")   
                        else:
                            QMessageBox.about(self, "Виникла помилка!" ,"Будь ласка, вкажіть номер додатку правильно")   
                    else:
                        QMessageBox.about(self, "Виникла помилка!" ,"Будь ласка, вкажіть номер атестату правильно")   
                else:
                    QMessageBox.about(self, "Виникла помилка!" ,"Будь ласка, вкажіть назву навч. закладу")   
            else:
                QMessageBox.about(self, "Виникла помилка!" ,"Будь ласка, оберіть свій рівень освіти")   
        else:
            QMessageBox.about(self, "Виникла помилка!" ,"Вкажіть повну адресу в такому форматі -> область місто вулиця номер будинку")

    def confirm_upd_teacher(self):
        self.name_and_surname = self.lineEdit_date.text()
        self.email = self.lineEdit_date_2.text()
        self.phone_number = self.lineEdit_date_3.text()
        self.password = self.lineEdit_date_4.text()

        self.name_and_surname = self.name_and_surname.split()
        if len(self.name_and_surname) == 2:
            if '@' in self.email and '.' in self.email:
                if self.phone_number.isdigit() and len(self.phone_number) == 10:
                    if len(self.password)>0:
                        self.teachers_faculty = self.comboBox.currentText()
                        self.teachers_posada = self.comboBox_2.currentText()
                        if self.teachers_faculty != "" and self.teachers_posada != "":
                            confirm_upd_teacher(self,self.name_and_surname,self.email,self.phone_number,self.teachers_faculty,self.teachers_posada,self.password,self.current_id_)
                        else:
                            QMessageBox.about(self, "Виникла помилка!" ,"Будь ласка, оберіть запропановані варіанти")
                    else:
                        QMessageBox.about(self, "Виникла помилка!" ,"Будь ласка, вкажіть пароль")   
                else:
                    QMessageBox.about(self, "Виникла помилка!" ,"Вкажіть номер телефону правильно, як вказано в прикладі -> 0991234567")   
            else:
                QMessageBox.about(self, "Виникла помилка!" ,"Вкажіть пошту в форматі, як вказано в наведеному прикладі -> someemail@gmail.com")  
        else:
            QMessageBox.about(self, "Виникла помилка!" ,"Вкажіть прізвище та ім'я в таком форматі -> Прізвище Ім'я")  

    def confirm_upd_scores(self):
        try:
            self.scores_date = self.lineEdit_date.text()
            self.ukr_mova = float(self.lineEdit_ukr_mova.text())
            self.math = float(self.lineEdit_math.text())
            self.eng_mova = float(self.lineEdit_eng_mova.text())
            self.phis = float(self.lineEdit_phis.text())
            self.geo = float(self.lineEdit_geo.text())
            if self.ukr_mova >= 0 and self.ukr_mova <= 200 and self.math >= 0 and self.math <= 200  and self.eng_mova >= 0 and self.eng_mova <= 200  and self.phis >= 0 and self.phis <= 200  and self.geo >= 0 and self.geo <= 200:
                if '-' in self.scores_date and len(self.scores_date)!=0:
                    confirm_upd_scores(self,self.scores_date,self.ukr_mova,self.math,self.eng_mova,self.phis,self.geo,self.current_id_)
                else:
                    QMessageBox.about(self, "Виникла помилка!" ,"Будь ласка, вкажіть дату правльно, як вказано на прикладі -> 2022-01-01")
            else:
                QMessageBox.about(self, "Виникла помилка!" ,"Будь ласка, перевірте виставлені оцінки")
                return False
        except ValueError:
            pass

    def help_to_hide_labels(self):
        self.admin_lbl.hide()
        self.lbl.hide()
        self.label_2.setText('Додавання даних')

    def add_some_ac(self):
        choice = take_choice(self)
        if choice != -1:
            if choice == 1:
                uic.loadUi('add_admin_for_admin.ui',self)
                self.help_to_hide_labels()
                self.admin_add_admin.setText('Додати')
                self.admin_back.clicked.connect(self.make_new_admin_ac)
                self.admin_add_admin.clicked.connect(self.add_tbl_admin)
            elif choice == 2:
                uic.loadUi('add_benefits_for_admin.ui',self)
                self.help_to_hide_labels()
                self.admin_add_benefit.setText('Додати')
                self.admin_back.clicked.connect(self.make_new_admin_ac)
                self.admin_add_benefit.clicked.connect(self.add_tbl_benefits)
            elif choice == 3:
                uic.loadUi('add_exams_for_admin.ui',self)
                self.help_to_hide_labels()
                self.admin_back.clicked.connect(self.make_new_admin_ac)
                self.admin_add_exams.clicked.connect(self.add_tbl_exams)
            elif choice == 4:
                QMessageBox.about(self, "Виникла помилка!" ,"Вибачте, але додавати дані до цієї таблиці не можна")
                #uic.loadUi('add_exams_results_for_admin.ui',self)
                #self.admin_back.clicked.connect(self.make_new_admin_ac)
            elif choice == 5:
                uic.loadUi('add_faculty_for_admin.ui',self)
                self.help_to_hide_labels()
                self.admin_back.clicked.connect(self.make_new_admin_ac)
                self.admin_add_faculty.clicked.connect(self.add_tbl_faculty)
            elif choice == 6:
                uic.loadUi('add_graduants_for_admin.ui',self)
                self.help_to_hide_labels()
                self.admin_back.clicked.connect(self.make_new_admin_ac)
                self.admin_add_graduants.clicked.connect(self.add_tbl_graduants)
            elif choice == 7:
                QMessageBox.about(self, "Виникла помилка!" ,"Вибачте, але додавати дані до цієї таблиці не можна")
                
                #uic.loadUi('add_scores_for`_admin.ui',self)
                #self.admin_back.clicked.connect(self.make_new_admin_ac)
                #self.admin_add_scores.clicked.connect(self.add_tbl_scores)
            elif choice == 8:
                uic.loadUi('add_teacher_for_admin.ui',self)
                self.help_to_hide_labels()
                self.admin_back.clicked.connect(self.make_new_admin_ac)
                self.admin_add_teacher.clicked.connect(self.add_tbl_teacher)
    """
        Додавання /\  
                  \/ Адміна
    """

    def add_tbl_benefits(self):
        self.benefit_name = self.take_benefit_name.text()
        self.num_of_places = self.take_num_of_places.text()
        if len(self.benefit_name) !=0:
            if len(self.num_of_places) !=0:
                add_tbl_benefits(self,self.benefit_name,self.num_of_places)
            else:
                QMessageBox.about(self, "Виникла помилка!" ,"Будь ласка, Введіть дані коректно")
        else:
            QMessageBox.about(self, "Виникла помилка!" ,"Будь ласка, Введіть дані коректно")
 
    def add_tbl_admin(self):
        self.name_surname = self.take_name_and_surname.text()
        self.email = self.take_email.text()
        self.phone = self.take_phone.text()
        self.password = self.take_password.text()
        self.password_again = self.take_password_again.text()
        
        self.name_surname = self.name_surname.strip().split(" ")
        if len(self.name_surname) == 2:
            if '@' in self.email and '.' in self.email:
                if self.phone.isdigit() and len(self.phone) == 10:
                    if self.password == self.password_again and len(self.password)>0:
                        add_tbl_admin(self,self.name_surname,self.email,self.phone,self.password)
                    else:
                        QMessageBox.about(self, "Виникла помилка!" ,"Перевірте вказані вами паролі, вони мають співпадати")   
                else:
                    QMessageBox.about(self, "Виникла помилка!" ,"Вкажіть номер телефону правильно, як вказано в прикладі -> 0991234567")   
            else:
                QMessageBox.about(self, "Виникла помилка!" ,"Вкажіть пошту в форматі, як вказано в наведеному прикладі -> someemail@gmail.com")   
        else:
            QMessageBox.about(self, "Виникла помилка!" ,"Вкажіть прізвище та ім'я в таком форматі -> Прізвище Ім'я")  

    def add_tbl_exams(self):
        self.exams_name = self.take_exams_name.text()
        self.exams_date = self.take_exams_date.text()
        self.exams_min_pass = self.take_exams_min_pass.text()
        self.exams_time = self.take_exams_time.text()
        self.exams_faculty = self.take_faculty.currentText()

        if self.exams_faculty == 'Англійської мови':
            self.exams_faculty = 1
        elif self.exams_faculty == 'Географії':
            self.exams_faculty = 2
        elif self.exams_faculty == 'Української мови':
            self.exams_faculty = 3
        else:
            self.exams_faculty = 0

        if len(self.exams_name)!=0:
            if len(self.exams_date)!=0 and '-' in str(self.exams_date):
                if self.exams_min_pass.isdigit() and len(self.exams_min_pass)!=0:
                    if ':' in str(self.exams_time) and len(self.exams_time)!=0:
                        if self.exams_faculty!=0:
                            add_tbl_exams(self,self.exams_name,self.exams_date,self.exams_min_pass,self.exams_time,self.exams_faculty)
                        else:
                            QMessageBox.about(self, "Виникла помилка!" ,"Потрібно обрати факультет") 
                    else:
                        QMessageBox.about(self, "Виникла помилка!" ,"Вкажіть час, як вказано на наведеному прикладі -> 01:30:00") 
                else:
                    QMessageBox.about(self, "Виникла помилка!" ,"Вкажіть мінімальний прохідний числом") 
            else:
                QMessageBox.about(self, "Виникла помилка!" ,"Вкажіть дату правильно, як вказано в наведеному прикладі -> 2023-01-01") 
        else:
            QMessageBox.about(self, "Виникла помилка!" ,"Вкажіть назву екзамена")  

    def add_tbl_faculty(self):
        self.faculty_name = self.take_faculty_name.text()
        self.faculty_adress = self.take_faculty_adress.text()
        self.faculty_phone = self.take_faculty_phone.text()
        self.comp_subject = self.take_comp_subject.text()
        self.num_of_places = self.take_num_of_places.text()
        self.num_of_budget_places = self.take_num_of_budget_places.text()
        
        self.faculty_adress = self.faculty_adress.split(" ")
                #область місто вулиця номер будинку
        if len(self.faculty_name)!=0:
            if len(self.faculty_adress) == 4:
                if len(self.faculty_phone) == 10 and self.faculty_phone.isdigit():
                    if len(self.comp_subject)!=0:
                        if len(self.num_of_places)!=0 and self.num_of_places.isdigit():
                            if len(self.num_of_budget_places)!=0 and self.num_of_budget_places.isdigit():
                                add_tbl_faculty(self,self.faculty_name,self.faculty_adress,self.faculty_phone,self.comp_subject,self.num_of_places,self.num_of_budget_places)
                            else:
                                QMessageBox.about(self, "Виникла помилка!" ,"Вкажіть кількість бюджетних місць")
                        else:
                            QMessageBox.about(self, "Виникла помилка!" ,"Вкажіть кількість всіх місць")
                    else:
                        QMessageBox.about(self, "Виникла помилка!" ,"Вкажіть обов'язкові предмети")
                else:
                    QMessageBox.about(self, "Виникла помилка!" ,"Вкажіть номер телеофну правильно, як вказано на наведеному прикладі -> 0991234567")
            else:
                QMessageBox.about(self, "Виникла помилка!" ,"Вкажіть адресу правильно, як вказано на наведеному прикладі -> область місто вулиця номер_будинку")
        else:
            QMessageBox.about(self, "Виникла помилка!" ,"Вкажіть назву факультета")

    def add_tbl_graduants(self):
        self.name_surname = self.lineEdit_fullname.text()
        self.email = self.lineEdit_2_email.text()
        self.phone_number = self.lineEdit_3_ph_num.text()
        self.password = self.lineEdit_4_pass.text()
        self.password_again = self.lineEdit_5_rep_pass.text()
        self.name_and_surname = self.name_surname.split(" ")

        if len(self.name_and_surname) == 2:
            if '@' in self.email and '.' in self.email:
                if self.phone_number.isdigit() and len(self.phone_number) == 10:
                    if self.password == self.password_again and len(self.password)>0:
                        pass
                        
                    else:
                        QMessageBox.about(self, "Виникла помилка!" ,"Перевірте вказані вами паролі, вони мають співпадати")   
                else:
                    QMessageBox.about(self, "Виникла помилка!" ,"Вкажіть номер телефону правильно, як вказано в прикладі -> 0991234567")   
            else:
                QMessageBox.about(self, "Виникла помилка!" ,"Вкажіть пошту в форматі, як вказано в наведеному прикладі -> someemail@gmail.com")   
        else:
            QMessageBox.about(self, "Виникла помилка!" ,"Вкажіть прізвище та ім'я в таком форматі -> Прізвище Ім'я")  
        
        self.adress = self.lineEdit_full_address.text()
        self.ed_level = self.comboBox_ed_level.currentText()
        self.name_ed_institution = self.lineEdit_2_inst_name.text()
        self.num_atestat = self.lineEdit_3_num_atestat.text()
        self.num_dodatok = self.lineEdit_4_num_dodatok.text()
        selected_text = self.comboBox_faculty.currentText()
        if selected_text == "Англійської мови":
            self.faculty = 1
        elif selected_text == "Географії":
            self.faculty = 2
        elif selected_text == "Української мови":
            self.faculty = 3
        else:
            self.faculty = ""

        selected_benefits = self.comboBox_benefits.currentText()
        if selected_benefits == "Квота-1":
            self.benefits = 1
        elif selected_text == "Квота-2":
            self.benefits = 2
        elif selected_text == "Квота-3":
            self.benefits = 3
        elif selected_text == "Квота-іноземців":
            self.benefits = 4
        else:
            self.benefits = 5


        self.full_adress = self.adress.split(" ")
        if len(self.full_adress) == 5:
            if len(self.ed_level) > 0:
                if len(self.name_ed_institution) > 0:
                    if len(self.num_atestat) == 10:
                        if len(self.num_dodatok) == 8:
                            if self.faculty != "":
                                add_tbl_graduants(self,self.name_and_surname,self.email,self.phone_number,self.full_adress,self.ed_level,self.name_ed_institution,self.num_atestat,self.num_dodatok,self.faculty,self.benefits,self.password)
                            else:
                                QMessageBox.about(self, "Виникла помилка!" ,"Будь ласка, оберіть факультет")   
                        else:
                            QMessageBox.about(self, "Виникла помилка!" ,"Будь ласка, вкажіть номер додатку правильно")   
                    else:
                        QMessageBox.about(self, "Виникла помилка!" ,"Будь ласка, вкажіть номер атестату правильно")   
                else:
                    QMessageBox.about(self, "Виникла помилка!" ,"Будь ласка, вкажіть назву навч. закладу")   
            else:
                QMessageBox.about(self, "Виникла помилка!" ,"Будь ласка, оберіть свій рівень освіти")   
        else:
            QMessageBox.about(self, "Виникла помилка!" ,"Вкажіть повну адресу в такому форматі -> область місто вулиця номер будинку")

    def add_tbl_teacher(self):
        self.name_and_surname = self.lineEdit_date.text()
        self.email = self.lineEdit_date_2.text()
        self.phone_number = self.lineEdit_date_3.text()
        self.password = self.lineEdit_date_4.text()

        self.name_and_surname = self.name_and_surname.split()
        if len(self.name_and_surname) == 2:
            if '@' in self.email and '.' in self.email:
                if self.phone_number.isdigit() and len(self.phone_number) == 10:
                    if len(self.password)>0:
                        self.teachers_faculty = self.comboBox.currentText()
                        self.teachers_posada = self.comboBox_2.currentText()
                        if self.teachers_faculty != "" and self.teachers_posada != "":
                            add_tbl_teacher(self,self.name_and_surname,self.email,self.phone_number,self.teachers_faculty,self.teachers_posada,self.password)
                        else:
                            QMessageBox.about(self, "Виникла помилка!" ,"Будь ласка, оберіть запропановані варіанти")
                    else:
                        QMessageBox.about(self, "Виникла помилка!" ,"Будь ласка, вкажіть пароль")   
                else:
                    QMessageBox.about(self, "Виникла помилка!" ,"Вкажіть номер телефону правильно, як вказано в прикладі -> 0991234567")   
            else:
                QMessageBox.about(self, "Виникла помилка!" ,"Вкажіть пошту в форматі, як вказано в наведеному прикладі -> someemail@gmail.com")  
        else:
            QMessageBox.about(self, "Виникла помилка!" ,"Вкажіть прізвище та ім'я в таком форматі -> Прізвище Ім'я")  

    # def add_tbl_scores(self):
    #     try:
    #         self.scores_date = self.lineEdit_date.text()
    #         self.ukr_mova = int(self.lineEdit_ukr_mova.text())
    #         self.math = int(self.lineEdit_math.text())
    #         self.eng_mova = int(self.lineEdit_eng_mova.text())
    #         self.phis = int(self.lineEdit_phis.text())
    #         self.geo = int(self.lineEdit_geo.text())

    #         if self.ukr_mova >= 0 and self.ukr_mova <= 200 and self.math >= 0 and self.math <= 200  and self.eng_mova >= 0 and self.eng_mova <= 200  and self.phis >= 0 and self.phis <= 200  and self.geo >= 0 and self.geo <= 200:
    #             if '-' in self.scores_date and len(self.scores_date)!=0:
    #                 window.setFixedSize(755,620)
    #                 add_tbl_scores(self,self.scores_date,self.ukr_mova,self.math,self.eng_mova,self.phis,self.geo)
    #             else:
    #                 QMessageBox.about(self, "Виникла помилка!" ,"Будь ласка, вкажіть дату правльно, як вказано на прикладі -> 2022-01-01")
    #         else:
    #             QMessageBox.about(self, "Виникла помилка!" ,"Будь ласка, перевірте виставлені оцінки")
    #             return False
    #     except ValueError:
    #         pass


    def make_new_teach_ac(self):
        make_new_teach_ac(self)

    def update_new_teach(self):
        window.setFixedSize(755,620)
        uic.loadUi('upd_teach.ui',self)
        input_old_teach(self)
        self.btn_upd.clicked.connect(self.confirm_upd_teach)
        self.btn_back.clicked.connect(self.make_new_teach_ac)

    def confirm_upd_teach(self):
        self.name_surname = self.lineEdit_fullname.text()
        self.email = self.lineEdit_2_email.text()
        self.phone_number = self.lineEdit_3_ph_num.text()
        self.password = self.lineEdit_4_pass.text()
        self.password_again = self.lineEdit_5_rep_pass.text()
        self.name_and_surname = self.name_surname.strip().split(" ")

        if len(self.name_and_surname) == 2:
            if '@' in self.email and '.' in self.email:
                if self.phone_number.isdigit() and len(self.phone_number) == 10:
                    if self.password == self.password_again and len(self.password)>0:
                        self.teachers_faculty = self.comboBox.currentText()
                        self.teachers_posada = self.comboBox_2.currentText()
                        if self.teachers_faculty != "" and self.teachers_posada != "":
                            window.setFixedSize(755,620)
                            update_new_teach(self,self.name_and_surname, self.email,  self.phone_number,self.teachers_faculty, self.teachers_posada, self.password, self.teach_id)
                            make_new_teach_ac(self)
                        else:
                            QMessageBox.about(self, "Виникла помилка!" ,"Будь ласка, оберіть запропановані варіанти")
                            return False
                        
                    else:
                        QMessageBox.about(self, "Виникла помилка!" ,"Перевірте вказані вами паролі, вони мають співпадати")   
                        return False 
                else:
                    QMessageBox.about(self, "Виникла помилка!" ,"Вкажіть номер телефону правильно, як вказано в прикладі -> 0991234567")   
                    self.check_reg_1
                    return False
            else:
                QMessageBox.about(self, "Виникла помилка!" ,"Вкажіть пошту в форматі, як вказано в наведеному прикладі -> someemail@gmail.com")   
                self.check_reg_1
                return False
        else:
            QMessageBox.about(self, "Виникла помилка!" ,"Вкажіть прізвище та ім'я в таком форматі -> Прізвище Ім'я")  
            self.check_reg_1
            return False
        
    def show_teach_scores(self):
        show_teach_scores(self)

    def show_teach_no_scores(self):
        show_teach_no_scores(self)

    def edit_table(self):
        self.current_id_teach = self.input_teach.text()
        if self.current_id_teach == '':
            QMessageBox.information(self, "Редагування таблиці", "Впишіть айді для редагування")
        else:
            window.setFixedSize(755,620)
            uic.loadUi('edit_scores.ui',self)
            input_old_scores_teach(self)
            self.btn_upd.clicked.connect(self.confirm_upd_teach_scores)
            self.btn_back.clicked.connect(self.make_new_teach_ac)

    def confirm_upd_teach_scores(self):
        self.ukr_mova = int(self.lineEdit_ukr_mova.text())
        self.math = int(self.lineEdit_math.text())
        self.eng_mova = int(self.lineEdit_eng_mova.text())
        self.phis = int(self.lineEdit_phis.text())
        self.geo = int(self.lineEdit_geo.text())

        if self.ukr_mova >= 0 and self.ukr_mova <= 200 and self.math >= 0 and self.math <= 200  and self.eng_mova >= 0 and self.eng_mova <= 200  and self.phis >= 0 and self.phis <= 200  and self.geo >= 0 and self.geo <= 200:
            window.setFixedSize(755,620)

            edit_table(self,self.ukr_mova, self.math, self.eng_mova,self.phis, self.geo, self.current_id_teach)
            make_new_teach_ac(self)
        else:
            QMessageBox.about(self, "Виникла помилка!" ,"Будь ласка, перевірте виставлені оцінки")
            return False


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.setFixedSize(450,500)
    window.show()
    sys.exit(app.exec())

