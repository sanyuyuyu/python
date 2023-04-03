
fi = open("aaa.txt","r",encoding="utf-8")
fo = open("aaa.txt", "w", encoding="utf-8")
flag = False
for line in fi:
    if "【原文】" in line:
        flag = True
        continue
    if "【注释】" in line:
        flag = False
    line = line.strip("\n")
    line = line.lstrip().rstrip()
    if flag:
        print(line)
        if line:
        	fo.write(line+"\n")
fo.close()
fi.close()     



