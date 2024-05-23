import csv

# 定义存储提取信息的列表
gossip_time = []
total_events = []
consensus_events = []

# 读取日志文件
with open('out.txt', 'r') as file:
    lines = file.readlines()

# 提取信息并添加到相应列表中
for line in lines:
    if "Gossip Runtime" in line:
        gossip_time.append(float(line.split(':')[1].strip().split()[0]))
    elif "Num. of Events" in line:
        total_events.append(int(line.split(':')[1].strip()))
    elif "Num. of Consensus Events" in line:
        consensus_events.append(int(line.split(':')[1].strip()))

# 将提取的信息写入CSV文件
with open('hashgraph_gossip_info.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Gossip Runtime', 'Num. of Events', 'Num. of Consensus Events'])
    for i in range(len(gossip_time)):
        writer.writerow([gossip_time[i], total_events[i], consensus_events[i]])

print("数据已成功写入hashgraph_gossip_info.csv文件。")
