import csv
import matplotlib.pyplot as plt
import numpy as np

# 读取CSV文件
csv_file = "Fin_lachesis_stats.csv"
consensus_events = []
total_events = []

# 用来正常显示中文标签
plt.rcParams['font.sans-serif']=['SimHei','Times New Roman']

with open(csv_file, 'r') as file:
    reader = csv.reader(file)
    next(reader)  # 跳过表头
    for row in reader:
        consensus_event = int(row[2])
        total_event = int(row[1])
        total_events.append(total_event)
        consensus_events.append(consensus_event)

# 计算每秒钟未达成共识的事件
unresolved_events = [total - consensus for total, consensus in zip(total_events, consensus_events)]

# 计算CDF
def calculate_cdf(unresolved_events, X):
    count = 0
    for event in unresolved_events:
        if event <= X:
            count += 1
    return count / len(unresolved_events)

# 计算PDF
def calculate_pdf(unresolved_events, X):
    count = 0
    for event in unresolved_events:
        if event == X:
            count += 1
    
    #不能除0
    if X==0:
        return  count / (len(unresolved_events) * 0.00000001)
    return count / (len(unresolved_events) * X)

# 计算每个整数X对应的CDF和PDF值
X_values = list(range(max(unresolved_events) + 1))
CDF_values = [calculate_cdf(unresolved_events, X) for X in X_values]
PDF_values = [calculate_pdf(unresolved_events, X) for X in X_values]

# 绘制图表
fig, ax1 = plt.subplots()

# 绘制累积分布函数图像
color = 'tab:blue'
ax1.set_xlabel('未达成共识的事件数目')
ax1.set_ylabel('累积分布函数', color=color)
ax1.plot(X_values, CDF_values, color=color, marker='o', linestyle='-')
ax1.tick_params(axis='y', labelcolor=color)

# 添加第二个y轴，用于绘制PDF
ax2 = ax1.twinx()
color = 'tab:red'
ax2.set_ylabel('分布密度函数', color=color)
ax2.plot(X_values, PDF_values, color=color, marker='s', linestyle='--')
ax2.tick_params(axis='y', labelcolor=color)

plt.title('未达成共识的事件的数目的累积分布函数和分布密度函数')
plt.grid(True)
plt.tight_layout()

# 显示图表
plt.show()
