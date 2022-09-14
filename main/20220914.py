

file = "test.txt"
f = open(file, encoding='utf-8')
for line in f: 
    print(line)
f.close

file = "test.txt"
f = open(file, encoding="utf-8")
#逐行读取
for line in f:
    print(line,end="")
f.close

#with open(待打开文件) as 文件对象:
    #文件操作代码块


file = "test.txt"
# 打开文件
with open(file,encoding="utf-8") as f:
    # 读取文件全部内容
    read_str = f.read()
    print(read_str)


file = "test.txt"
with open(file, mode="w", encoding="utf-8") as f:
    #文件内容
    f.write("内容") #覆盖


file = "test.txt"
with open(file, mode= "w", encoding="utf-8") as f:
    f.write("I love fish.\n")
    f.write("I love flower.")

#文件复制
#shutil.copy(old,new)
import shutil 
shutil.copy("test.txt","aaa.txt")
shutil.copy("test.txt","../aaa.txt")




import shutil 
#复制目录。新目录存在会报错
#shutil.copytree("../1","a4")

#移动文件，目录。 修改文件名
#shtuil.move(old,new)

#删除有数据的目录：rmtree

if __name__ == '__main__':
    with open("/tmp/test.txt",'w') as f: 
        f.write("test")
    
    with open("/tmp/test.txt",'r') as f:
        print(f.read())



import hashlib
 
def file_piece_sha256(in_file_path, piece_size):
    sha256 = hashlib.sha256()
    with open(in_file_path, "rb") as in_file:
       while True:
        piece = in_file.read(piece_size)
    if piece:
        sha256.update(piece.hex().encode('utf-8'))
    else:
        break
 
    return sha256.digest().hex()
 
if __name__ == '__main__':
    ret = file_piece_sha256('file_piece_sha256.py', 128)
    print("file hash is: ", ret)






























