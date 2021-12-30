import mysql.connector


class gts_Database:
    def __init__(self):
        self.mydb = mysql.connector.connect(host = 'localhost',
                               user ='user name',
                               password = 'your password',
                               database = 'gts')
        cur = self.mydb.cursor()
        print(self.mydb.connection_id)
        #Create tables into gts database;
        gtstbl = ("CREATE TABLE IF NOT EXISTS EMPLOYEES(Emp_id int primary key, Emp_name varchar(15), Emp_department varchar(25))")
        cur.execute(gtstbl)
        self.mydb.commit()
        print("Table Created succesfully into gts database.")
        print("\n")

#Insert values into gts database table...
    def insert(self):
        Emp_id = int(input("Enter Employee id: "));
        Emp_name = input("Enter Employee name: ");
        Emp_department = input("Enter Employee department: ")
        insert = ("INSERT INTO EMPLOYEES(EMP_id , Emp_name , Emp_department) values(%s,%s,%s)")
        records = (Emp_id,Emp_name,Emp_department)
        cur = self.mydb.cursor()
        cur.execute(insert, records)
        self.mydb.commit()
        print("Records Inserted succesfully.")
        print("\n")

#Display data of gts database tables...
    def display(self):
        print("\nYour Data is Here.")
        display = ("SELECT * FROM employees")
        cur = self.mydb.cursor()
        cur.execute(display)
        record = cur.fetchall()
        for rec in record:
            print(rec)
            self.mydb.commit()

            print("\n")

#Delete data from gts database table...
    def delete(self):
        Emp_id = int(input("Enter Employee id which you want to delete: "))
        delete = ("DELETE FROM employees WHERE Emp_id = '%d'" %Emp_id)
        cur  =self.mydb.cursor()
        cur.execute(delete, Emp_id)
        self.mydb.commit()
        print("Record Deleted successfully.")
        print("\n")
    
    def update(self):
        print("What do you want to change in this table.")
        print("1.Employee Id.")
        print("2.Employee Name.")
        print("3.Employee Department.")
        opt = int(input())
        if opt == 1:
            Emp_id = int(input("Enter Employee id in which you want to change: "))
            newid = input("Enter New Id: ")
            update_id = ("UPDATE EMPLOYEES SET Emp_id = %s WHERE Emp_id = %s")
            updatedata = (newid,Emp_id)
            cur = self.mydb.cursor()
            cur.execute(update_id , updatedata)
            self.mydb.commit()
            print("Record updated successfully.")
            print("\n")
        elif opt == 2:
            Emp_id = int(input("Enter Employee id in which you want to change: "))
            newname = input("Enter New Name: ")
            update_name = ("UPDATE EMPLOYEES SET Emp_name = %s WHERE Emp_id = %s")
            updatedata = (newname,Emp_id)
            cur = self.mydb.cursor()
            cur.execute(update_name , updatedata)
            self.mydb.commit()
            print("Record updated successfully.")
            print("\n")
        elif opt == 3:
            Emp_id = int(input("Enter Employee id in which you want to change: "))
            newdepartment = input("Enter new department:")
            updatedepartment = ("UPDATE EMPLOYEES SET Emp_department = %s WHERE Emp_id = %s")
            updatedata = (newdepartment,Emp_id)
            cur = self.mydb.cursor()
            cur.execute(updatedepartment , updatedata)
            self.mydb.commit()
            print("Record updated successfully.")
            print("\n")
        else:
            print("Something Went wrong//...")
       
     
def main():
    gts = gts_Database()
    while True:
        print("***** Welcome into Gts Database *****")
        print("     PRESS 1.FOR INSERT NEW DATA     ")
        print("     PRESS 2.FOR DISPLAY DATA        ")
        print("     PRESS 3.FOR DELETE DATA         ")
        print("     PRESS 4.FOR UPDATE DATA         ")
        print("     PRESS 5.FOR EXIT                ")
        print()
        try:
            choice = int(input())
            if choice == 1:
                gts.insert()
            elif choice == 2:
                gts.display()
            elif choice == 3:
                gts.delete()
            elif choice == 4:
                gts.update()
            elif choice == 5:
                break
            else:
                print("!Invaild input, Try again")
        except Exception as e:
            print("!Invaild Data")

if __name__ == "__main__":
    main()
         






    
    

    



