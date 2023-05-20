
X = [[12, 7, 3],
     [4, 5, 6],
     [7, 8, 9]]
 
 
Y = [[5, 8, 1],
     [6, 7, 3],
     [4, 5, 9]]
 
 
result = [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]  # 初始化结果
 
 
for i in range(len(X)):  # 迭代三次 拿到每一个列表
    for j in range(len(X[0])):  # 拿到列表中的元素
        result[i][j] = X[i][j] + Y[i][j]
 
 
for i in result:
    print(i)