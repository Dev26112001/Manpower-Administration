# Manpower-Administration
# importing mysql connector
import mysql.connector

# making Connection
con = mysql.connector.connect(
    host="localhost", user="root", password="password", database="emp")


# Function to mAdd_Employee
def Add_Employ():
    Id = input("Enter Employ Id : ")

    # Checking if Employee with given Id
    # Already Exist or Not
    if (check_employee(Id) == True):
        print("Employee aready exists\nTry Again\n")
        menu()

    else:
        Name = input("Enter Employ Name : ")
        Post = input("Enter Employ Post : ")
        Salary = input("Enter Employ Salary : ")
        data = (Id, Name, Post, Salary)

        # Inserting Employee details in
        # the Employee Table
        sql = 'insert into empd values(%s,%s,%s,%s)'
        c = con.cursor()

        # Executing the SQL Query
        c.execute(sql, data)

        # commit() method to make changes in
        # the table
        con.commit()
        print("Employ Added Successfully ")
        menu()


# Function to Promote Employee
def Promote_Employee():
    Id = int(input("Enter Employ's Id"))

    # Checking if Employee with given Id
    # Exist or Not
    if (check_employee(Id) == False):
        print("Employee does not exists\nTry Again\n")
        menu()
    else:
        Amount = int(input("Enter increase in Salary"))

        # Query to Fetch Salary of Employee
        # with given Id
        sql = 'select salary from empd where id=%s'
        data = (Id,)
        c = con.cursor()

        # Executing the SQL Query
        c.execute(sql, data)

        # Fetching Salary of Employee with given Id
        r = c.fetchone()
        t = r[0] + Amount

        # Query to Update Salary of Employee with
        # given Id
        sql = 'update empd set salary=%s where id=%s'
        d = (t, Id)

        # Executing the SQL Query
        c.execute(sql, d)

        # commit() method to make changes in the table
        con.commit()
        print("Employe Promoted")
        menu()


# Function to Remove Employee with given Id
def Remove_Employ():
    Id = input("Enter Employ Id : ")

    # Checking if Employee with given Id Exist
    # or Not
    if (check_employee(Id) == False):
        print("Employee does not exists\nTry Again\n")
        menu()
    else:

        # Query to Delete Employye from Table
        sql = 'delete from empd where id=%s'
        data = (Id,)
        c = con.cursor()

        # Executing the SQL Query
        c.execute(sql, data)

        # commit() method to make changes in
        # the table
        con.commit()
        print("Employee Removed")
        menu()


# Function To Check if Employee with
# given Id Exist or Not
def check_employee(employee_id):
    # Query to select all Rows f
    # rom employee Table
    sql = 'select * from empd where id=%s'

    # making cursor buffered to make
    # rowcount method work properly
    c = con.cursor(buffered=True)
    data = (employee_id,)

    # Executing the SQL Query
    c.execute(sql, data)

    # rowcount method to find
    # number of rows with given values
    r = c.rowcount
    if r == 1:
        return True
    else:
        return False


# Function to Display All Employees
# from Employee Table
def Display_Employees():
    # query to select all rows from
    # Employee Table
    sql = 'select * from empd'
    c = con.cursor()

    # Executing the SQL Query
    c.execute(sql)

    # Fetching all details of all the
    # Employees
    r = c.fetchall()
    for i in r:
        print("Employ Id : ", i[0])
        print("Employ Name : ", i[1])
        print("Employ Post : ", i[2])
        print("Employ Salary : ", i[3])
        print("---------------------\
		-----------------------------\
		------------------------------\
		---------------------")

    menu()


# menu function to display menu
def menu():
    print("Welcome to Employ Management Record")
    print("Press ")
    print("1 to Add Employ")
    print("2 to Remove Employ ")
    print("3 to Promote Employ")
    print("4 to Display Employees")
    print("5 to Exit")

    ch = int(input("Enter your Choice "))
    if ch == 1:
        Add_Employ()
    elif ch == 2:
        Remove_Employ()
    elif ch == 3:
        Promote_Employee()
    elif ch == 4:
        Display_Employees()
    elif ch == 5:
        exit(0)
    else:
        print("Invalid Choice")
        menu()


# Calling menu function
menu()
