from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
import MySQLdb
from PyQt5.uic import loadUiType
import datetime
from xlrd import *
from xlsxwriter import *

ui,_ = loadUiType('hospital.ui')

login,_ = loadUiType('login.ui')

class Login(QWidget , login):
    def __init__(self):
        QWidget.__init__(self)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.Handel_Login)
        style = open('themes/darkgray.css' , 'r')
        style = style.read()
        self.setStyleSheet(style)

    def Handel_Login(self):

        self.db = MySQLdb.connect(host='localhost', user='root', password='Rohan@2001', db='hospital')
        self.cur = self.db.cursor()

        username = self.lineEdit.text()
        password = self.lineEdit_2.text()

        sql = ''' SELECT * FROM users'''

        self.cur.execute(sql)
        data = self.cur.fetchall()
        for row in data:
            if username == row[1] and password == row[3]:
                print('User Matched')
                self.window2 = MainApp()
                self.close()
                self.window2.show()

            else:
                self.label.setText('Make Sure You Enter Your Username And Password Correctly')




class MainApp(QMainWindow ,ui):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.Handel_UI_Changes()
        self.Handel_Buttons()
        self.Black1_Theme()

        self.Show_Discardable_Inventory_Quantity()
        self.Show_Replaceable_Inventory_Quantity()
        self.Show_Purchasable_Inventory_Quantity()

        self.Show_Discardable_Inventory_Quantity_Combobox()
        self.Show_Replaceable_Inventory_Quantity_Combobox()
        self.Show_Purchasable_Inventory_Quantity_Combobox()

        self.Show_All_Inventory()
        self.Show_All_Hospitals()

        self.Show_All_Records()

     

    def Handel_UI_Changes(self):
        self.Hiding_Themes()
        self.tabWidget.tabBar().setVisible(False)

    def Handel_Buttons(self):
        self.pushButton_3.clicked.connect(self.Show_Themes)
        self.pushButton_13.clicked.connect(self.Hiding_Themes)

        self.pushButton.clicked.connect(lambda:self.Open_Records_Tab())
        self.pushButton_2.clicked.connect(lambda:self.Open_Inventory_Tab())
        self.pushButton_26.clicked.connect(lambda:self.Open_Hospital_Tab())
        self.pushButton_14.clicked.connect(lambda:self.Open_Users_Tab())
        self.pushButton_18.clicked.connect(lambda:self.Open_Supply_Tab())

        self.pushButton_5.clicked.connect(lambda:self.Add_New_Inventory())
        self.pushButton_7.clicked.connect(lambda:self.Search_Inventory())
        self.pushButton_6.clicked.connect(lambda:self.Edit_Inventory())
        self.pushButton_8.clicked.connect(lambda:self.Delete_Inventory())

        self.pushButton_19.clicked.connect(lambda:self.Add_Discardable_Inventory_Quantity())
        self.pushButton_20.clicked.connect(lambda:self.Add_Replaceable_Inventory_Quantity())
        self.pushButton_21.clicked.connect(lambda:self.Add_Purchasable_Inventory_Quantity())

        self.pushButton_15.clicked.connect(lambda:self.Add_New_User())
        self.pushButton_16.clicked.connect(lambda:self.Login())
        self.pushButton_17.clicked.connect(lambda:self.Edit_User())

        self.pushButton_9.clicked.connect(lambda:self.Black1_Theme())
        self.pushButton_10.clicked.connect(lambda:self.Black2_Theme())
        self.pushButton_11.clicked.connect(lambda:self.Dark_Gray_Theme())
        self.pushButton_12.clicked.connect(lambda:self.Dark_Blue_Theme())

        self.pushButton_22.clicked.connect(lambda:self.Add_New_Hospital())
        self.pushButton_24.clicked.connect(lambda:self.Search_Hospital())
        self.pushButton_23.clicked.connect(lambda:self.Edit_Hospital())
        self.pushButton_25.clicked.connect(lambda:self.Delete_Hospital())

        self.pushButton_4.clicked.connect(lambda:self.Handel_Records())

        self.pushButton_29.clicked.connect(lambda:self.Export_Records())
        self.pushButton_27.clicked.connect(lambda:self.Export_Inventory())
        self.pushButton_28.clicked.connect(lambda:self.Export_Hospitals())



    def Show_Themes(self):
        self.groupBox.show()

    def Hiding_Themes(self):
        self.groupBox.hide()

    #################################################
    ################# Opening Tabs ##################

    def Open_Records_Tab(self):
        self.tabWidget.setCurrentIndex(0)

    def Open_Inventory_Tab(self):
        self.tabWidget.setCurrentIndex(1)

    def Open_Hospital_Tab(self):
        self.tabWidget.setCurrentIndex(2)

    def Open_Users_Tab(self):
        self.tabWidget.setCurrentIndex(3)

    def Open_Supply_Tab(self):
        self.tabWidget.setCurrentIndex(4)

    #################################################
    #################### Records ####################

    def Handel_Records(self):

        inventory_name = self.lineEdit.text()
        inventory_quantity = self.lineEdit_13.text()
        days = self.comboBox_2.currentIndex() + 1
        replacement_status = self.comboBox_3.currentText()
        inventory_status = self.comboBox.currentText()
        current_status = self.comboBox_4.currentText()
        today_date = datetime.date.today()
        to_date = today_date + datetime.timedelta(days=expiry)

        print(today_date)
        print(to_date)

        self.db = MySQLdb.connect(host='localhost', user='root', password='Rohan@2001', db='hospital')
        self.cur = self.db.cursor()

        self.cur.execute('''
            INSERT INTO records(inventory_name , inventory_quantity , current_status , replacement_status , 
            inventory_status , days , date , to_date)
            VALUES (%s , %s , %s , %s , %s , %s , %s , %s)
        ''', (inventory_name , inventory_quantity , current_status , replacement_status , inventory_status , days , today_date  , to_date))

        self.db.commit()
        self.statusBar().showMessage('New Operation Added')

        self.Show_All_Records()

    def Show_All_Records(self):

        self.db = MySQLdb.connect(host='localhost', user='root', password='Rohan@2001', db='hospital')
        self.cur = self.db.cursor()

        self.cur.execute(''' 
            SELECT inventory_name , inventory_quantity , current_status , replacement_status , inventory_status 
                   , date , to_date FROM records
        ''')

        data = self.cur.fetchall()

        print(data)

        self.tableWidget.setRowCount(0)
        self.tableWidget.insertRow(0)
        for row , form in enumerate(data):
            for column , item in enumerate(form):
                self.tableWidget.setItem(row , column , QTableWidgetItem(str(item)))
                column += 1

            row_position = self.tableWidget.rowCount()
            self.tableWidget.insertRow(row_position)



    #################################################
    #################### Inventory ######################


    def Show_All_Inventory(self):

        self.db = MySQLdb.connect(host='localhost', user='root', password='Rohan@2001', db='hospital')
        self.cur = self.db.cursor()

        self.cur.execute(''' SELECT inventory_name , inventory_description , inventory_status , inventory_quantity , 
         discardable_inventory_quantity , replaceable_inventory_quantity , purchasable_inventory_quantity ,
         required_currency FROM inventory ''')
        data = self.cur.fetchall()

        print(data)
        self.tableWidget_5.setRowCount(0)
        self.tableWidget_5.insertRow(0)

        for row, form in enumerate(data):
            for column, item in enumerate(form):
                self.tableWidget_5.setItem(row, column, QTableWidgetItem(str(item)))
                column += 1

            row_position = self.tableWidget_5.rowCount()
            self.tableWidget_5.insertRow(row_position)

        self.db.close()



    def Add_New_Inventory(self):

        self.db = MySQLdb.connect(host='localhost' , user='root' , password='Rohan@2001' , db='hospital')
        self.cur = self.db.cursor()

        inventory_name = self.lineEdit_2.text()
        inventory_description = self.textEdit_3.toPlainText()
        inventory_status = self.comboBox_6.currentText()
        inventory_quantity = self.lineEdit_21.text()
        discardable_inventory_quantity = self.comboBox_10.currentText()
        replaceable_inventory_quantity = self.comboBox_12.currentText()
        purchasable_inventory_quantity = self.comboBox_11.currentText()
        required_currency = self.lineEdit_24.text()

        self.cur.execute('''
            INSERT INTO inventory(inventory_name,inventory_description,inventory_status,inventory_quantity,discardable_inventory_quantity,
            replaceable_inventory_quantity,purchasable_inventory_quantity,required_currency)
            VALUES (%s , %s , %s , %s , %s , %s , %s , %s)
        ''' ,(inventory_name , inventory_description , inventory_status , inventory_quantity , discardable_inventory_quantity ,
              replaceable_inventory_quantity , purchasable_inventory_quantity,required_currency,))

        self.db.commit()
        self.statusBar().showMessage('New Inventory Added')

        self.lineEdit_2.setText('')
        self.textEdit_3.setPlainText('')
        self.comboBox_6.setCurrentIndex(0)
        self.lineEdit_21.setText('')
        self.comboBox_10.setCurrentIndex(0)
        self.comboBox_12.setCurrentIndex(0)
        self.comboBox_11.setCurrentIndex(0)
        self.lineEdit_24.setText('')
        self.Show_All_Inventory()


    def Search_Inventory(self):

        self.db = MySQLdb.connect(host='localhost', user='root', password='Rohan@2001', db='hospital')
        self.cur = self.db.cursor()

        inventory_name = self.lineEdit_3.text()

        sql = ''' SELECT * FROM inventory WHERE inventory_name = %s'''
        self.cur.execute(sql , [(inventory_name)])

        data = self.cur.fetchone()

        print((data))
        self.lineEdit_8.setText(data[1])
        self.textEdit_2.setPlainText(str(data[2]))
        self.comboBox_5.setCurrentText(str(data[3]))
        self.lineEdit_7.setText(str(data[4]))
        self.comboBox_7.setCurrentText(str(data[5]))
        self.comboBox_8.setCurrentText(str(data[6]))
        self.comboBox_9.setCurrentText(str(data[7]))
        self.lineEdit_23.setText(str(data[8]))





    def Edit_Inventory(self):

        self.db = MySQLdb.connect(host='localhost', user='root', password='Rohan@2001', db='hospital')
        self.cur = self.db.cursor()

        inventory_name = self.lineEdit_8.text()
        inventory_description = self.textEdit_2.toPlainText()
        inventory_status = self.comboBox_5.currentText()
        inventory_quantity = self.lineEdit_7.text()
        discardable_inventory_quantity = self.comboBox_7.currentText()
        replaceable_inventory_quantity = self.comboBox_8.currentText()
        purchasable_inventory_quantity = self.comboBox_9.currentText()
        required_currency = self.lineEdit_23.text()

        search_inventory_name = self.lineEdit_3.text()

        self.cur.execute('''
            UPDATE inventory SET inventory_name = %s ,inventory_description = %s ,inventory_status = %s ,inventory_quantity = %s ,discardable_inventory_quantity = %s ,
            replaceable_inventory_quantity = %s ,purchasable_inventory_quantity = %s ,required_currency = %s WHERE inventory_name = %s 
            ''', (inventory_name , inventory_description , inventory_status , inventory_quantity , discardable_inventory_quantity ,
              replaceable_inventory_quantity , purchasable_inventory_quantity , required_currency , search_inventory_name))

        self.db.commit()
        self.statusBar().showMessage('Inventory Updated')
        self.Show_All_Inventory()




    def Delete_Inventory(self):

        self.db = MySQLdb.connect(host='localhost', user='root', password='Rohan@2001', db='hospital')
        self.cur = self.db.cursor()

        inventory_name = self.lineEdit_3.text()

        warning = QMessageBox.warning(self , 'Delete Inventory' , "Are You Sure You Want To Delete The Inventory From Rohan's Database" , QMessageBox.Yes | QMessageBox.No)
        if warning == QMessageBox.Yes :
            sql = ''' DELETE FROM inventory WHERE inventory_name = %s '''
            self.cur.execute(sql , [(inventory_name)])
            self.db.commit()
            self.statusBar().showMessage('Inventory Deleted')
            self.Show_All_Inventory()



    #################################################
    #################### Hospitals ##################


    def Show_All_Hospitals(self):

        self.db = MySQLdb.connect(host='localhost', user='root', password='Rohan@2001', db='hospital')
        self.cur = self.db.cursor()

        self.cur.execute(''' SELECT hospital_name , hospital_email , hospital_nationalid FROM hospital ''')
        data = self.cur.fetchall()

        print(data)
        self.tableWidget_6.setRowCount(0)
        self.tableWidget_6.insertRow(0)

        for row, form in enumerate(data):
            for column, item in enumerate(form):
                self.tableWidget_6.setItem(row, column, QTableWidgetItem(str(item)))
                column += 1

            row_position = self.tableWidget_6.rowCount()
            self.tableWidget_6.insertRow(row_position)

        self.db.close()

    def Add_New_Hospital(self):

        hospital_name = self.lineEdit_6.text()
        hospital_email = self.lineEdit_22.text()
        hospital_nationalid = self.lineEdit_25.text()

        self.db = MySQLdb.connect(host='localhost', user='root', password='Rohan@2001', db='hospital')
        self.cur = self.db.cursor()

        self.cur.execute('''
                    INSERT INTO hospital(hospital_name , hospital_email , hospital_nationalid)
                    VALUES (%s , %s , %s)
                ''', (hospital_name, hospital_email, hospital_nationalid))
        self.db.commit()
        self.db.close()
        self.statusBar().showMessage('New Hospital Added')
        self.Show_All_Hospitals()



    def Search_Hospital(self):

        hospital_nationalid = self.lineEdit_12.text()

        self.db = MySQLdb.connect(host='localhost', user='root', password='Rohan@2001', db='hospital')
        self.cur = self.db.cursor()

        sql = ''' SELECT * FROM hospital WHERE hospital_nationalid = %s '''
        self.cur.execute(sql, [(hospital_nationalid)])
        data = self.cur.fetchone()
        print(data)

        self.lineEdit_11.setText(data[1])
        self.lineEdit_26.setText(data[2])
        self.lineEdit_30.setText(data[3])




    def Edit_Hospital(self):

        hospital_original_national_id = self.lineEdit_12.text()
        hospital_name = self.lineEdit_11.text()
        hospital_email = self.lineEdit_26.text()
        hospital_national_id = self.lineEdit_30.text()

        self.db = MySQLdb.connect(host='localhost', user='root', password='Rohan@2001', db='hospital')
        self.cur = self.db.cursor()

        self.cur.execute('''
                    UPDATE hospital SET hospital_name = %s , hospital_email = %s , hospital_nationalid = %s WHERE hospital_nationalid = %s
                ''', (hospital_name, hospital_email, hospital_national_id, hospital_original_national_id))
        self.db.commit()
        self.db.close()
        self.statusBar().showMessage('Hospital Data Updated ')
        self.Show_All_Hospitals()

    def Delete_Hospital(self):

        hospital_original_national_id = self.lineEdit_12.text()

        warning_message = QMessageBox.warning(self, "Delete Hospital", "Are You Sure You Want To Delete This Hospital?",
                                              QMessageBox.Yes | QMessageBox.No)

        if warning_message == QMessageBox.Yes:
            self.db = MySQLdb.connect(host='localhost', user='root', password='Rohan@2001', db='hospital')
            self.cur = self.db.cursor()

            sql = ''' DELETE FROM hospital WHERE hospital_nationalid = %s '''
            self.cur.execute(sql, [(hospital_original_national_id)])

            self.db.commit()
            self.db.close()
            self.statusBar().showMessage('Hospital Deleted ')
            self.Show_All_Hospitals()

    #################################################
    #################### Users ######################

    def Add_New_User(self):

        self.db = MySQLdb.connect(host='localhost', user='root', password='Rohan@2001', db='hospital')
        self.cur = self.db.cursor()

        username = self.lineEdit_4.text()
        email = self.lineEdit_5.text()
        password = self.lineEdit_9.text()
        password2 = self.lineEdit_10.text()

        if password == password2 :
            self.cur.execute('''
                INSERT INTO users(user_name , user_email , user_password)
                VALUES (%s , %s , %s)
            ''' , (username , email , password))

            self.db.commit()
            self.statusBar().showMessage('New User Added')

        else:
            self.label_5.setText('Please Enter a Valid Password!!!')



    def Login(self):

        self.db = MySQLdb.connect(host='localhost', user='root', password='Rohan@2001', db='hospital')
        self.cur = self.db.cursor()

        username = self.lineEdit_14.text()
        password = self.lineEdit_15.text()

        sql = ''' SELECT * FROM users'''

        self.cur.execute(sql)
        data = self.cur.fetchall()
        for row in data:
            if username == row[1] and password == row[3]:
                print('User Matched')
                self.statusBar().showMessage('Valid Username & Password')
                self.groupBox_4.setEnabled(True)

                self.lineEdit_16.setText(row[1])
                self.lineEdit_17.setText(row[2])
                self.lineEdit_18.setText(row[3])


    def Edit_User(self):

        username = self.lineEdit_16.text()
        email = self.lineEdit_17.text()
        password = self.lineEdit_18.text()
        password2 = self.lineEdit_19.text()

        original_name = self.lineEdit_14.text()

        if password == password2:
            self.db = MySQLdb.connect(host='localhost', user='root', password='Rohan@2001', db='hospital')
            self.cur = self.db.cursor()

            print(username)
            print(email)
            print(password)

            self.cur.execute('''
                           UPDATE users SET user_name=%s , user_email=%s , user_password=%s WHERE user_name=%s
                       ''', (username, email, password, original_name))

            self.db.commit()
            self.statusBar().showMessage('User Data Updated Successfully')

        else:
            print('Incorrect Password!!!')

    #################################################
    #################### Supply ######################

    def Add_Discardable_Inventory_Quantity(self):

        self.db = MySQLdb.connect(host='localhost', user='root', password='Rohan@2001', db='hospital')
        self.cur = self.db.cursor()

        discardable_inventory_quantity = self.lineEdit_27.text()

        self.cur.execute('''
            INSERT INTO discardable_inventory (discardable_inventory_quantity) VALUES (%s)
        ''' , (discardable_inventory_quantity,))

        self.db.commit()
        self.statusBar().showMessage('New Quantity of Discardable Inventory Added')
        self.lineEdit_27.setText('')
        self.Show_Discardable_Inventory_Quantity()
        self.Show_Discardable_Inventory_Quantity_Combobox()


    def Show_Discardable_Inventory_Quantity(self):

        self.db = MySQLdb.connect(host='localhost' , user='root' , password='Rohan@2001' , db='hospital')
        self.cur = self.db.cursor()

        self.cur.execute(''' SELECT discardable_inventory_quantity FROM discardable_inventory''')
        data = self.cur.fetchall()

        if data :
            self.tableWidget_2.setRowCount(0)
            self.tableWidget_2.insertRow(0)
            for row , form in enumerate(data):
                for column , item in enumerate(form) :
                    self.tableWidget_2.setItem(row , column , QTableWidgetItem(str(item)))
                    column += 1

                row_position = self.tableWidget_2.rowCount()
                self.tableWidget_2.insertRow(row_position)



    def Add_Replaceable_Inventory_Quantity(self):

        self.db = MySQLdb.connect(host='localhost', user='root', password='Rohan@2001', db='hospital')
        self.cur = self.db.cursor()

        replaceable_inventory_quantity = self.lineEdit_28.text()

        self.cur.execute('''
                    INSERT INTO replaceable_inventory (replaceable_inventory_quantity) VALUES (%s)
                ''', (replaceable_inventory_quantity,))

        self.db.commit()
        self.lineEdit_28.setText('')
        self.statusBar().showMessage('New Quantity of Replaceable Inventory Added')
        self.Show_Replaceable_Inventory_Quantity()
        self.Show_Replaceable_Inventory_Quantity_Combobox()

    def Show_Replaceable_Inventory_Quantity(self):

        self.db = MySQLdb.connect(host='localhost', user='root', password='Rohan@2001', db='hospital')
        self.cur = self.db.cursor()

        self.cur.execute(''' SELECT replaceable_inventory_quantity FROM replaceable_inventory''')
        data = self.cur.fetchall()

        print(data)

        if data:
            self.tableWidget_3.setRowCount(0)
            self.tableWidget_3.insertRow(0)
            for row, form in enumerate(data):
                for column, item in enumerate(form):
                    self.tableWidget_3.setItem(row, column, QTableWidgetItem(str(item)))
                    column += 1

                row_position = self.tableWidget_3.rowCount()
                self.tableWidget_3.insertRow(row_position)


    def Add_Purchasable_Inventory_Quantity(self):

        self.db = MySQLdb.connect(host='localhost', user='root', password='Rohan@2001', db='hospital')
        self.cur = self.db.cursor()

        purchasable_inventory_quantity = self.lineEdit_29.text()

        self.cur.execute('''
                           INSERT INTO purchasable_inventory (purchasable_inventory_quantity) VALUES (%s)
                       ''', (purchasable_inventory_quantity,))

        self.db.commit()
        self.lineEdit_29.setText('')
        self.statusBar().showMessage('New Quantity of Purchasable Inventory Added')
        self.Show_Purchasable_Inventory_Quantity()
        self.Show_Purchasable_Inventory_Quantity_Combobox()


    def Show_Purchasable_Inventory_Quantity(self):

        self.db = MySQLdb.connect(host='localhost', user='root', password='Rohan@2001', db='hospital')
        self.cur = self.db.cursor()

        self.cur.execute(''' SELECT purchasable_inventory_quantity FROM purchasable_inventory''')
        data = self.cur.fetchall()

        print(data)

        if data:
            self.tableWidget_4.setRowCount(0)
            self.tableWidget_4.insertRow(0)
            for row, form in enumerate(data):
                for column, item in enumerate(form):
                    self.tableWidget_4.setItem(row, column, QTableWidgetItem(str(item)))
                    column += 1

                row_position = self.tableWidget_4.rowCount()
                self.tableWidget_4.insertRow(row_position)



    ####################################################
    ######### Show Supply data in UI #################


    def Show_Discardable_Inventory_Quantity_Combobox(self):
        self.db = MySQLdb.connect(host='localhost', user='root', password='Rohan@2001', db='hospital')
        self.cur = self.db.cursor()

        self.cur.execute(''' SELECT discardable_inventory_quantity FROM discardable_inventory ''')
        data = self.cur.fetchall()

        self.comboBox_10.clear()
        for discardable_inventory_quantity in data :
            self.comboBox_10.addItem(str(discardable_inventory_quantity[0]))
            self.comboBox_7.addItem(str(discardable_inventory_quantity[0]))



    def Show_Replaceable_Inventory_Quantity_Combobox(self):
        self.db = MySQLdb.connect(host='localhost', user='root', password='Rohan@2001', db='hospital')
        self.cur = self.db.cursor()

        self.cur.execute(''' SELECT replaceable_inventory_quantity FROM replaceable_inventory ''')
        data = self.cur.fetchall()

        self.comboBox_12.clear()
        for replaceable_inventory_quantity in data :
            self.comboBox_12.addItem(str(replaceable_inventory_quantity[0]))
            self.comboBox_8.addItem(str(replaceable_inventory_quantity[0]))



    def Show_Purchasable_Inventory_Quantity_Combobox(self):
        self.db = MySQLdb.connect(host='localhost', user='root', password='Rohan@2001', db='hospital')
        self.cur = self.db.cursor()

        self.cur.execute(''' SELECT purchasable_inventory_quantity FROM purchasable_inventory ''')
        data = self.cur.fetchall()

        self.comboBox_11.clear()
        for purchasable_inventory_quantity in data :
            self.comboBox_11.addItem(str(purchasable_inventory_quantity[0]))
            self.comboBox_9.addItem(str(purchasable_inventory_quantity[0]))


    ########################################
    ######### Export Data #################

    def Export_Records(self):
        self.db = MySQLdb.connect(host='localhost', user='root', password='Rohan@2001', db='hospital')
        self.cur = self.db.cursor()

        self.cur.execute(''' 
            SELECT inventory_name , inventory_quantity , current_status , replacement_status , inventory_status 
                   , date , to_date FROM records
        ''')

        data = self.cur.fetchall()
        wb = Workbook('records.xlsx')
        sheet1 = wb.add_worksheet()

        sheet1.write(0, 0, 'Inventory Name')
        sheet1.write(0, 1, 'Inventory Quantity')
        sheet1.write(0, 2, 'Current Status')
        sheet1.write(0, 3, 'Replacement Status')
        sheet1.write(0, 4, 'Inventory Status')
        sheet1.write(0, 5, 'From - Date')
        sheet1.write(0, 6, 'To - Date')

        row_number = 1
        for row in data:
            column_number = 0
            for item in row:
                sheet1.write(row_number, column_number, str(item))
                column_number += 1
            row_number += 1

        wb.close()
        self.statusBar().showMessage('Records Report Created Successfully')

    def Export_Inventory(self):
        self.db = MySQLdb.connect(host='localhost', user='root', password='Rohan@2001', db='hospital')
        self.cur = self.db.cursor()

        self.cur.execute(
            ''' SELECT inventory_name , inventory_description , inventory_status , inventory_quantity , 
         discardable_inventory_quantity , replaceable_inventory_quantity , purchasable_inventory_quantity ,
         required_currency FROM inventory''')
        data = self.cur.fetchall()

        wb = Workbook('inventory.xlsx')
        sheet1 = wb.add_worksheet()

        sheet1.write(0, 0, 'Inventory Name')
        sheet1.write(0, 1, 'Inventory Description')
        sheet1.write(0, 2, 'Inventory Status')
        sheet1.write(0, 3, 'Inventory Quantity')
        sheet1.write(0, 4, 'Discardable Inventory Quantity')
        sheet1.write(0, 5, 'Replaceable Inventory Quantity')
        sheet1.write(0, 6, 'Purchasable Inventory Quantity')
        sheet1.write(0, 7, 'Required Currency')

        row_number = 1
        for row in data:
            column_number = 0
            for item in row:
                sheet1.write(row_number, column_number, str(item))
                column_number += 1
            row_number += 1

        wb.close()
        self.statusBar().showMessage('Inventory Report Created Successfully')

    def Export_Hospitals(self):
        self.db = MySQLdb.connect(host='localhost', user='root', password='Rohan@2001', db='hospital')
        self.cur = self.db.cursor()

        self.cur.execute(''' SELECT hospital_name , hospital_email , hospital_nationalid FROM hospital ''')
        data = self.cur.fetchall()

        wb = Workbook('hospitals.xlsx')
        sheet1 = wb.add_worksheet()

        sheet1.write(0, 0, 'Hospital Name')
        sheet1.write(0, 1, 'Hospital Email')
        sheet1.write(0, 2, 'Hospital NationalID')

        row_number = 1
        for row in data:
            column_number = 0
            for item in row:
                sheet1.write(row_number, column_number, str(item))
                column_number += 1
            row_number += 1

        wb.close()
        self.statusBar().showMessage('Hospitals Report Created Successfully')

    ####################################################
    #################### UI Themes #####################

    def Dark_Blue_Theme(self):
        style = open('themes/darkblue.css', 'r')
        style = style.read()
        self.setStyleSheet(style)

    def Dark_Gray_Theme(self):
        style = open('themes/darkgray.css', 'r')
        style = style.read()
        self.setStyleSheet(style)

    def Black2_Theme(self):
        style = open('themes/black2.css', 'r')
        style = style.read()
        self.setStyleSheet(style)

    def Black1_Theme(self):
        style = open('themes/black1.css', 'r')
        style = style.read()
        self.setStyleSheet(style)


def main():
    app = QApplication(sys.argv)
    window = Login()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()