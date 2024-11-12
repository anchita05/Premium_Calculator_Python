import pymysql as pm
from tkinter import *
conn = pm.connect(
        host = "localhost",
        user = "root",
        passwd = "mysql"
    )
cursor = conn.cursor()
cursor.execute("use project2022")
def tk_calculator():
    root=Tk()
    t=StringVar(root)
    label_name=Label(root,text="Enter your Name: ")
    text0=Entry(root,textvariable=t)
    label_name.grid(row=0,column=0)
    text0.grid(row=0,column=1)

    a=StringVar(root)
    label_phno=Label(root,text="Phone Number: ")
    text2=Entry(root,textvariable=a)
    label_phno.grid(row=2,column=0)
    text2.grid(row=2,column=1)

    b=StringVar(root)
    label_destination=Label(root,text="Enter your Destination: ")
    text3=Entry(root,textvariable=b)
    label_destination.grid(row=3,column=0)
    text3.grid(row=3,column=1)

    c=StringVar(root)
    label_address=Label(root,text="Enter your Address: ")
    text4=Entry(root,textvariable=c)
    label_address.grid(row=4,column=0)
    text4.grid(row=4,column=1)

    d=StringVar(root)
    label_duration=Label(root,text="Enter your Duration: ")
    text5=Entry(root,textvariable=d)
    label_duration.grid(row=5,column=0)
    text5.grid(row=5,column=1)

    e=StringVar(root)
    label_age=Label(root,text="Enter your Age: ")
    text6=Entry(root,textvariable=e)
    label_age.grid(row=6,column=0)
    text6.grid(row=6,column=1)

    f=StringVar(root)
    label_plan=Label(root,text="Enter your coverage plan 50k(1)/100k(2)/250k(3): ")
    text7=Entry(root,textvariable=f)
    label_plan.grid(row=7,column=0)
    text7.grid(row=7,column=1)
     
    premium=""
    def main():
        name = t.get()
        phno = a.get()
        dest = b.get()
        address = c.get()
        days = d.get()
        age = e.get()
        plan = f.get()
        age1=int(e.get())
        plan1=int(f.get())
        
        if age1 <= 50:
            agegrp = "3m_50y"
        elif age1 <= 60:
            agegrp = "51_60"
        elif age1<=70:
            agegrp = "61_70"
        else:
            print('No premium available!!! Age group should be between 3 Months and 70 Years')
        if plan1 == 1:
            plan1 = "premium50"
        elif plan1 == 2:
            plan1 = "premium100"
        else:
            plan1 = "premium250"
        
        global premium
        
        query = f"select {agegrp} from {plan1} where days = {days}"
        cursor.execute(query)
        premium = cursor.fetchone()[0]
        
        sql = "insert into customer values(%s,%s,%s,%s,%s,%s,%s,%s)"
        values = name,phno,dest,address,days,age,plan1,premium
        cursor.execute(sql,values)
        conn.commit()
        
        print("Your premium is :",premium)
        x=StringVar(root)
        x.set('your premium is '+str(premium))  
        answer=Label(root,textvariable= x)   
        answer.grid(row=12)  

    button2=Button(root,text="Premium",command=main)
    button2.grid(row=9)
        
    root.mainloop()

def update_command():
    oldField = input("Enter old field : ")
    oldValue = input("Enter old value : ")
    newField = input("Enter new field : ")
    newValue = input("Enter new value : ")
    query = f"update customer set {newField} = '{newValue}' where {oldField} = '{oldValue}'"
    print(query)
    cursor.execute(query)
    conn.commit()

def delete_command():
    field = input("Enter field : ")
    value = input("Enter value : ")
    query = f"delete from customer where {field} = '{value}'"
    print(query)
    cursor.execute(query)
    conn.commit()

ch='yes'
while (ch=='yes'):
    print('1.Calculate Premium')
    print('2.Update Record')
    print('3.Delete Record')
    op=int(input('Enter Your Option Number: '))
    if op==1:
        tk_calculator()
    elif op==2:
        update_command()
    elif op==3:
        delete_command()
    else:
        print('WRONG INPUT!!! PLEASE ENTER CORRECT OPTION NUMBER FROM 1/2/3')
        break
    ch=input('Do you want to continue? Yes/No: ')