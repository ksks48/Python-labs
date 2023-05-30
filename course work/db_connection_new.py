from PyQt6 import QtWidgets, uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableView, QMessageBox
from PyQt6.QtCore import QAbstractTableModel, Qt
import mysql.connector
from PyQt6.QtGui import QAction


class TableModel(QAbstractTableModel):
    def __init__(self, data, header):
        super().__init__()
        self._data = data
        self._header = header

    def rowCount(self, parent):
        return len(self._data)

    def columnCount(self, parent):
        if self._data:
            return len(self._data[0])
        else:
            return 0

    def data(self, index, role):
        if role == Qt.ItemDataRole.DisplayRole:
            row = index.row()
            column = index.column()
            value = self._data[row][column]
            return str(value)

    def headerData(self, section, orientation, role):
        if role == Qt.ItemDataRole.DisplayRole:
            if orientation == Qt.Orientation.Horizontal:
                return self._header[section]

mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="",
    database="entrance exams"
)


def check_login(contact_number, password):
    cursor = mydb.cursor()
    sql = "SELECT * FROM Graduants WHERE contact_number = %s AND password = %s"
    val = (contact_number, password)
    cursor.execute(sql, val)
    result = cursor.fetchone()

    if result:
        return 1

    sql = "SELECT * FROM Teacher WHERE contact_number = %s AND password = %s"
    val = (contact_number, password)
    cursor.execute(sql, val)
    result = cursor.fetchone()

    if result:
        return 2

    sql = "SELECT * FROM Admin WHERE contact_number = %s AND password = %s"
    val = (contact_number, password)
    cursor.execute(sql, val)
    result = cursor.fetchone()

    if result:
        return 3

    return False


"""
    Функції для Абітурієнтів
    !!!!!!!!!!!!!!!!!!!!!!!!
"""




def insert_data(self, name_and_surname, email, phone_number, full_address, ed_level, name_ed_institution, num_atestat, num_dodatok, faculty, benefits, password):
    cursor = mydb.cursor()
    insert_query = "INSERT INTO Graduants (first_name, last_name, email, contact_number, region, locality, street, `apartment number`, flat, ed_level, name_ed_institution, num_atestat, num_dodatok, faculty_id, benefits, password) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    values = (name_and_surname[0], name_and_surname[1], email, phone_number, full_address[0], full_address[1], full_address[2], full_address[3], full_address[4], ed_level, name_ed_institution, num_atestat, num_dodatok, faculty, benefits, password)

    try:
        cursor.execute(insert_query, values)
        mydb.commit()

        cursor.execute("SELECT graduants_id, faculty_id FROM Graduants WHERE contact_number = %s", [self.phone_number])
        result = cursor.fetchone()
        if result:
            graduants_id = result[0]
            faculty_id = result[1]

        cursor.execute("INSERT INTO Scores (graduants_id, date, score_mathematics, score_ukrainian, score_english, score_physics, score_geography) VALUES (%s, '2000-01-01', 0, 0, 0, 0, 0)", (graduants_id,))
        mydb.commit()

        cursor.execute("INSERT INTO Exams_results (`faculty_id`,`graduants_id`,`average_score`,`status`) VALUES (%s,%s,get_average(%s),get_status(%s))", (faculty_id, graduants_id, graduants_id, graduants_id))
        mydb.commit()

        make_new_ac(self)

    except mysql.connector.Error as error:
        print("Помилка під час вставки даних:", error)

    cursor.close()

def make_new_ac(self):
    uic.loadUi('ac_grad.ui', self)
    cursor = mydb.cursor()
    cursor.execute("SELECT graduants_id, first_name, last_name, email, contact_number, region, locality, street, `apartment number`, flat, ed_level, name_ed_institution, num_atestat, num_dodatok, faculty_id, benefits FROM Graduants WHERE contact_number = %s", [self.phone_number])
    result = cursor.fetchone()
        
    if result:
        self.graduants_id = result[0]
        self.faculty_id = result[14]
        
        cursor.execute("UPDATE Exams_results SET `faculty_id` = %s, `average_score` = get_average(%s), `status` = get_status(%s) WHERE `graduants_id` = %s", (self.faculty_id, self.graduants_id, self.graduants_id, self.graduants_id))
        mydb.commit()

        self.label_id_2.setText("№ " + str(result[0]))
        self.label_full_name_2.setText(result[1] + " " + result[2])
        self.label_email_2.setText(result[3])
        self.label_num_ph_2.setText(result[4])
        self.label_addres_2.setText(result[5] + " " + result[6] + " " + result[7] + " " + result[8] + " " + result[9])
        self.label_ed_level_2.setText(result[10])
        self.label_name_ed_institution_2.setText(result[11])
        self.label_num_atestat_2.setText(result[12])
        self.label_num_dodatok_2.setText(result[13])
        self.label_faculty_2.setText(str(result[14]))
        self.label_benefits_2.setText(str(result[15]))

        self.btn_delete_ac.clicked.connect(self.confirm_delete_account)
        self.btn_upd_data.clicked.connect(self.update_data)
        self.btn_common_r.clicked.connect(self.show_table_common_rate)
        self.btn_enroled1.clicked.connect(self.show_table_enroled)
        self.btn_order.clicked.connect(self.show_table_ordered_rate)
        self.btn_grad_scores.clicked.connect(self.show_grad_scores)

        self.btn_home_1.clicked.connect(self.show_start)

    cursor.close()
    

