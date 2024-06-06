from flask import Flask, render_template, jsonify
import openpyxl
from datetime import datetime, time

app = Flask(__name__)

# 读取 Excel 文件
workbook = openpyxl.load_workbook('/config/system.xlsx')
sheet = workbook.active

def ensure_two_elements(arr) -> list:
    if len(arr) < 2:
        while len(arr) < 2:
            arr.append("null")
    return arr

def get_non_empty_values_for_datetime(sheet, target_datetime) -> list:
    for row in sheet.iter_rows(values_only=True):
        if len(row) > 0:
            if isinstance(row[0], datetime) and row[0].date() == target_datetime.date():
                # 仅保留非空值
                InfrastructurePerson = [cell for cell in row[1:] if cell is not None]
                return InfrastructurePerson
    return "null"
def get_duty_personnel() -> list:
    target_date = datetime.now().date()  # 获取当前日期
    target_datetime = datetime.combine(target_date, time())  

    duty_person = ensure_two_elements(get_non_empty_values_for_datetime(sheet, target_datetime))
    return duty_person

# 定义路由和视图函数
@app.route('/')
def display_duty_schedule() -> any:
    target_date = datetime.now().date()
    duty_person = get_duty_personnel()
    return render_template('duty_schedule.html', in_duty_person=duty_person[0], en_duty_person=duty_person[1])

@app.route('/get_duty_personnel')
def get_updated_duty_personnel() -> str:
    duty_person = get_duty_personnel()
    return duty_person[0] + ', ' + duty_person[1]

if __name__ == '__main__':
    app.run(debug=True, host="192.168.103.172", port=80)