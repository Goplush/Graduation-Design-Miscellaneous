import pandas as pd
import matplotlib.pyplot as plt

# 读取CSV文件
df = pd.read_csv("Fin_lachesis_system_stats_cpu_modified_mem_percent_modified.csv")

# 将时间列转换为datetime类型
df['时间'] = pd.to_datetime(df['时间'])

# 用来正常显示中文标签
plt.rcParams['font.sans-serif']=['SimHei','Times New Roman']


# 内存使用量单位转换为MB
df['内存使用量(KB)'] = df['内存使用量(KB)'] / 1000

# 计算平均值
cpu_load_mean = df['CPU负载'].mean()
memory_usage_mean = df['内存使用量(KB)'].mean()
memory_usage_percentage_mean = df['内存使用率(%)'].mean()

# 绘制CPU负载-时间图像
plt.figure(figsize=(10, 6))
plt.plot(df['时间'], df['CPU负载'], label='CPU负载')
plt.axhline(y=cpu_load_mean, color='r', linestyle='--', label=f'CPU负载平均值: {cpu_load_mean:.2f}')
plt.xlabel('时间')
plt.ylabel('CPU负载')
plt.title('CPU负载随时间变化')
plt.legend()
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()

# 绘制内存使用量-时间和内存使用率-时间图像
fig, ax1 = plt.subplots(figsize=(10, 6))

# 内存使用量
color = 'tab:blue'
ax1.set_xlabel('时间')
ax1.set_ylabel('内存使用量(MB)', color=color)
ax1.plot(df['时间'], df['内存使用量(KB)'], color=color)
ax1.axhline(y=memory_usage_mean, color='r', linestyle='--', label=f'内存使用量平均值: {memory_usage_mean:.2f} MB')
ax1.tick_params(axis='y', labelcolor=color)

# 内存使用率
ax2 = ax1.twinx()
color = 'tab:red'
ax2.set_ylabel('内存使用率(%)', color=color)
ax2.plot(df['时间'], df['内存使用率(%)'], color=color)
#ax2.set_ylim(20.5, 21.5)  # 设置内存使用率的坐标轴范围
ax2.axhline(y=memory_usage_percentage_mean, color='g', linestyle='--', label=f'内存使用率平均值: {memory_usage_percentage_mean:.2f}%')
ax2.tick_params(axis='y', labelcolor=color)

plt.title('内存使用量和内存使用率随时间变化')
fig.autofmt_xdate(rotation=45)
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