def show_table_common_rate(self):
    
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM Exams_results")
    result = cursor.fetchall()
    
    header = [desc[0] for desc in cursor.description]
    
    model = TableModel(result, header)
    self.tableView.setModel(model)
    for column in range(len(header)):
        self.tableView.setColumnWidth(column,120)
    cursor.close()

def show_table_ordered_rate(self):
    
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM Exams_results order by average_score DESC")
    result = cursor.fetchall()
    
    header = [desc[0] for desc in cursor.description]

    model = TableModel(result, header)
    self.tableView.setModel(model)
    for column in range(len(header)):
        self.tableView.setColumnWidth(column,120)
    cursor.close()

def show_table_enroled(self):
    
    cursor = mydb.cursor()
    cursor.execute("SELECT `graduants`.`graduants_id`, `first_name`, `last_name`, (`score_mathematics`+`score_ukrainian`+`score_english`+`score_physics`+`score_geography`)/3 AS average,`benefits`, `ed_level` FROM `scores` LEFT JOIN `graduants`  ON `scores`.`graduants_id` = `graduants`.`graduants_id` WHERE `ed_level` <> 'початкова освіта' AND  (`score_mathematics` > 150) AND (`score_ukrainian` > 150) AND (`score_english` > 130 or `score_english` = 0) AND (`score_physics` > 130 OR `score_physics` = 0) AND (`score_geography` > 120 OR `score_geography` = 0)  AND `graduants`.`faculty_id` = %s ORDER BY CASE WHEN `graduants`.`benefits` <> 5 THEN 0 ELSE 1 END, `average` DESC LIMIT 8;", (self.faculty_id,))
    result = cursor.fetchall()
    
    header = [desc[0] for desc in cursor.description]
    model = TableModel(result, header)
    self.tableView.setModel(model)
    for column in range(len(header)):
        self.tableView.setColumnWidth(column,120)
    cursor.close()

def show_grad_scores(self):
    
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM Scores  WHERE graduants_id = %s",(self.graduants_id,))
    result = cursor.fetchall()
    
    header = [desc[0] for desc in cursor.description]
    
    model = TableModel(result, header)
    self.tableView.setModel(model)
    for column in range(len(header)):
        self.tableView.setColumnWidth(column,120)
    cursor.close()


def delete_account(self):
    cursor = mydb.cursor()
    cursor.execute(f"SET FOREIGN_KEY_CHECKS=0")
    cursor.execute("DELETE FROM Graduants WHERE graduants_id = %s", (self.graduants_id,))
    cursor.execute(f"SET FOREIGN_KEY_CHECKS=1")
    mydb.commit()
    cursor.close()
    QMessageBox.information(self, "Видалення аккаунту", "Аккаунт успішно видалено.")


def update_new_data(self, name_and_surname, email, phone_number, full_address, ed_level, name_ed_institution, num_atestat, num_dodatok, faculty, benefits, password, graduants_id):
    cursor = mydb.cursor()
    update_query = "UPDATE Graduants SET first_name = %s, last_name = %s, email = %s, contact_number = %s, region = %s, locality = %s, street = %s, `apartment number` = %s, flat = %s, ed_level = %s, name_ed_institution = %s, num_atestat = %s, num_dodatok = %s, faculty_id = %s, benefits = %s, password = %s WHERE graduants_id = %s"
    values = (name_and_surname[0], name_and_surname[1], email, phone_number, full_address[0], full_address[1], full_address[2], full_address[3], full_address[4], ed_level, name_ed_institution, num_atestat, num_dodatok, faculty, benefits, password, graduants_id)

    try:
        cursor.execute(update_query, values)
        mydb.commit()
        make_new_ac(self)

    except mysql.connector.Error as error:
        print("Помилка під час оновлення даних:", error)
    cursor.close()

def input_old_data(self):
    cursor = mydb.cursor()

    select_query = "SELECT * FROM Graduants WHERE graduants_id = %s"
    select_values = (self.graduants_id,)
    cursor.execute(select_query, select_values)
    old_data = cursor.fetchone()

    self.lineEdit_fullname.setText(old_data[1] + " " + old_data[2])
    self.lineEdit_2_email.setText(old_data[3])
    self.lineEdit_3_ph_num.setText(old_data[4])
    self.lineEdit_full_address.setText(old_data[5] + " " + old_data[6] + " " + old_data[7] + " " + old_data[8] + " " + old_data[9])
    self.comboBox_ed_level.setCurrentIndex(self.comboBox_faculty.currentIndex())
    self.lineEdit_2_inst_name.setText(old_data[11])
    self.lineEdit_3_num_atestat.setText(old_data[12])
    self.lineEdit_4_num_dodatok.setText(old_data[13])
    self.comboBox_faculty.setCurrentIndex(self.comboBox_faculty.currentIndex())
    self.comboBox_benefits.setCurrentIndex(self.comboBox_benefits.currentIndex())
    cursor.close()


