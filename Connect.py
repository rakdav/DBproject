import pyodbc


class Connect:
    def __init__(self, db, user, password, server):
        self.connect = pyodbc.connect("Driver={SQL Server};"
                                      "Server=" + server + ";"
                                                           "Database=" + db + ";"
                                                                              "UID=" + user + ";"
                                                                                              "PWD=" + password + ";", autocommit=True)

    def InsertStaff(self, insertDict):
        con = self.connect
        cur = con.cursor()
        query = f"INSERT INTO staff " \
                f"values ('{insertDict['Surname']}'," \
                f"'{insertDict['Lastname']}'," \
                f"'{insertDict['BirthDay']}'," \
                f"'{insertDict['Phone']}'," \
                f"'{insertDict['Post']}'," \
                f"'{insertDict['Date_input']}'," \
                f"'{insertDict['Type_post']}')"
        try:
            cur.execute(query)
        except pyodbc.Error as err:
            print("Error", err)
        cur.close()

    def getStaffAll(self):
        con = self.connect
        cur = con.cursor()
        query = f"SELECT * FROM staff"
        try:
            cur.execute(query)
            rows = cur.fetchall()
        except pyodbc.Error as err:
            print("Error", err)
        cur.close()
        return rows

    def get_staff_by_surname(self, name):
        con = self.connect
        cur = con.cursor()
        query = f"SELECT * FROM staff WHERE Surname='"+name+"'"
        try:
            cur.execute(query)
            rows = cur.fetchall()
        except pyodbc.Error as err:
            print("Error", err)
        cur.close()
        return rows

