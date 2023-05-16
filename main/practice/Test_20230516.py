tour = []
height = []
hei = 100 
tim = 10
for i in range(1,tim+1):
	if i == 1:
		tour.append(hei)
	else:
		tour.append(2 * hei)
	hei /= 2
	height.append(hei)
print(f'总高度：tour = {sum(tour)}')
print(f'第十次反弹高度：height = {height[-1]}')




