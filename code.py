# Life Management System


class life:
    def __init__(self):
        self.records=[]
        self.obje=[]
        self.bille=[]

    def money(self):
        print("\n========== Money Management ==========")
        print("Enter the details below.")
        amount=int(input("Enter the amount (Rs): "))
        print("\nSelect an option:")
        print("1. Borrow")
        print("2. Lend")
        choose=int(input("Enter your choice (1 or 2): "))
        bor=[]
        if choose==1:
            bor.append("borrowed")
        elif choose==2:
            bor.append("lent")
        else:
            print("Invalid option. Please choose 1 or 2.")
            return
        date=input("Enter the date (DD/MM/YYYY): ")
        a=f"{amount} amount is {bor[0]} on {date}."
        self.records.append(a)
        print("\nRecord added successfully!")
        print(a)

    def thing(self):
        print("\n========== Things Management ==========")
        obj=input("Enter the item name: ")
        daty=input("Enter the date (DD/MM/YYYY): ")
        print("\n1. Borrow\n2. Lend")
        opt=int(input("Enter your choice (1 or 2): "))
        a=[]
        if opt==1:
            a.append("borrowed")
        elif opt==2:
            a.append("lent")
        else:
            print("Invalid option.")
            return
        c=f"{obj} is {a[0]} on {daty}."
        self.obje.append(c)
        print("\nRecord added successfully!")
        print(c)

    def rent(self):
        print("\n========== Bills Management ==========")
        name=input("Enter the bill name: ")
        date=input("Enter the due date (DD/MM/YYYY): ")
        amount=int(input("Enter the bill amount (Rs): "))
        d=f"{name} bill must be paid before {date}. Amount: Rs {amount}."
        self.bille.append(d)
        print("\nBill added successfully!")
        print(d)

    def modify(self):
        print("\n========== Delete Records ==========")
        print("1. Money\n2. Things\n3. Bills")
        mod_opt=int(input("Choose an option: "))
        if mod_opt==1:
            print(self.records)
            i=int(input("Enter the record number to delete: "))
            if i<=len(self.records):
                self.records.pop(i-1); print("Record deleted successfully.")
        elif mod_opt==2:
            print(self.obje)
            i=int(input("Enter the record number to delete: "))
            if i<=len(self.obje):
                self.obje.pop(i-1); print("Record deleted successfully.")
        elif mod_opt==3:
            print(self.bille)
            i=int(input("Enter the record number to delete: "))
            if i<=len(self.bille):
                self.bille.pop(i-1); print("Record deleted successfully.")
        else:
            print("Invalid option.")

    def display(self):
        print("\n========== All Records ==========")
        print("\nMoney Records")
        for i,item in enumerate(self.records,1):
            print(f"{i}. {item}")
        print("\nThings Records")
        for i,item in enumerate(self.obje,1):
            print(f"{i}. {item}")
        print("\nBills")
        for i,item in enumerate(self.bille,1):
            print(f"{i}. {item}")

life=life()

def system():
    while True:
        print("""
========================================
        LIFE MANAGEMENT SYSTEM
========================================
1. Money Management
2. Things Management
3. Bills Management
4. Delete a Record
5. View All Records
6. Exit
========================================
""")
        choice=int(input("Enter your choice (1-6): "))
        if choice==1:
            life.money()
        elif choice==2:
            life.thing()
        elif choice==3:
            life.rent()
        elif choice==4:
            life.modify()
        elif choice==5:
            life.display()
        elif choice==6:
            print("Thank you for using Life Management System. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

system()