"""
    Все для Адміністратора
    !!!!!!!!!!!!!!!!!!!!!!
"""


def make_new_admin_ac(self):
    uic.loadUi('ac_admin.ui', self)
    cursor = mydb.cursor()
    cursor.execute("SELECT admin_id ,first_name, last_name, email, contact_number FROM Admin WHERE contact_number = %s", [self.admin_phone])
    result = cursor.fetchone()
    
    self.label_help_admin.hide()
    self.input_admin.hide()
    

    if result:
        self.admin_id = result[0]
        self.label_admin_id.setText("№ " + str(result[0]))
        self.label_full_name_2.setText(result[1] + " " + result[2])
        self.label_email_2.setText(result[3])
        self.label_num_ph_2.setText(result[4])

        self.btn_delete_acc.clicked.connect(self.confirm_delete_admin_account)
        self.btn_upd_name_and_surname.clicked.connect(self.update_admin_data)
        
        self.btn_show_admin_tbl.clicked.connect(self.show_admin_tbl)
        self.btn_show_benefits_tbl.clicked.connect(self.show_benefits_tbl)
        
        self.btn_show_exams_tbl.clicked.connect(self.show_exams_tbl)
        self.btn_show_exams_results_tbl.clicked.connect(self.show_exams_results)
        self.btn_show_faculty_tbl.clicked.connect(self.show_faculty_tbl)
        self.btn_show_graduants_tbl.clicked.connect(self.show_graduants_tbl)
        self.btn_show_scores_tbl.clicked.connect(self.show_scores_tbl)
        self.btn_show_teacher_tbl.clicked.connect(self.show_teacher_tbl)
        self.btn_delete_ac_2.clicked.connect(self.delete_some_ac)

        self.btn_home_2.clicked.connect(self.show_start)
        self.btn_add_some_ac.clicked.connect(self.add_some_ac)
        self.btn_upd_some_ac.clicked.connect(self.upd_some_ac)

        try:
            if self.choice==1:
                show_admin_tbl(self)
            elif self.choice==2:
                show_benefits_tbl(self)
            elif self.choice==3:
                show_exams_tbl(self)
            elif self.choice==4:
                show_exams_results(self)
            elif self.choice==5:
                show_faculty_tbl(self)
            elif self.choice==6:
                show_graduants_tbl(self)
            elif self.choice==7:
                show_scores_tbl(self)
            else:
                show_teacher_tbl(self)
        except AttributeError:
            pass

    cursor.close()

def delete_admin_account(self):
    cursor = mydb.cursor()
    cursor.execute("DELETE FROM Admin Where admin_id = %s", (self.admin_id,))

    mydb.commit()
    cursor.close()
    QMessageBox.information(self, "Видалення аккаунту", "Аккаунт успішно видалено.")


def insert_admin_data(self, name_and_surname, email, phone_number,password):
    cursor = mydb.cursor()
    insert = "INSERT INTO Admin (first_name, last_name, email, contact_number, password) VALUES  (%s, %s, %s, %s, %s)"
    values = (name_and_surname[0], name_and_surname[1], email, phone_number, password)

    try:
        cursor.execute(insert, values)
        mydb.commit()
        make_new_admin_ac(self)

    except mysql.connector.Error as error:
        print("Помилка під час вставки даних:", error)

    
def update_new_admin(self,name_and_surname, email, phone_number, password,admin_id):
    cursor = mydb.cursor()
    update = "UPDATE Admin SET first_name = %s, last_name = %s, email = %s, contact_number = %s, password = %s WHERE admin_id = %s"
    values = (name_and_surname[0], name_and_surname[1], email, phone_number, password, admin_id)

    try:
        cursor.execute(update, values)
        mydb.commit()
        make_new_admin_ac(self)

    except mysql.connector.Error as error:
        print("Помилка під час оновлення даних:", error)

    cursor.close()

def input_old_admin(self):
    cursor = mydb.cursor()

    select_query = "SELECT * FROM Admin WHERE admin_id = %s"
    select_values = (self.admin_id,)
    cursor.execute(select_query, select_values)
    old_data = cursor.fetchone()

    self.lineEdit_fullname_admin.setText(old_data[1] + " " + old_data[2])
    self.lineEdit_2_email_admin.setText(old_data[3])
    self.lineEdit_3_ph_num_admin.setText(old_data[4])
    cursor.close()



def help_to_show(self,name):
    cursor = mydb.cursor()
    cursor.execute(f"SELECT * FROM {name}")
    result = cursor.fetchall()

    header = [head[0] for head in cursor.description]
    
    model = TableModel(result, header)
    self.tableView.setModel(model)
    for column in range(len(header)):
        self.tableView.setColumnWidth(column,120)

    cursor.close()

def show_(self,name):
    self.label_help_admin.show()
    self.input_admin.show()
    self.label_help_admin.setText(f'Введіть {name}:')

def show_admin_tbl(self):
    show_(self,'admin_id')
    help_to_show(self,'Admin')
    self.choice = 1

