import re
import os
 
 
file_name = "网站访问日志.txt"
 
 
 
 
def read_txt(filename):
    """
    读取文件中的数据
    :param filename: 文件名
    :return: 返回文件数据列表
    """
    if os.path.exists(filename):
        with open(filename, "r") as file:
            log_list = file.readlines()
            if log_list:
                return log_list
 
 
 
 
def total(filename, name):
    """
    统计文件中所有的pv数，uv数，设备列表等
    :param filename: 需要处理的文本
    :param name: 传入需要返回哪个数据列表
    :return: 根据name 返回对应的列表
    """
    uv_list = []  # 统计所有的uv数量
    pv_list = []  # 统计所有的pv数量
    equipment_list = []  # 统计所有的设备来源
    log_list = read_txt(filename)  # 读取文本中的数据
    for log in log_list:
        # 1.统计本日志文件的总uv
        re_obj1 = re.match(r"(\d{1,3}\.){3}\d{1,3}", log.strip())
        if re_obj1:
            uv_list.append(re_obj1.group())
        # 2.将符合的pv追加到列表中
        pv_list.append(log.split("\"")[1])
        # 3.将符合的设备来源添加到列表中
        mozilla_index = log.find("Mozilla/5.0")
        r_index = log.find(")", mozilla_index)
        if mozilla_index != -1 and r_index != -1:
            equipment_list.append(log[mozilla_index: r_index + 1])
    if name == "uv":
        return uv_list
    elif name == "pv":
        return pv_list
    elif name == "equipment":
        return equipment_list
 
 
 
 
def every_hour(filename):
    """
    列出全天每小时的pv、uv数
    :param filename: 文件名
    :return: 无
    """
    temp_hour = "00"
    count = 0
    log_list = read_txt(filename)
    every_hour_uv = []
    for log in log_list:
        hour = re.search(r"\[.*\]", log).group().split(":")[1]
        value = ""
        if re.match(r"(\d{1,3}\.){3}\d{1,3}", log.strip()):
            value = re.match(r"(\d{1,3}\.){3}\d{1,3}", log.strip()).group()
        if temp_hour == hour:
            if value not in every_hour_uv:
                every_hour_uv.append(value)
            count += 1
            if temp_hour == "23" and log == log_list[-1]:
                print(f"全天{temp_hour}~第二天00时间段的uv数量为:{len(every_hour_uv) - 1}", end=" ")
                print(f"pv数量为:{count}")
        else:
            # 因为文件中每一行的数据有些并不是以ip开头 所以就会存在为空
            # 那么第一次为空的时候在列表中是不存在的 所以要减去为空白的一次
            temp = temp_hour
            temp_hour = hour
            print(f"全天{temp}~{temp_hour}时间段的uv数量为:{len(every_hour_uv) - 1}", end=" ")
            print(f"pv数量为:{count}")
            count = 1
            every_hour_uv.clear()
            every_hour_uv.append(value)
 
 
 
 
def show(filename, name, default=1):
    """
    根据传入的名称 统计指定的值以及其对应的数量 并选择是否排序及个数
    :param default: 结果默认降序排列 并且取出前10个数据
    :param filename: 文件名
    :param name: 统计的名称
    :return: 返回字典 key:为要查询的名称 value:为其对应的数量
    """
    name1_list = total(filename, name)
    # 对数据进行去重
    name1_set = set(name1_list)
    # 定义字典用于返回结果
    name1_dict = {}
    if name == "uv":
        for name1 in name1_set:
            if name1 not in name1_dict:
                name1_dict[name1] = name1_list.count(name1)
    elif name == "pv":
        for pv in name1_set:
            try:
                new_pv = pv.split(" ")[1]
                if new_pv not in name1_dict:
                    name1_dict[new_pv] = name1_list.count(pv)
            except IndexError as e:
                pass
    elif name == "equipment":
        for equipment in name1_set:
            if equipment not in name1_dict:
                name1_dict[equipment] = name1_list.count(equipment)
    top10_name = sorted(name1_dict.items(), key=lambda item: item[1], reverse=True)[:10]
    return top10_name
 
 
 
 
if __name__ == "__main__":
    print(total(file_name, "uv"))  # 测试统计uv数量
    every_hour(file_name)  # 测试统计一天每小时的uv pv数量
    print(show(file_name, "pv"))  # 测试top10 pv数量