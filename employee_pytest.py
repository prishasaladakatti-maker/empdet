from employee import employee_info

def test_employee_info():
    result = employee_info("Prisha", 101, "Computer Science", 50000)

    expected = (
        "Employee Name: Prisha\n"
        "Employee ID: 101\n"
        "Department: Computer Science\n"
        "Salary: 50000"
    )

    assert result == expected