def show_benefits_tbl(self):
    show_(self,'benefit_id')
    help_to_show(self,'Benefits')
    self.choice = 2

def show_exams_tbl(self):
    show_(self,'teacher_id')
    help_to_show(self,'Exams')
    self.choice = 3

def show_exams_results(self):
    show_(self,'graduants_id')
    help_to_show(self,'Exams_results') 
    self.choice = 4

def show_faculty_tbl(self):
    show_(self,'faculty_id')
    help_to_show(self,'Faculty')
    self.choice = 5

def show_graduants_tbl(self):
    show_(self,'graduants_id')
    help_to_show(self,'Graduants')
    self.choice = 6

def show_scores_tbl(self):
    show_(self,'graduants_id')
    help_to_show(self,'Scores')
    self.choice = 7

def show_teacher_tbl(self):
    show_(self,'teacher_id')
    help_to_show(self,'Teacher')
    self.choice = 8

def take_choice(self):
    try:
        return self.choice
    except AttributeError:
        QMessageBox.information(self, "Помилка", "Оберіть таблицю!")
        return -1

def help_to_delete(tbl_name, id_name, current_id):
        try:
            cursor = mydb.cursor()
            cursor.execute(f"SET FOREIGN_KEY_CHECKS=0")
            cursor.execute(f"DELETE FROM {tbl_name} Where {id_name} = {current_id}")
            cursor.execute(f"SET FOREIGN_KEY_CHECKS=1")
            cursor.execute(f"")
            mydb.commit()
            cursor.close()
            help_to_autoincrement(tbl_name)
        except mysql.connector.errors.ProgrammingError:
            pass # Виникала при подвійному спамі на кнопку видалити


"""
    НЕ ПРАЦЮЄ бл***  |
                    \|/
"""
def help_to_autoincrement(tbl_name):
    cursor = mydb.cursor()
    cursor.execute(f"DELETE FROM SQLITE_SEQUENCE WHERE name='{tbl_name}'")
    cursor.execute(f"UPDATE SQLITE_SEQUENCE SET seq = 0 WHERE name = '{tbl_name}'")
    mydb.commit()
    cursor.close()

def delete_some_ac(self, current_id):
    if current_id == '':
        QMessageBox.information(self, "Видалення аккаунту", "Впишіть айді для видалення")
    else:
        try:
            if self.choice == 1:
                help_to_delete('Admin','admin_id',current_id)
                show_admin_tbl(self)
            elif self.choice == 2:
                help_to_delete('Benefits','benefit_id',current_id)
                show_benefits_tbl(self)
            elif self.choice == 3:
                help_to_delete('Exams','teacher_id',current_id)
                help_to_delete('Teacher','teacher_id',current_id)
                show_exams_tbl(self)
            elif self.choice == 4:
                help_to_delete('Exams_results','graduants_id',current_id)
                help_to_delete('Graduants','graduants_id',current_id)
                help_to_delete('Scores','graduants_id',current_id)
                show_exams_tbl(self)
            elif self.choice == 5:
                help_to_delete('Faculty','faculty_id',current_id)
                show_faculty_tbl(self)
            elif self.choice == 6:
                help_to_delete('Graduants','graduants_id',current_id)
                help_to_delete('Scores','graduants_id',current_id)
                help_to_delete('Exams_results','graduants_id',current_id)
                show_graduants_tbl(self)   
            elif self.choice == 7:
                help_to_delete('Graduants','graduants_id',current_id)
                help_to_delete('Scores','graduants_id',current_id)
                help_to_delete('Exams_results','graduants_id',current_id)
                show_scores_tbl(self)
            elif self.choice == 8:
                help_to_delete('Exams','teacher_id',current_id)
                help_to_delete('Teacher','teacher_id',current_id)
                show_teacher_tbl(self)
        except mysql.connector.errors.IntegrityError:
            QMessageBox.information(self, "Видалення аккаунту", "Цей аккаунт не можливо видалити!")


def add_tbl_benefits(self,benefit_name,num_of_places):
    cursor = mydb.cursor()
    insert_query = "INSERT INTO Benefits (`benefit_name`,`num_of_places`) VALUES (%s, %s)"
    values = (benefit_name, num_of_places)
    try:
        cursor.execute(insert_query, values)
        mydb.commit()
        make_new_admin_ac(self)

    except mysql.connector.Error as error:
        print("Помилка під час вставки даних:", error)
    
    cursor.close()

def add_tbl_admin(self,name_surname,email,phone,password):
    cursor = mydb.cursor()
    insert_query = "INSERT INTO Admin (`first_name`,`last_name`,`email`,`contact_number`,`password`) VALUES (%s,%s,%s,%s,%s)"
    values = (name_surname[0],name_surname[1],email,phone,password)
    try:
        cursor.execute(insert_query,values)
        mydb.commit()
        make_new_admin_ac(self)
    except mysql.connector.Error as error:
        print("Помилка під час вставки даних:", error)

