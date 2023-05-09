# def triagnles():
# 	n = [1]
# 	yield n 
# 	while(True):
# 		n = [v + n[k-1] if(k > 0 and k<=(len(n)-1)) else v for k,v in enumerate(n)]
# 		n.append()
# 		yield n
# print(triagnles())

def triangles():
    L = [1]
    yield L
    while True:
        L = [v+w for v,w in zip([0]+L,L+[0])]
        yield L
        
for i,row in enumerate(triangles()):
    print(row)
    if i>=10:
        break