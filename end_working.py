import start_working
import payment

for i in range(len(start_working.employee_list)):
    print(start_working.employee_list[i] + ": " + payment.employee_list[i].salary)

print("お疲れさまでした")
