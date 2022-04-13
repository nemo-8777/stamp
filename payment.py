import sys
import datetime
import start_working

dt = datetime.datetime.now()

def in_time(employee_name):
    index = start_working.employee_list.index(employee_name)
    start_working.employee_list[index].in_time_h = dt.hour
    start_working.employee_list[index].in_time_m = dt.minute

def up_time(employee_name):
    index = start_working.employee_list.index(employee_name)
    start_working.employee_list[index].up_time_h = dt.hour
    start_working.employee_list[index].up_time_minute = dt.minute
    today_salary = employee_name.cal_salary()
    return today_salary

if __name__ == "__main__":
    if sys.argv[1] == "in":
            employee_list = []
            in_time(sys.argv[2])

    elif sys.argv[1] == "up":
            up_time(sys.argv[2])
    else:
        print("input error")