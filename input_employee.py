import subprocess

in_or_up = ""
who_areyou = ""

print("yeah!")
while(True):
    print("出勤なら'I'退勤なら'U'と入力してください\n業務を終了する場合'E'と入力してください")
    in_or_up = input()

    if in_or_up == "E":
        subprocess.call("python end_working.py")
        break

    print("名前を入力してください")
    name = input()

    subprocess.call("python payment.py " + in_or_up + " " + name)