def add_tbl_exams(self, name, date, min_pass, time, faculty_id):
    cursor = mydb.cursor()
    cursor.execute(f"SET FOREIGN_KEY_CHECKS=0")
    cursor.execute('SELECT MAX(teacher_id) FROM Teacher')
    teacher_id = cursor.fetchone()[0]
    insert_query = "INSERT INTO Exams (`teacher_id`,`name`,`date`,`min_passing_score`,`time`,`faculty_id`) VALUES (%s,%s,%s,%s,%s,%s)"
    values = (teacher_id+1,name,date,min_pass,time,faculty_id)
    try:
        cursor.execute(insert_query,values)
        mydb.commit()
        make_new_admin_ac(self)
        cursor.execute(f"SET FOREIGN_KEY_CHECKS=1")
    except mysql.connector.Error as error:
        print("Помилка під час вставки даних:", error)

    insert_2 = "INSERT INTO Teacher (`first_name`,`last_name`,`email`,`contact_number`,`department`,`position`) VALUES (%s,%s,%s,%s,%s,%s)"
    values_2 = ('new_acc','','','','','')
    try:
        cursor.execute(insert_2,values_2)
        mydb.commit()
        make_new_admin_ac(self)
    except mysql.connector.Error as error:
        print("Помилка під час вставки даних:", error)


def add_tbl_faculty(self,name,adress,phone,comp_subject,num_of_places,num_of_budget_places):
    cursor = mydb.cursor()
    #cursor.execute(f"SET FOREIGN_KEY_CHECKS=0")
    insert_query = "INSERT INTO Faculty (`name`,`region`,`city`,`street`,`house_number`,`contact_number`,`compulsory_subject`,`all_number_of_places`,`number_of_budget_places`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    values = (name,adress[0],adress[1],adress[2],adress[3],phone,comp_subject,num_of_places,num_of_budget_places)
    try:
        cursor.execute(insert_query,values)
        mydb.commit()
        make_new_admin_ac(self)
       # cursor.execute(f"SET FOREIGN_KEY_CHECKS=1")
    except mysql.connector.Error as error:
        print("Помилка під час вставки даних:", error)

def add_tbl_graduants(self,name_and_surname,email,phone_number,full_address,ed_level,name_ed_institution,num_atestat,num_dodatok,faculty,benefits,password):
    cursor = mydb.cursor()
    insert_query = "INSERT INTO Graduants (first_name, last_name, email, contact_number, region, locality, street, `apartment number`, flat, ed_level, name_ed_institution, num_atestat, num_dodatok, faculty_id, benefits, password) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    values = (name_and_surname[0], name_and_surname[1], email, phone_number, full_address[0], full_address[1], full_address[2], full_address[3], full_address[4], ed_level, name_ed_institution, num_atestat, num_dodatok, faculty, benefits, password)
    try:
        cursor.execute(insert_query,values)
        mydb.commit()
        make_new_admin_ac(self)
       # cursor.execute(f"SET FOREIGN_KEY_CHECKS=1")
    except mysql.connector.Error as error:
        print("Помилка під час вставки даних:", error)

    cursor.execute('SELECT MAX(graduants_id) FROM Graduants')
    graduants_id = cursor.fetchone()[0]
    insert_2 = "INSERT INTO Scores (`graduants_id`,`date`,`score_mathematics`,`score_ukrainian`,`score_english`,`score_physics`,`score_geography`) VALUES (%s,%s,%s,%s,%s,%s,%s)"
    values_2 = (graduants_id,'0000-00-00','0','0','0','0','0')
    try:
        cursor.execute(insert_2,values_2)
        mydb.commit()
        make_new_admin_ac(self)
    except mysql.connector.Error as error:
        print("Помилка під час вставки даних:", error)

def add_tbl_teacher(self,name_and_surname,email,phone,department,position,password):
    cursor = mydb.cursor()
    insert_query = "INSERT INTO Teacher (`first_name`,`last_name`,`email`,`contact_number`,`department`,`position`,`password`) VALUES (%s,%s,%s,%s,%s,%s,%s)"
    values = (name_and_surname[0],name_and_surname[1],email,phone,department,position,password)
    try:
        cursor.execute(insert_query,values)
        mydb.commit()
        make_new_admin_ac(self)
    except mysql.connector.Error as error:
        print("Помилка під час вставки даних:", error)

def help_to_show_labels(self,current_id_):
    self.lbl.setText(f'№ {current_id_}')
    self.label_2.setText('Оновлення даних')

def upd_some_ac_admin(self,current_id_):
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM Admin WHERE admin_id = %s", [current_id_])
    result = cursor.fetchone()
    
    if result:
        uic.loadUi('add_admin_for_admin.ui',self)
        help_to_show_labels(self,current_id_)
        self.admin_back.clicked.connect(self.make_new_admin_ac)
        self.admin_add_admin.clicked.connect(self.upd_admin_admin)

        self.take_name_and_surname.setText(result[1] + " " + result[2])
        self.take_email.setText(result[3])
        self.take_phone.setText(result[4])

    else:
        QMessageBox.about(self, "Виникла помилка!" ,"Вибачте, але адміністратора з таким ідентифікатором не існує")

