
incount = int(input('钱：'))

if incount < 36000:
	print(incount -  incount * 0.03)
elif incount > 36000 and incount < 144000:
	print(incount - 36000 * 0.03 - (incount - 36000) * 0.1)
elif incount >144000 and incount <300000:
	print(incount - 36000 * 0.03 - (incount - 144000)* 0.2 )
else:
	print(incount - 36000 * 0.03 - (incount - 300000) * 0.25)

