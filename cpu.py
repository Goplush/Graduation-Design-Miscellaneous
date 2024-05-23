import pandas as pd

file_name = 'lachesis_system_stats'

# 读取CSV文件
df = pd.read_csv(file_name+".csv")

# 修改CPU负载列
df["CPU负载"] = df["CPU负载"].apply(lambda x: x.split()[1])  # 保留最近五分钟内的平均负载

# 保存修改后的CSV文件
df.to_csv(file_name+"_cpu_modified.csv", index=False)