def upd_some_ac_benefits(self,current_id_):
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM Benefits WHERE benefit_id = %s", [current_id_])
    result = cursor.fetchone()
    
    if result:
        uic.loadUi('add_benefits_for_admin.ui',self)
        help_to_show_labels(self,current_id_)
        self.admin_add_benefit.setText('Оновити')
        self.admin_back.clicked.connect(self.make_new_admin_ac)
        self.admin_add_benefit.clicked.connect(self.confirm_upd_benefits)

        self.take_benefit_name.setText(result[1])
        self.take_num_of_places.setText(str(result[2]))

    else:
        QMessageBox.about(self, "Виникла помилка!" ,"Вибачте, але квот з таким ідентифікатором не існує")

def confirm_upd_benefits(self,name,num_of_places,current_id_):
    cursor = mydb.cursor()
    update = "UPDATE Benefits SET benefit_name = %s, num_of_places = %s WHERE benefit_id = %s"
    values = (name,num_of_places,current_id_)
    try:
        cursor.execute(update, values)
        mydb.commit()
        make_new_admin_ac(self)

    except mysql.connector.Error as error:
        print("Помилка під час оновлення даних:", error)

def upd_some_ac_exams(self,current_id_):
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM Exams WHERE teacher_id = %s", [current_id_])
    result = cursor.fetchone()
    
    if result:
        uic.loadUi('add_exams_for_admin.ui',self)
        help_to_show_labels(self,current_id_)
        self.admin_add_exams.setText('Оновити')
        self.admin_back.clicked.connect(self.make_new_admin_ac)
        self.admin_add_exams.clicked.connect(self.confirm_upd_exams)

        self.take_exams_name.setText(result[1])
        self.take_exams_date.setText(str(result[2]))
        self.take_exams_min_pass.setText(str(result[3]))
        self.take_exams_time.setText(str(result[4]))
        self.take_faculty.setCurrentIndex(result[5])

    else:
        QMessageBox.about(self, "Виникла помилка!" ,"Вибачте, але вчителів з таким ідентифікатором не існує")

def confirm_upd_exams(self,exam_name,exam_date,min_pass,exam_time,exam_faculty,current_id):
    cursor = mydb.cursor()
    update = "UPDATE Exams SET name = %s, date = %s, min_passing_score = %s, time = %s, faculty_id = %s WHERE teacher_id = %s"
    values = (exam_name,exam_date,min_pass,exam_time,exam_faculty,current_id)
    try:
        cursor.execute(update, values)
        mydb.commit()
        make_new_admin_ac(self)

    except mysql.connector.Error as error:
        print("Помилка під час оновлення даних:", error)

def upd_some_ac_faculty(self,current_id_):
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM Faculty WHERE faculty_id = %s", [current_id_])
    result = cursor.fetchone()
    
    if result:
        uic.loadUi('add_faculty_for_admin.ui',self)
        help_to_show_labels(self,current_id_)
        self.admin_add_faculty.setText('Оновити')
        self.admin_back.clicked.connect(self.make_new_admin_ac)
        self.admin_add_faculty.clicked.connect(self.confirm_upd_faculty)

        self.take_faculty_name.setText(result[1])
        self.take_faculty_adress.setText(f"{result[2]} {result[3]} {result[4]} {result[5]}")
        self.take_faculty_phone.setText(result[6])
        self.take_comp_subject.setText(result[7])
        self.take_num_of_places.setText(str(result[8]))
        self.take_num_of_budget_places.setText(str(result[9]))

    else:
        QMessageBox.about(self, "Виникла помилка!" ,"Вибачте, але факультетів з таким ідентифікатором не існує")

def confirm_upd_faculty(self,faculty_name,faculty_adress,faculty_phone,comp_subject,num_of_places,num_of_budget_places,current_id_):
    cursor = mydb.cursor()
    update = "UPDATE Faculty SET name = %s, region = %s, city = %s, street = %s, house_number = %s, contact_number = %s, compulsory_subject = %s, all_number_of_places = %s, number_of_budget_places = %s WHERE faculty_id = %s"
    values = (faculty_name,faculty_adress[0],faculty_adress[1],faculty_adress[2],faculty_adress[3],faculty_phone,comp_subject,num_of_places,num_of_budget_places,current_id_)
    try:
        cursor.execute(update, values)
        mydb.commit()
        make_new_admin_ac(self)

    except mysql.connector.Error as error:
        print("Помилка під час оновлення даних:", error)

def upd_some_ac_graduants(self,current_id_):
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM Graduants WHERE graduants_id = %s", [current_id_])
    result = cursor.fetchone()
    
    if result:
        uic.loadUi('add_graduants_for_admin.ui',self)
        help_to_show_labels(self,current_id_)
        self.admin_add_graduants.setText('Оновити')
        self.admin_back.clicked.connect(self.make_new_admin_ac)
        self.admin_add_graduants.clicked.connect(self.confirm_upd_graduants)

        self.lineEdit_fullname.setText(result[1] + " " + result[2])
        self.lineEdit_2_email.setText(result[3])
        self.lineEdit_3_ph_num.setText(result[4])
        self.lineEdit_full_address.setText(result[5] + " " + result[6] + " " + result[7] + " " + result[8] + " " + result[9])
        self.lineEdit_2_inst_name.setText(result[11])
        self.lineEdit_3_num_atestat.setText(result[12])
        self.lineEdit_4_num_dodatok.setText(result[13])
    else:
        QMessageBox.about(self, "Виникла помилка!" ,"Вибачте, але абітурієнтів з таким ідентифікатором не існує")

