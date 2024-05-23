
# 输出文件路径
output_file="system_stats.csv"

# 写入 CSV 文件头
echo "时间,CPU负载,内存使用量(MB),内存使用率(%)" > "$output_file"

while true; do
    # 获取当前时间
    current_time=$(date +"%H:%M:%S")

    # 获取CPU平均负载
    load=$(cat /proc/loadavg | cut -d ' ' -f 1-3)

    # 获取内存使用量（单位：KB）
    memory_usage=$(free -k | grep Mem | sed 's/ \+/ /g' | cut -d ' ' -f 3)

    # 获取内存总量（单位：KB）
    memory_total=$(free -k | grep Mem | sed 's/ \+/ /g' | cut -d ' ' -f 2)

    # 计算内存使用率
    memory_usage_percentage=$((memory_usage * 100 / memory_total))

    # 写入数据到 CSV 文件
    echo "$current_time,$load,$memory_usage,$memory_usage_percentage" >> "$output_file"

    # 等待一秒钟
    sleep 1
done
