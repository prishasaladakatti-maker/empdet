def employee_info(name, emp_id, department, salary):
    details = (
        "Employee Name: " + name + "\n"
        "Employee ID: " + str(emp_id) + "\n"
        "Department: " + department + "\n"
        "Salary: " + str(salary)
    )
    return details


# Main program
result = employee_info("Prisha", 101, "Computer Science", 50000)
print(result)