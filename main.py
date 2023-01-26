from datetime import datetime
from Connect import Connect


# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi():
    con = Connect("python", "user14", "user14", "LisenseServer\\sqlexpress")
    Print(con.getStaffAll())
    Print(con.get_staff_by_surname("dfdsfs"))


def Print(rows):
    for i in rows:
        print(str(i.Surname).strip(), str(i.Lastname).strip(), i.BirthDay,
              str(i.Phone).strip(),
              str(i.Post).strip(), i.Date_input,
              str(i.Type_post).strip(), sep=" ")


def InsertStaff(con):
    staff = dict()
    staff["Surname"] = input("Введите имя:")
    staff["Lastname"] = input("Введите фамилию:")
    date_birth = input("Введите рождения:")
    staff["BirthDay"] = date_birth
    staff["Phone"] = input("Введите телефон:")
    staff["Post"] = input("Введите должность:")
    date_post = input("Введите поступления:")
    staff["Date_input"] = date_post
    staff["Type_post"] = input("Введите тип должности:")
    con.InsertStaff(staff)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
