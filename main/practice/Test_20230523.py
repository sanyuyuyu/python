import os
 
 
# TODO 1.读取文件 判断文件是否存在 存在则读取 判断文件内容是否为空
if os.path.exists("stock_data.txt"):
    with open("stock_data.txt", "r") as file:
        stock_data = file.readlines()
 
 
    # TODO 2.如果读取的数据不为空 则继续进行后续操作
    while stock_data:
        query_info = input("股票查询接口>>:")
        if query_info.count("<") == 1 or query_info.count(">") == 1:
            # TODO 2.1 用户录入数据时录入符号
            symbol = ">" if query_info.find("<") == -1 else "<"  # 指定用户录入时的符号
            name, num_str1 = query_info.split(symbol)  # 按照用户录入的符号进行切割 得到要查找的比较类型以及数字
            if stock_data[0].strip().find(name) != -1:  # 判断
                index = stock_data[0].strip().split(",").index(name)  # 得到类型在列表出现的位置
                print(stock_data[0].strip().split(","))  # 展示
                total_list = []
                for i in range(1, len(stock_data)):
                    temp_list = stock_data[i].strip().split(",")
                    # 根据类型在列表中出现的位置查找对应的其对应的数据
                    num_str2 = temp_list[index].replace("%", "") if temp_list[index].find("%") != -1 else temp_list[
                        index]
                    # 判断表达式 符合条件的往总列表中添加
                    if eval(str(float(num_str2) > float(num_str1))) if symbol == ">" else eval(str(
                            float(num_str2) < float(num_str1))):
                        total_list.append(temp_list)
                for i in total_list:
                    print(i)
                print(f"找到{len(total_list)}条")
        else:
            # TODO 2.2 用户录入数据时没有符号的情况
            name_list = [stock.strip().split(",") for stock in stock_data if
                         stock.strip().split(",")[2].find(query_info) != -1]
            # 展示
            for name in name_list:
                print(name)
            print(f"找到{len(name_list)}条")