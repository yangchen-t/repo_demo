import pandas as pd
from datetime import datetime, timedelta

# 获取当前日期
start_date = datetime.now().replace(month=7,day=1)
print(start_date)
# 计算下个月的第一天
end_date = (start_date + timedelta(days=52)).replace(day=1)

# 生成日期范围
date_range = pd.date_range(start=start_date, end=end_date, freq='D')

# 过滤出周六和周日
weekend_dates = date_range[date_range.weekday.isin([5, 6])]

# 创建DataFrame
df = pd.DataFrame({'Date': weekend_dates})

# 将日期转换为月份格式
df['Date'] = df['Date'].dt.strftime('%Y-%m-%d')

# 值班人员列表
duty_personnel = ["陈向洋", "王涛", "马艳文", "王静博"]

# 计算每个周末日期对应的值班人员
repeated_personnel = [duty_personnel[i % len(duty_personnel)] for i in range(len(weekend_dates))]

if len(repeated_personnel) != len(df):
    for i in range(len(duty_personnel)):
        repeated_personnel.append(duty_personnel[i])
        if len(repeated_personnel) == len(df):
            break
else:
    pass

# 更新DataFrame中的值班人员列
df['值班人员'] = repeated_personnel

# 计算每个人对应的英国值班人员
uk_duty_personnel = []
for person in repeated_personnel:
    uk_duty_personnel += [person, person] 
    if len(uk_duty_personnel) == len(df):
        break

# 截取与日期数量相匹配的长度
uk_duty_personnel = uk_duty_personnel[:len(df)]

# 更新DataFrame中的英国值班人员列
df['英国值班人员'] = uk_duty_personnel

# 输出到CSV文件
csv_file = 'system.csv'
df.to_csv(csv_file, index=False)
