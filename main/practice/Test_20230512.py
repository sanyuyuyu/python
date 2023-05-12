count = 0
i = 101
while i < 200:
	j = 2
	while j < i / 2:
		if i % j == 0:
			break 
		j += 1
	else:
		count += 1
		print(i)
	i += 1
print(f"The total is {count}")
count = 0

for i in range(101, 201):
    for j in range(2, int(i / 2)):  
        if i % j == 0:
            break
    else:
        count += 1
        print(i)
print(f"The total is {count}")