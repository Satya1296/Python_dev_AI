from employee import Employee
def main():
    print("Company Name:", Employee.company_name)
    print("Employees Before:", Employee.get_total_employees())

    emp1=Employee(101,"Alice","HR",40000,"ABCDE1234F")
    emp2=Employee(102,"Bob","IT",50000,"PQRSX9876Z")

    print("\nEmployee Details")
    print(emp1)
    print(emp2)

    print("\nEmployees after:", Employee.get_total_employees())
    print("PF for e1: ",emp1.calculate_pf())

    emp1.apply_hike(10)
    print("After 10% hike:",emp1.salary)

    print(emp1.transfer_department("Data Science"))

    print("is valid salary(9000):", Employee.is_valid_salary(9000))

    try:
        emp1.salary=5000
    except Exception as e:
        print("Blocked:",e)

    try:
        emp1.emp_id=999
    except Exception as e:
        print("Blocked:",e)

    print("protected:",emp1._department)

    print("private:",emp1._Employee__pan_number)

if __name__ == "__main__":
    main()
