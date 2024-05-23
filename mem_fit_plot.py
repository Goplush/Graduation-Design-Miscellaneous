import csv
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# 读取CSV文件中的数据
time = []
memory_usage = []
with open('Fin_lachesis_system_stats_cpu_modified_mem_percent_modified.csv', mode='r') as file:
    csv_reader = csv.DictReader(file)
    i=0
    for row in csv_reader:
        time.append(i)
        i=i+1
        memory_usage.append(float(row['内存使用量(KB)']))


# 定义线性函数模型
def linear_function(x, a, b):
    return a * x + b

# 使用最小二乘法拟合线性函数
params, _ = curve_fit(linear_function, time, memory_usage)

# 获取拟合后的参数
a, b = params

# 计算拟合后的内存使用量
memory_fit = linear_function(np.array(time), a, b)

# 绘制内存使用量和拟合函数的图表

# 用来正常显示中文标签
plt.rcParams['font.sans-serif']=['SimHei','Times New Roman']
plt.figure(figsize=(10, 6))
plt.scatter(time, memory_usage, label='内存使用量')
plt.plot(time, memory_fit, color='red', linestyle='--', label='拟合函数: {:.2f}x + {:.2f}'.format(a, b))
plt.axhline(y=np.mean(memory_usage), color='green', linestyle='-', label='平均内存使用量: {:.2f} KB'.format(np.mean(memory_usage)))
plt.xlabel('时间 (秒)')
plt.ylabel('内存使用量 (KB)')
plt.title('内存使用量随时间变化的线性拟合')
plt.legend()
plt.grid(True)
plt.show()
