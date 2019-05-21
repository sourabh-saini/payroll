from tkinter import *
from tkinter import Tk, Canvas, Frame, BOTH
import mysql.connector
import tkinter.messagebox
import datetime

class Gui():
    def __init__(self,master):

        self.mydb = mysql.connector.connect(

            host='localhost',
            user='root',
            passwd='',
            database='payroll_management'
        )
        self.mycursor = self.mydb.cursor()
        self.sql = "select Emp_id from employee"
        self.mycursor.execute(self.sql)

        self.id_value = self.mycursor.fetchall()
        print(self.id_value)
        self.id_value=self.id_value[-1][0]
        print(self.id_value)

        self.Show_count=0
        self.insert_count=0
        self.Company_name = Label(master,text='ABCD Lmt.', font=("Helvetica", 30, "bold"), foreground='black', bg='#33E6FF')
        self.Company_name.grid(row=0,columnspan=3)

        self.Insert_data = Button(master, text="Insert Employee data", command=self.Insert, pady=5,font=("Helvetica", 10, "bold"), bg="yellow")
        self.Insert_data.grid(row=3, column=0,padx=30,pady=20)
        self.Show_data = Button(master, text="Show Employee data", command=self.Show, pady=5,font=("Helvetica", 10, "bold"), bg="yellow")
        self.Show_data.grid(row=3, column=2,pady=20)


    def Insert(self):

        print('inserted')
        print("show count ",self.Show_count)
        if self.Show_count >0:
            while self.Show_count !=0:
                self.frame1.destroy()
                print("frame1 is destroyed")
                self.Show_count=self.Show_count - 1

        self.insert_count = self.insert_count +1
        print("show count ", self.Show_count)
        print("insert count ",self.insert_count)
        print("       ")
        self.frame = Frame(root, width=300, height=60, relief=SUNKEN, pady=10, padx=10, background="white")
        self.frame.grid(row=5,columnspan=3)

        """self.Emp_id = Label(self.frame,text="Employee ID",font=("Helvetica",10,"bold"))
        self.Emp_id.grid(row=0,column=0,pady=10)
        self.Entry_Emp_id = Label(self.frame,text="{}".format(self.id_value +1),font=("Helvetica",10,"bold"))
        self.Entry_Emp_id.grid(row=0,column=1,padx=20)"""

        self.Emp_name = Label(self.frame, text="Employee Name", font=("Helvetica", 10, "bold"), background="white")
        self.Emp_name.grid(row=1, column=0,pady=10)
        self.Entry_Emp_name = Entry(self.frame)
        self.Entry_Emp_name.grid(row=1, column=1, padx=20)

        self.Basic_salary = Label(self.frame, text="Basic Salary", font=("Helvetica", 10, "bold"), background="white")
        self.Basic_salary.grid(row=2, column=0,pady=10)
        self.Entry_Basic_salary = Entry(self.frame)
        self.Entry_Basic_salary.grid(row=2, column=1, padx=20)

        self.Leave = Label(self.frame, text="No. of Leave Taken", font=("Helvetica", 10, "bold"), background="white")
        self.Leave.grid(row=3, column=0, pady=10)
        self.Entry_Leave = Entry(self.frame)
        self.Entry_Leave.grid(row=3, column=1, padx=20)

        self.insert_submit = Button(self.frame, text="Insert Data", command=self.cal_data, pady=5,font=("Helvetica", 10, "bold"), bg="yellow")
        self.insert_submit.grid(row=4, columnspan=2, pady=20)

    def Show(self):

        print("Showed")
        print("insert count ", self.insert_count)
        if self.insert_count > 0:
            while self.insert_count != 0:
                self.frame.destroy()
                print("frame is destroyed")
                self.insert_count = self.insert_count - 1

        self.Show_count = self.Show_count + 1
        print("insert count ", self.insert_count)
        print("show count ", self.Show_count)
        print("       ")
        self.frame1 = Frame(root, width=290, height=60, relief=SUNKEN, pady=10, padx=10, background="white")
        self.frame1.grid(row=5, columnspan=3, pady=20)

        self.id_lbl = Label(self.frame1, text="Emp_ID", font=("Helvetica", 12), background="white")
        self.id_lbl.grid(row=0, column=0, pady=3, sticky='e')
        self.entry_id=Entry(self.frame1)
        self.entry_id.grid(row=0,column=1,padx=20)

        """self.name_lbl = Label(self.frame1, text="Name", font=("Helvetica", 12))
        self.name_lbl.grid(row=0, column=2, pady=30, sticky='e')
        self.entry_name = Entry(self.frame1)
        self.entry_name.grid(row=0, column=3, padx=20)"""

        self.show_submit = Button(self.frame1, text="Show Data", command=self.get_data, pady=5,font=("Helvetica", 10, "bold"), bg="yellow")
        self.show_submit.grid(row=0, column=4, pady=20)



    def cal_data(self):
        self.get_name=self.Entry_Emp_name.get()
        if self.get_name.isalpha() == True:
            print("correct name")

        else:
            print("Enter correct name")

        self.get_salary=self.Entry_Basic_salary.get()
        if self.get_salary.isdigit() == True:
            print("correct salary")
        else:
            print("Enter correct salary")

        self.get_leave = int(self.Entry_Leave.get())

        if self.get_leave > 15:
            print("basic salary",self.get_salary)
            self.salary_per_day = float(float(self.get_salary) / 30)
            self.extra_days = int(self.get_leave - 15)
            self.get_salary = float(self.get_salary) - (self.salary_per_day * self.extra_days)
            print("basic salary after deduction",self.get_salary)

        self.da = float(self.get_salary) * 1.32
        self.hra = float(self.get_salary) * 0.2
        self.ma = float(self.get_salary) * 0.1
        self.pa = 500.0
        self.gross_salary = float(self.get_salary) + self.da +self.hra + self.ma + self.pa
        self.tax = float(self.gross_salary) * 0.1
        self.epf=float(self.gross_salary) * 0.12
        self.net_salary = self.gross_salary - self.tax - self.epf
        print(self.get_name, self.net_salary)

        #inserting data into db
        try:
            self.mycursor = self.mydb.cursor()
    
            self.sql="insert into employee values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            self.value=('null',self.get_name,self.Entry_Basic_salary.get(),self.da,self.get_leave,self.hra,self.ma,self.pa,self.gross_salary,self.tax,self.epf,self.net_salary)
    
            self.mycursor.execute(self.sql,self.value)
            self.mydb.commit()
    
            print("row inserted",self.mycursor.lastrowid)
            tkinter.messagebox.showinfo("Alert","Insertion Successfull,your Emp id is {}".format(self.mycursor.lastrowid))
        except mysql.connector.errors.ProgrammingError:
            tkinter.messagebox.showinfo("Alert","Insertion not Successfull")

    def get_data(self):
        """self.get_name_show = self.entry_name.get()
        if self.get_name_show.isalpha() == True:
            print("correct name")

        else:
            print("Enter correct name")"""

        self.get_id = self.entry_id.get()
        if self.get_id.isdigit() == True:
            print("correct id")
        else:
            print("Enter correct id")

        print(self.get_id)

        self.sql = "select * from employee where Emp_id={}".format(self.get_id)
        self.mycursor.execute(self.sql)

        self.myresult = self.mycursor.fetchall()

        for x in self.myresult:
            print(x)
            print(type(x[0]))

        self.canvas = Canvas(self.frame1, width=2, height=335,bg="White")
        self.canvas.grid(rowspan=12, row=1, column=1)
        self.canvas.create_line(2, 0, 2, 335)
        self.canvas1 = Canvas(self.frame1, width=310, height=2, bg="White")
        self.canvas1.grid(row=12, columnspan=3,column=0)
        self.canvas1.create_line(0, 2,310,2)
        # canvas.create_line(300, 35, 300, 200, dash=(4, 2))
        # canvas.create_line(55, 85, 155, 85, 105, 180, 55, 85)

        self.id1 = Label(self.frame1, text="Emp_ID", font=("Helvetica", 12),bg="White")
        self.id1.grid(row=1, column=0, pady=3, sticky='e')
        self.name_lbl = Label(self.frame1, text="Name", font=("Helvetica", 12),bg="White")
        self.name_lbl.grid(row=2, column=0, pady=3, sticky='e')
        self.basic_lbl = Label(self.frame1, text="Basic Salary", font=("Helvetica", 12),bg="White")
        self.basic_lbl.grid(row=3, column=0, pady=3, sticky='e')
        self.Leave_lbl = Label(self.frame1, text="No. of Leave", font=("Helvetica", 12), bg="White")
        self.Leave_lbl.grid(row=4, column=0, pady=3, sticky='e')
        self.DA_lbl = Label(self.frame1, text="Dearness Allowance", font=("Helvetica", 12),bg="White")
        self.DA_lbl.grid(row=5, column=0, pady=3, sticky='e')
        self.HRA_lbl = Label(self.frame1, text="House Rent Allowance", font=("Helvetica", 12),bg="White")
        self.HRA_lbl.grid(row=6, column=0, pady=3, sticky='e')
        self.PA_lbl = Label(self.frame1, text="Phone Allowance", font=("Helvetica", 12),bg="White")
        self.PA_lbl.grid(row=7, column=0, pady=3, sticky='e')
        self.MA_lbl = Label(self.frame1, text="Medical Allowance", font=("Helvetica", 12),bg="White")
        self.MA_lbl.grid(row=8, column=0, pady=3, sticky='e')
        self.gross_lbl = Label(self.frame1, text="Gross Salary", font=("Helvetica", 12),bg="White")
        self.gross_lbl.grid(row=9, column=0, pady=3, sticky='e')
        self.tax_lbl = Label(self.frame1, text="Tax", font=("Helvetica", 12),bg="White")
        self.tax_lbl.grid(row=10, column=0, pady=3, sticky='e')
        self.Epf_lbl = Label(self.frame1, text="EPF", font=("Helvetica", 12), bg="White")
        self.Epf_lbl.grid(row=11, column=0, pady=3, sticky='e')
        self.net_lbl = Label(self.frame1, text="Net Salary", font=("Helvetica", 12),bg="White")
        self.net_lbl.grid(row=13, column=0, pady=3, sticky='e')

        self.id1_value = Label(self.frame1, text="{}".format(self.myresult[0][0]), font=("Helvetica", 12),bg="White")
        self.id1_value.grid(row=1, column=2, pady=3, sticky='w')
        self.name_lbl_value = Label(self.frame1, text="{}".format(self.myresult[0][1]), font=("Helvetica", 12),bg="White")
        self.name_lbl_value.grid(row=2, column=2, pady=3, sticky='w')
        self.basic_lbl_value = Label(self.frame1, text="{}".format(self.myresult[0][2]), font=("Helvetica", 12),bg="White")
        self.basic_lbl_value.grid(row=3, column=2, pady=3, sticky='w')
        self.leave_lbl_value = Label(self.frame1, text="{}".format(self.myresult[0][4]), font=("Helvetica", 12),bg="White")
        self.leave_lbl_value.grid(row=4, column=2, pady=3, sticky='w')
        self.DA_lbl_value = Label(self.frame1, text="{}".format(self.myresult[0][3]), font=("Helvetica", 12),bg="White")
        self.DA_lbl_value.grid(row=5, column=2, pady=3, sticky='w')
        self.HRA_lbl_value = Label(self.frame1, text="{}".format(self.myresult[0][5]), font=("Helvetica", 12),bg="White")
        self.HRA_lbl_value.grid(row=6, column=2, pady=3, sticky='w')
        self.PA_lbl_value = Label(self.frame1, text="{}".format(self.myresult[0][6]), font=("Helvetica", 12),bg="White")
        self.PA_lbl_value.grid(row=7, column=2, pady=3, sticky='w')
        self.MA_lbl_value = Label(self.frame1, text="{}".format(self.myresult[0][7]), font=("Helvetica", 12),bg="White")
        self.MA_lbl_value.grid(row=8, column=2, pady=3, sticky='w')
        self.gross_lbl_value = Label(self.frame1, text="{}".format(self.myresult[0][8]), font=("Helvetica", 12),bg="White")
        self.gross_lbl_value.grid(row=9, column=2, pady=3, sticky='w')
        self.tax_lbl_Value = Label(self.frame1, text="{}".format(self.myresult[0][9]), font=("Helvetica", 12),bg="White")
        self.tax_lbl_Value.grid(row=10, column=2, pady=3, sticky='w')
        self.epf_lbl_Value = Label(self.frame1, text="{}".format(self.myresult[0][10]), font=("Helvetica", 12),bg="White")
        self.epf_lbl_Value.grid(row=11, column=2, pady=3, sticky='w')
        self.net_lbl_value = Label(self.frame1, text="{}".format(self.myresult[0][11]), font=("Helvetica", 12),bg="White")
        self.net_lbl_value.grid(row=13, column=2, pady=3, sticky='w')

root=Tk()
root.title("Payroll Management")
root.config(background="#33E6FF",padx=100,pady=30)
g = Gui(root)
root.resizable(width=False,height=False)

root.mainloop()