def confirm_upd_graduants(self, name_and_surname, email, phone_number, full_address,ed_level,name_ed_institution,num_atestat,num_dodatok,faculty,benefits,password,current_id_):
    cursor = mydb.cursor()
    update_query = "UPDATE Graduants SET first_name = %s, last_name = %s, email = %s, contact_number = %s, region = %s, locality = %s, street = %s, `apartment number` = %s, flat = %s, ed_level = %s, name_ed_institution = %s, num_atestat = %s, num_dodatok = %s, faculty_id = %s, benefits = %s, password = %s WHERE graduants_id = %s"
    values = (name_and_surname[0], name_and_surname[1], email, phone_number, full_address[0], full_address[1], full_address[2], full_address[3], full_address[4], ed_level, name_ed_institution, num_atestat, num_dodatok, faculty, benefits, password, current_id_)

    try:
        cursor.execute(update_query, values)
        mydb.commit()
        make_new_admin_ac(self)

    except mysql.connector.Error as error:
        print("Помилка під час оновлення даних:", error)
    cursor.close()

def upd_some_ac_teacher(self,current_id_):
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM Teacher WHERE teacher_id = %s", [current_id_])
    result = cursor.fetchone()
    if result:
        uic.loadUi('add_teacher_for_admin.ui',self)
        help_to_show_labels(self,current_id_)
        self.admin_add_teacher.setText('Оновити')
        self.admin_back.clicked.connect(self.make_new_admin_ac)
        self.admin_add_teacher.clicked.connect(self.confirm_upd_teacher)

        self.lineEdit_date.setText(f"{result[1]} {result[2]}")
        self.lineEdit_date_2.setText(result[3])
        self.lineEdit_date_3.setText(result[4])
    else:
        QMessageBox.about(self, "Виникла помилка!" ,"Вибачте, але вчителів з таким ідентифікатором не існує")

def confirm_upd_teacher(self,name_and_surname,email,phone_number,teachers_faculty,teachers_posada,password,current_id_):
    cursor = mydb.cursor()
    update = "UPDATE Teacher SET first_name = %s, last_name = %s, email = %s, contact_number = %s,department = %s,position = %s, password = %s WHERE teacher_id = %s"
    values = (name_and_surname[0], name_and_surname[1], email, phone_number, teachers_faculty, teachers_posada, password, current_id_)

    try:
        cursor.execute(update, values)
        mydb.commit()
        make_new_admin_ac(self)

    except mysql.connector.Error as error:
        print("Помилка під час оновлення даних:", error)

    cursor.close()

def upd_some_ac_scores(self,current_id_):
    cursor = mydb.cursor()
    cursor.execute('SELECT * FROM Scores WHERE graduants_id = %s', [current_id_])
    result = cursor.fetchone()
    print(result)
    if result:
        uic.loadUi('add_scores_for_admin.ui',self)
        help_to_show_labels(self,current_id_)
        self.btn_upd.setText('Оновити')
        self.btn_back.clicked.connect(self.make_new_admin_ac)
        self.btn_upd.clicked.connect(self.confirm_upd_scores)

        self.lineEdit_date.setText(str(result[1]))
        self.lineEdit_ukr_mova.setText(str(result[2]))
        self.lineEdit_math.setText(str(result[3]))
        self.lineEdit_eng_mova.setText(str(result[4]))
        self.lineEdit_phis.setText(str(result[5]))
        self.lineEdit_geo.setText(str(result[6]))
    else:
        QMessageBox.about(self, "Виникла помилка!" ,"Вибачте, але абітурієнтів з таким ідентифікатором не існує")

def confirm_upd_scores(self,scores_date,ukr_mova,math,eng_mova,phis,geo,current_id_):
    cursor = mydb.cursor()
    update_scores = "UPDATE Scores SET date = %s, score_mathematics = %s, score_ukrainian = %s, score_english = %s, score_physics = %s, score_geography = %s WHERE graduants_id = %s"
    values = (scores_date,math,ukr_mova, eng_mova, phis, geo, current_id_)
    
    try:
        cursor.execute(update_scores, values)
        mydb.commit()
        make_new_admin_ac(self)
        
        cursor.execute("SELECT graduants_id, faculty_id FROM Graduants WHERE graduants_id = %s", [current_id_])
        result = cursor.fetchone()
        if result:
               graduants_id = result[0]
               faculty_id = result[1]
        cursor.execute("UPDATE Exams_results SET faculty_id = %s, average_score = get_average(%s), status = get_status(%s) WHERE graduants_id = %s", (faculty_id, graduants_id, graduants_id, graduants_id))
        mydb.commit()
    except mysql.connector.Error as error:
        print("Помилка під час оновлення даних:", error)
    
    cursor.close()


"""
!!!!!!!!!!!!!!!!!!!!!
ТІЧЕРИ
"""


