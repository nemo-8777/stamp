import subprocess

employee_list = []

class working:
    def __init__(self):
        in_time_h = 0
        in_time_m = 0
        up_time_h = 0
        up_time_m = 0
        wage = 1000
        salary = 0
    def cal_salary(self):
        working_time_h = self.up_time_h - self.in_time_h
        working_time_m = self.up_time_m - self.in_time_m
        self.salary = self.wage * (working_time_h + working_time_m / 60)
        return self.salary

print("本日の出勤者を入力してください\n終了する場合は'X'と入力してください")

while(True):
    name = input()
    if(name!="X"):
        employee_list.append(name)
        index = employee_list.index(name)
        employee_list[index] = working()
    else:
        subprocess.run("python input_employee.py")
        break
