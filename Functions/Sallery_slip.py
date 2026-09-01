Employee_detail = {}

def emp_sallery():
    Employee_detail["ID :"] = int(input("Enter Employee ID :"))
    Employee_detail["Name :"] = input("Enter Employee Name :")
    Employee_detail["Department :"] = input("Enter Employee Department :")
    Employee_detail["Designation :"] = input("Enter Employee Designation :")

    salry = int(input("Enter Basic Sallery :"))
    hra = int(input("Enter House Rent Allowance :"))
    DA = int(input("Enter Dearness Allowance :"))
    bonus = int(input("Enter Bonus :"))

    PF = int(input("Enter Provident Fund :"))
    Tax = int(input("Enter Tax :"))

    Gross_sallery = salry + hra + DA + bonus

    Total_deduction = PF + Tax

    Net_sallery = Gross_sallery - Total_deduction

    Employee_detail["Gross Sallery :"] = Gross_sallery
    Employee_detail["Total Deduction :"] = Total_deduction
    Employee_detail["Net Sallery :"] = Net_sallery

emp_sallery()

for key,value in Employee_detail.items():
    print("_______________________")
    print(f"{key} : {value}")