def make_new_teach_ac(self):
    uic.loadUi('teacher_ac.ui', self)
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM Teacher WHERE contact_number = %s", [self.teach_phone])
    result = cursor.fetchone()
    
    if result:
        self.teach_id = result[0]
        self.label_id_2.setText("№ " + str(result[0]))
        self.label_full_name_2.setText(result[1] + " " + result[2])
        self.label_email_2.setText(result[3])
        self.label_num_ph_2.setText(result[4])
        self.label_faculty_3.setText(str(result[5]))
        self.label_posada.setText(str(result[6]))

        self.btn_delete_ac.clicked.connect(self.confirm_delete_account_teach)
        self.btn_upd_data.clicked.connect(self.update_new_teach)

        self.btn_scores.clicked.connect(self.show_teach_scores)
        self.btn_grad.clicked.connect(self.show_teach_no_scores)
        self.btn_edit_scores.clicked.connect(self.edit_table)

        self.btn_home_3.clicked.connect(self.show_start)

    cursor.close()

def insert_data_teacher(self, name_and_surname, email, phone_number, teachers_faculty, teachers_posada, password):
    cursor = mydb.cursor()
    insert_query = "INSERT INTO Teacher (`first_name`,`last_name`,`email`,`contact_number`,`department`,`position`, `password`) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    values = (name_and_surname[0], name_and_surname[1], email, phone_number, teachers_faculty, teachers_posada, password)

    self.teach_phone = phone_number
    try:
        cursor.execute(insert_query, values)
        mydb.commit()
        make_new_teach_ac(self)

    except mysql.connector.Error as error:
        print("Помилка під час вставки даних:", error)
    
    cursor.close()

def delete_teach_account(self):
    cursor = mydb.cursor()
    cursor.execute("DELETE FROM Teacher Where teacher_id = %s", (self.teach_id,))

    mydb.commit()
    cursor.close()
    QMessageBox.information(self, "Видалення аккаунту", "Аккаунт успішно видалено.")

def update_new_teach(self,name_and_surname, email, phone_number, teachers_faculty, teachers_posada, password, teach_id):
    cursor = mydb.cursor()
    update = "UPDATE Teacher SET first_name = %s, last_name = %s, email = %s, contact_number = %s,department = %s,position = %s, password = %s WHERE teacher_id = %s"
    values = (name_and_surname[0], name_and_surname[1], email, phone_number, teachers_faculty, teachers_posada, password, teach_id)

    try:
        cursor.execute(update, values)
        mydb.commit()
        make_new_teach_ac(self)

    except mysql.connector.Error as error:
        print("Помилка під час оновлення даних:", error)

    cursor.close()

def input_old_teach(self):
    cursor = mydb.cursor()

    select_query = "SELECT * FROM Teacher WHERE teacher_id = %s"
    select_values = (self.teach_id,)
    cursor.execute(select_query, select_values)
    old_data = cursor.fetchone()

    self.lineEdit_fullname.setText(old_data[1] + " " + old_data[2])
    self.lineEdit_2_email.setText(old_data[3])
    self.lineEdit_3_ph_num.setText(old_data[4])
    cursor.close()

def show_teach_scores(self):
    
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM Scores")
    result = cursor.fetchall()
    
    header = [desc[0] for desc in cursor.description]
    
    model = TableModel(result, header)
    self.tableView.setModel(model)
    for column in range(len(header)):
        self.tableView.setColumnWidth(column,120)
    cursor.close()

def show_teach_no_scores(self):
    
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM Scores where score_mathematics = 0 or score_ukrainian = 0 or (score_english = 0 and score_physics = 0 and score_geography = 0)")
    result = cursor.fetchall()
    
    header = [desc[0] for desc in cursor.description]
    
    model = TableModel(result, header)
    self.tableView.setModel(model)
    for column in range(len(header)):
        self.tableView.setColumnWidth(column,120)
    cursor.close()

def edit_table(self, ukr_mova, math, eng_mova, phis, geo, current_id_teach):
    cursor = mydb.cursor()
    update_scores = "UPDATE scores SET date = curdate(), score_mathematics = %s, score_ukrainian = %s, score_english = %s, score_physics = %s, score_geography = %s WHERE graduants_id = %s"
    values = (math,ukr_mova, eng_mova, phis, geo, current_id_teach)
    
    try:
        cursor.execute(update_scores, values)
        mydb.commit()
        make_new_teach_ac(self)

    except mysql.connector.Error as error:
        print("Помилка під час оновлення даних:", error)

    cursor.close()

def input_old_scores_teach(self):
    cursor = mydb.cursor()

    select_query = "SELECT * FROM scores WHERE graduants_id = %s"
    select_values = (self.current_id_teach,)
    cursor.execute(select_query, select_values)
    old_data = cursor.fetchone()

    self.label_id_2.setText("№ " + str(int(old_data[0])))
    self.lineEdit_ukr_mova.setText(str(int(old_data[3])))
    self.lineEdit_math.setText(str(int(old_data[2])))
    self.lineEdit_eng_mova.setText(str(int(old_data[4])))
    self.lineEdit_phis.setText(str(int(old_data[5])))
    self.lineEdit_geo.setText(str(int(old_data[6])))
    cursor.close()