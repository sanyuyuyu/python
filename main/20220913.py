def get_data_from_file1(path: str) -> str:
    """获取path 例如:data.txt文件里的内容"""


    data = ''
    
    with open(path, 'r') as file:      
        for line in file.readlines():
            #输出111.
           if '111.\n' in line:
            data += line 
            print(data)

    return data       
          

data = get_data_from_file1("data.txt")




def get_data_from_file1(path: str) -> str:
    data = ''
    with open(path, 'r') as file:      
        for line in file.readlines():
            #输出111.
           if line == '111.':
            data += line 
            print(data)

    return data  

data = get_data_from_file1("data.txt")

















