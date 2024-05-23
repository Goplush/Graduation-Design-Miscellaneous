import csv
from datetime import datetime
file_name = ''

def convert_time_format(input_file, output_file):
    with open(input_file, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        rows = list(reader)

    for row in rows:
        time_str = row['时间']
        time_obj = datetime.strptime(time_str, '%Y-%m-%d %H:%M:%S')
        row['时间'] = time_obj.strftime('%H:%M:%S')

    with open(output_file, 'w', newline='') as csvfile:
        fieldnames = reader.fieldnames
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

if __name__ == "__main__":
    input_file = file_name+'.csv'  # 输入CSV文件的路径
    output_file = file_name+'_time_reformatted.csv'  # 输出CSV文件的路径
    convert_time_format(input_file, output_file)
