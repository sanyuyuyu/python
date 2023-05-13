for i in range(100,1000):
	    ge_wei = i % 10
	    shi_wei = i // 10 % 10
	    bai_wei = i // 100
	    if i == (ge_wei ** 3 + shi_wei ** 3 + bai_wei ** 3):
	        print(i)
