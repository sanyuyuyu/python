"""
1 双色球（假设一共八个球，6个红球，球号1-32、2个蓝球，球号1-16）
2 确保用户不能重复选择，不能超出范围
3 用户输入有误时有相应的错误提示
4 最后展示用户选择的双色球的号码
"""
# 没有卡输入的内容为空时的情况
print("Welcome to 小猿圈 lottery station")
 
 
red_ball_list = []  # 用于存储选中的红球号
blue_ball_list = []  # 用于存储选中的蓝球号
i = 1  # 提示用户输入红球号时候带编号 [1] [2]
j = 1  # 提示用户输入蓝球号时候带编号 [1] [2]
 
 
# 用户一直在选 所以采用死循环
while True:
    # 判断红球号是否已经有效选择6次 如果是则开始选篮球号
    if len(red_ball_list) == 6:
        # 篮球号选择有效的2次 则退出循环
        if len(blue_ball_list) == 2:
            break
 
 
        blue_ball_str = input("\033[34m["+str(j)+"]select blue ball:"+"\033[0m")
        blue_ball_num = 0  # 初始化值
        # 判断是否输入的内容是否为空或者是输入的是字母
        if blue_ball_str.isdigit():
            blue_ball_num = int(blue_ball_str)
            if 1 <= blue_ball_num <= 16:
                if blue_ball_num not in blue_ball_list:
                    blue_ball_list.append(blue_ball_num)
                    j += 1
                else:
                    print(f"number {blue_ball_num} is already exist in blue ball list")
            else:
                print("only can select n between 1-16")
        else:
            print("only can input num")
    else:
        red_ball_str = input("\033[31m[" + str(i) + "]select red ball" + "\033[0m:")
        if red_ball_str.isdigit():
            red_ball_num = int(red_ball_str)
            if 1 <= red_ball_num <= 32:
                if red_ball_num not in red_ball_list:
                    red_ball_list.append(red_ball_num)
                    i += 1
                else:
                    print(f"number {red_ball_num} is already exist in red ball list")
            else:
                print("only can select n between 1-32")
        else:
            print("only can input num")
print()
print()
print("Red ball:", red_ball_list)
print("Blue ball:", blue_ball_list)
print("Good Luck.")