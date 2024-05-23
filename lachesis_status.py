import csv
from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np

# 读取CSV文件
csv_file = "Fin_lachesis_stats.csv"

timestamps = []
total_events = []
consensus_events = []

with open(csv_file, 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        # 将时间戳字符串转换为datetime对象
        timestamp = datetime.strptime(row['timestamp'], '%H:%M:%S')
        timestamps.append(timestamp)
        total_events.append(int(row['total_events']))
        consensus_events.append(int(row['consensus_events']))

# 计算每秒钟未达成共识的事件
unresolved_events = [total - consensus for total, consensus in zip(total_events, consensus_events)]

# 计算未达成共识事件数目的平均值
average_unresolved = np.mean(unresolved_events)

# 绘制图表
plt.plot(timestamps, unresolved_events, marker='o', linestyle='-', label='Unresolved Events')
plt.axhline(y=average_unresolved, color='r', linestyle='--', label='Average Unresolved Events')
plt.title('Unresolved Events Over Time')
plt.xlabel('Time')
plt.ylabel('Unresolved Events')
plt.xticks(rotation=45)
plt.tight_layout()
plt.grid(True)
plt.legend()
plt.show()
