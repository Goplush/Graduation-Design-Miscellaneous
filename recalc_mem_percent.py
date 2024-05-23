import csv

# 用户空间内存大小（KB）
total_memory_kb = 3915620.352
file_name = 'lachesis_system_stats_cpu_modified'

# 打开CSV文件
with open(file_name+'.csv', mode='r') as file:
    csv_reader = csv.DictReader(file)
    fieldnames = csv_reader.fieldnames

    # 创建一个新的CSV文件来写入更新后的数据
    with open(file_name+'_mem_percent_modified.csv', mode='w', newline='') as updated_file:
        writer = csv.DictWriter(updated_file, fieldnames=fieldnames)
        writer.writeheader()

        # 逐行读取原始数据，并更新内存使用率列
        for row in csv_reader:
            memory_usage_kb = sum(map(int, row['内存使用量(KB)'].split()))
            memory_usage_percent = (memory_usage_kb / total_memory_kb) * 100
            row['内存使用率(%)'] = '{:.4f}'.format(memory_usage_percent)
            writer.writerow(row)

print("内存使用率已更新并保存到 updated_data.csv 文件中。")
