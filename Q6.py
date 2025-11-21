# Program to read employee name and salary until "stop"
# Then calculate total salary (Basic + HRA 20% + DA 10%)

staff_list = []   # list to store (employee_name, basic_pay)

while True:
    worker_name = input("Enter employee name (type 'stop' to end): ")

    if worker_name.lower() == "stop":
        break

    basic_pay = int(input("Enter basic salary: "))
    
    staff_list.append((worker_name, basic_pay))


# Display total salary
print("\n--- Employee Salary Details ---")

for worker_name, basic_pay in staff_list:
    hra = basic_pay * 0.20
    da = basic_pay * 0.10
    total_pay = basic_pay + hra + da

    print(f"Name: {worker_name}, Total Salary: {total_pay}")
